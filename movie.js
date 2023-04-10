// import * from "./"

const selectSeatsList = new Set();
const prefix = 'http://127.0.0.1:8080'
// var selectedSeatString = "sk"



function openTab(evt, TabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(TabName).style.display = "block";
    evt.currentTarget.className += " active";
  }

function showSeats(theaterId,movieId) {
    fetch(prefix+'/showSeats/'+theaterId+'/'+movieId, {
        method: 'GET',
       
    })
        .then(response => {response
        console.log('get showSeats list')
        console.log(response)
    })

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

    fetch(prefix+'/getAreaList/', {
        method: 'GET',
       
    })
        .then(response => {response
        console.log('get area list')
        console.log(response)
    })
    var arealist = document.getElementById("area-list");
    ele =''
    for (row in areaTableDetails) {
        r = areaTableDetails[row]
        ele+=" <div class='cursor-pointer' onclick='selectArea("+ r[0]+")'>"+ r[0]+","+ r[1]+"</div>"
    // <div onclick='selectSeats('areaId')'>Link 1</div>
    // var selectedSeats = document.getElementById("area-code-drowpdown"); 
    }
    arealist.innerHTML = ele
}

function selectArea(areaCode) {
    //get all theaters sort by area code --> theratersTableDetails

    var theaterConatiner = document.getElementById("display-theater");
    theaterConatiner.style.display = 'block'
    showTheaters(areaCode)
}


function showTheaters(area) {
    let theratersTableDetails = [['101', 'cine world', '102', 'A,B', '1,5'],[ '102', 'movies world', '102', 'A,B', '1,7']]
    fetch(prefix+'/getTheratersList/'+area, {
        method: 'GET',
       
    })
        .then(response => {response
        console.log('get theater list')
        console.log(response)
    })
    var arealist = document.getElementById("theater-list");
    ele =''
    for (row in theratersTableDetails) {
        r = theratersTableDetails[row]
        ele+=" <div class='cursor-pointer' onclick='selectTheater("+ r[0]+")'>"+ r[0]+","+ r[1]+"</div>"
    }
    arealist.innerHTML = ele
}


function selectTheater( ) {
    var theaterSeatConatiner = document.getElementById("seat-selection-cotainer");
    theaterSeatConatiner.style.display = 'block'
    showSeats({})
}


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

    // fetch(prefix+'/showBookedSeats/'+customerName+'/'+theaterName+'/'+movieName+'/'+, {
    //     method: 'GET',
    //     headers: {
    //         'Accept': 'application/json',
    //     },
    // })
    //     .then(response => {response.json()
    //     console.log(response)
    // })

    var theaterSeatConatiner = document.getElementById("booked-ticket-content");

    ele += "<div class='' id='customer-name'>"+ customerName+"</div>"
    ele += "<div class='' id='theater-name'>"+ theaterName+"</div>"
    ele += "<div class='' id='movie-name'>"+ movieName+"</div>"
    ele += "<div class='' id='movie-time'>"+ movieTime+"</div>"
    ele += "<div class='' id='seat-selected'>"+ seats+"</div>"
    theaterSeatConatiner.innerHTML = ele
}

function getBookingsForCustomer(){
    var name =  document.forms["CancelBookingFrom"]["name"].value;
    fetch(prefix+'/getBookingsForCustomer/'+name, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
        },
    })
        .then(response => {
        console.log(response.json())
    })
    } 