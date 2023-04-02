// import * from "./"

let selectSeatsList = []

function showSeats(seatsDictionary) {
    selectSeatsList = []
    obj = {'row': ['A', 'B'], 'column': ['1', '3'], 'seats': {'A-1': 'A', 'A-2': 'A', 'A-3': 'A', 'B-1': 'A', 'B-2': 'B', 'B-3': 'B'}}
    var seats = document.getElementById("seats");
    ele = ""
    cssClass = ""
    for (row in obj.row) {
       
        ele += "<div class=display-flex>"
    for (let i = 0; i < parseInt(obj.column[1]); i++) {
        // if(obj.seats)
        // cssClass=
        let seat = obj.row[row] + "-"+ (i+1)
        // console.log('seat') 
        // console.log(seat) 
        if(obj.seats[seat] == 'A') {
            ele += "<div class='seat-rows seat-available' onclick='selectSeats(" + row+","+(i+1) + ")'>" +
            "<i class='fa-solid fa-couch'></i></div>"
        } else {
            ele += "<div class='seat-rows seat-booked '><i class='fa-solid fa-couch'></i></div>"
        }
        // console.log(obj.seats[seat] == 'A') 
        
     }
     ele+="</div><br>"
    }

    seats.innerHTML = ele
}

function selectSeats(selectedRow, selectedColumn) {
    selectSeatsList.push( String.fromCharCode('A'.charCodeAt() + selectedRow) +"-"+selectedColumn)
    console.log(selectSeatsList)
}
