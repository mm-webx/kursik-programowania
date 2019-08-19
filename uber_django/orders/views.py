from django import views
from django.http import HttpResponse, JsonResponse

from accounts.models import Profile
from orders.models import Order


def check_conditions(request):
    user = request.user
    profile = user.profile

    if not user.is_authenticated:
        raise ValueError('You are not authenticated')

    if not profile.user_type == Profile.USER_TYPE_DRIVER:
        raise ValueError('You must have driver profile')

    if not profile.driver_is_free():
        raise ValueError('You must be free')


class NewOrders(views.View):
    def get(self, request):
        try:
            check_conditions(request)
        except ValueError as err:
            return HttpResponse(status=403, content=str(err))

        orders = Order.objects.filter(user_driver=None).order_by('created_at')

        orders_to_display = []
        for order in orders:
            orders_to_display.append(
                {
                    "id": order.id,
                    "client": order.user_client.username,
                    "created_at": order.created_at,
                    "price": order.price,
                }
            )

        return JsonResponse(dict(
            orders=orders_to_display
        ))


class AssignToOrders(views.View):
    def get(self, request, id):
        try:
            check_conditions(request)
        except ValueError as err:
            return HttpResponse(status=403, content=str(err))

        try:
            order = Order.objects.get(id=id, user_driver=None)
        except Order.DoesNotExist as err:
            return HttpResponse(status=404, content=str(err))

        order.user_driver = request.user
        order.save()

        return JsonResponse(dict(
            client=order.user_client.username,
            client_phone_number=order.user_client.profile.phone_number,
            created_at=order.created_at,
            price=order.price
        ))
