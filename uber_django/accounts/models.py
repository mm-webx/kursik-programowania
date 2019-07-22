from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Profile(models.Model):
    USER_TYPE_DRIVER = 1
    USER_TYPE_CLIENT = 2

    USER_TYPES_CHOICES = (
        (USER_TYPE_DRIVER, 'Driver'),
        (USER_TYPE_CLIENT, 'Client')
    )

    phone_number = models.TextField(max_length=12, null=False, default='000000000000')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    birth_date = models.DateField(null=False, blank=False)
    user_type = models.IntegerField(choices=USER_TYPES_CHOICES, null=False, default=USER_TYPE_CLIENT)

    def __str__(self):
        return f'User Profile {self.user.username} - {self.user_type}'

    def is_mature(self):
        if not self.birth_date:
            return False

        now = timezone.now().date()
        # TODO: fix it to check months and days also
        return now.year - self.birth_date.year >= 18
