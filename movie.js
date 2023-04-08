// import * from "./"

const selectSeatsList = new Set();
// var selectedSeatString = "sk"

function showSeats(seatsDictionary) {
    selectSeatsList.clear()
    obj = {'row': ['A', 'B'], 'column': ['1', '3'], 'seats': {'A-1': 'A', 'A-2': 'A', 'A-3': 'A', 'B-1': 'A', 'B-2': 'B', 'B-3': 'B'}}
    var seats = document.getElementById("seats");
    ele = ""
    cssClass = ""
    ele += "<div class='display-flex cursor-pointer'>"
    for (let i = 0; i < parseInt(obj.column[1]); i++) {
        ele += "<div>"+( i+1)+"</div>"
    }
    ele+="</div>"
    for (row in obj.row) {
       
        ele += "<div class=display-flex>"
    for (let i = 0; i < parseInt(obj.column[1]); i++) {
        // if(obj.seats)
        // cssClass=
        
        if(i==0){
            ele += "<div>"+obj.row[row]+"</div>"
        }
        let seat = obj.row[row] + "-"+ (i+1)
        // console.log('seat') 
        // console.log(seat) 
        
        if(obj.seats[seat] == 'A') {
            ele += "<div id=' "+String(row).concat(i+1)+" ' class='seat-rows seat-available clicked-seat cursor-pointer' onclick='selectSeats(" + row+","+(i+1) + ")'>" +
            "<i class='fa-solid fa-couch'></i></div>"
        } else {
            ele += "<div id=' "+String(row).concat(i+1)+" 'class='seat-rows seat-booked'><i class='fa-solid fa-couch'></i></div>"
        }
        // console.log(obj.seats[seat] == 'A') 
        
     }
     ele+="</div><br>"
    }

    // <div>selected seats: </div>

    seats.innerHTML = ele
}

function selectSeats(selectedRow, selectedColumn) {
    let createSeatString =String.fromCharCode('A'.charCodeAt() + selectedRow) +"-"+selectedColumn
    if(selectSeatsList.has(createSeatString)){
        // remove
        selectSeatsList.delete(createSeatString)
    } else{
        selectSeatsList.add( createSeatString)
    }
    showselectedseats()
}

function showselectedseats(){
    var selectedSeats = document.getElementById("selected-seats");
    const myIterator = selectSeatsList.values();
    let selectedSeatString = "";
    for (const entry of myIterator) {
        selectedSeatString += entry;
        selectedSeatString += ",";
    }
    ele = "<div class='display-flex cursor-pointer'> Selected Seats: &nbsp;"+selectedSeatString+"</div>"
    selectedSeats.innerHTML = ele
}


function showAreaDropdownItems() {
    let areaTableDetails = [[ '101', 'Pranell Street', '100'],[ '102', 'Prince Street', '200']]
    var arealist = document.getElementById("area-list");
    ele =''
    for (row in areaTableDetails) {
        r = areaTableDetails[row]
        ele+=" <div class='cursor-pointer' onclick='selectArea("+ r[0]+")'>"+ r[1]+"</div>"
    // <div onclick='selectSeats('areaId')'>Link 1</div>
    // var selectedSeats = document.getElementById("area-code-drowpdown"); 
    }
    arealist.innerHTML = ele
}

function selectArea(areaCode) {
    //get all theaters sort by area code --> theratersTableDetails

    var theaterConatiner = document.getElementById("display-theater");
    theaterConatiner.style.display = 'block'
    showTheaters()
}


function showTheaters() {
    let theratersTableDetails = [['101', 'cine world', '102', 'A,B', '1,5'],[ '102', 'movies world', '102', 'A,B', '1,7']]
    var arealist = document.getElementById("theater-list");
    ele =''
    for (row in theratersTableDetails) {
        r = theratersTableDetails[row]
        ele+=" <div class='cursor-pointer' onclick='selectTheater("+ r[0]+")'>"+ r[1]+"</div>"
    }
    arealist.innerHTML = ele
}


function selectTheater( ) {
    var theaterSeatConatiner = document.getElementById("seat-selection-cotainer");
    theaterSeatConatiner.style.display = 'block'
}

/* <div class=" container-fluid row" id="customer-name"></div>
<div class=" container-fluid row" id="theater-name"></div>
<div class=" container-fluid row" id="movie-name"></div>
<div class=" container-fluid row" id="movie-time"></div>
<div class=" container-fluid row" id="seat-selected"></div> */

function bookTickets( ) {
    var bookedTicketCotainer = document.getElementById("booked-ticket-cotainer");
    bookedTicketCotainer.style.display = 'block'
    showBookedSeats()
}


function showBookedSeats( ) {
    customerName= 'C101'
    theaterName = 'Cine World'
    movieName = "nike air"
    movieTime = '1900'
    seats= 'A-1,A-2'
    ele =''
    var theaterSeatConatiner = document.getElementById("booked-ticket-content");

    ele += "<div class='' id='customer-name'>"+ customerName+"</div>"
    ele += "<div class='' id='theater-name'>"+ theaterName+"</div>"
    ele += "<div class='' id='movie-name'>"+ movieName+"</div>"
    ele += "<div class='' id='movie-time'>"+ movieTime+"</div>"
    ele += "<div class='' id='seat-selected'>"+ seats+"</div>"
    theaterSeatConatiner.innerHTML = ele
}