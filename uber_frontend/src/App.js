import React from 'react';
import './App.css';

// Board
// Cell
// Status Bar - user turns
// Circle and Cross and Empty

function Cell(props) {
    const {data} = props;
    return <div style={{margin: 5, borderRight: "1px solid #000", minWidth: 50, display: "inline"}}>{data}</div>
}

function Row(props) {
    const {cells} = props;

    const render_cells = cells.map(cell => <Cell data={cell}/>)
    return (
        <div style={{borderBottom: "1px solid black"}}>
            {render_cells}
        </div>
    )
}

function Board(props) {
    const {n} = props;

    const generate_data = (n) => {
        let data = [];
        for (let i = 0; i < n; i++) {
            data[i] = [];
            for (let j = 0; j < n; j++) {
                data[i][j] = `${i}x${j}`;
            }
        }
        return data;
    };

    const render_rows = (data) => {
        return data.map(cells => <Row style={{background: "red"}} cells={cells}/>)
    };

    const data = generate_data(n);
    console.log(data);
    const rows = render_rows(data);

    return (
        <div style={{
            background: "#EEE",
            margin: 100
        }}>
            {rows}
        </div>
    )

}


function App() {


    return (
        <div>
            <Board n={5}/>
        </div>
    );
}

export default App;
