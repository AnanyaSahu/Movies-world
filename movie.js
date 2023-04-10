// import * from "./"

const selectSeatsList = new Set();
const prefix = 'http://127.0.0.1:8080'
let bookingIdForCustomer = ''
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
       
    }).then(response => response.json())
    .then((data) => {
        selectSeatsList.clear()
        // obj = {'row': ['A', 'B'], 'column': ['1', '3'], 'seats': {'A-1': 'A', 'A-2': 'A', 'A-3': 'A', 'B-1': 'A', 'B-2': 'B', 'B-3': 'B'}}
        obj= data.rows
        var seats = document.getElementById("seats");
        ele = ""
        cssClass = ""
        ele += "<div class='display-flex cursor-pointer'>"
        for (let i = 0; i < parseInt(obj.column[1]); i++) {
            ele += "<div>"+( i+1)+"</div>"
        }
        ele+="</div>"
        rowList = []
        console.log(obj.row[0].charCodeAt())
        console.log(obj.row[1].charCodeAt())
        for(i=obj.row[0].charCodeAt(); i<= obj.row[1].charCodeAt(); i++) {
            rowList.push(String.fromCharCode(i))
        }
        console.log(rowList)
        // while (rowItem)
        for (row in rowList) {
        //    console.log(obj.row)
            ele += "<div class=display-flex>"
        for (let i = 0; i < parseInt(obj.column[1]); i++) {
            // if(obj.seats)
            // cssClass=
            
            if(i==0){
                ele += "<div>"+rowList[row]+"</div>"
            }
            let seat = rowList[row] + "-"+ (i+1)
           
            
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
})   


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
    fetch(prefix+'/getAreaList/', {
        method: 'GET',
    }).then(response => response.json())
    .then((data) => {
        console.log('areaarearaearae') 
        console.log(data.rows)  
        for (row in data.rows) {
            r = data.rows[row]
            ele+=" <div class='cursor-pointer' onclick='selectArea("+ r[0]+")'>"+ r[0]+","+ r[1]+"</div>"
        }
        arealist.innerHTML = ele  
})   
}

function selectArea(areaCode) {
    //get all theaters sort by area code --> theratersTableDetails

    var theaterConatiner = document.getElementById("display-theater");
    theaterConatiner.style.display = 'block'
    showTheaters(areaCode)
}


function showTheaters(area) {
    ele =''
    var arealist = document.getElementById("theater-list");
    fetch(prefix+'/getTheratersList/'+area, {
        method: 'GET',
    }).then(response => response.json())
    .then((data) => {
        console.log('get therater') 
        console.log(data.rows)  
        for (row in data.rows) {
            r = data.rows[row]
            ele+=" <div class='cursor-pointer' onclick='selectTheater("+ r[1]+")'>"+ r[0]+","+ r[1]+"</div>"
        }
        arealist.innerHTML = ele  
})   
}

function selectTheater(theaterId) {
    var movieConatiner = document.getElementById("display-movie");
    var movieListContainer = document.getElementById("movie-list");
    var ele =''
    movieConatiner.style.display = 'block'
    let movieTableDetails = [['101', '101','111','movie name', 'showtiming', 'duration', 11]]

    fetch(prefix+'/getMovieList/'+theaterId, {
        method: 'GET',
    }).then(response => response.json())
    .then((data) => {
        console.log('get movies') 
        console.log(data.rows)  
        for (row in data.rows) {
            r = data.rows[row]
            ele+=" <div class='cursor-pointer' onclick='selectMovie("+ r[1]+","+r[2]+")'>"+ r[2]+","+ r[3]+"</div>"
        }
        movieListContainer.innerHTML = ele  
}) 
}

function selectMovie(theaterId, movieId ) {
    var theaterSeatConatiner = document.getElementById("seat-selection-cotainer");
    theaterSeatConatiner.style.display = 'block'
    showSeats(theaterId, movieId)
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
    var userbooking = document.getElementById("user-booking");
    userbooking.style.display = 'block'
    ele =''
    fetch(prefix+'/getBookingsForCustomer/'+name, {
        method: 'GET',
        headers: {
            'Accept': 'application/json',
        },
    })
        .then(response => response.json())
        .then((data) => {
            console.log(data.rows)  
            for (var i in  data.rows) {
                b = data.rows[i]
                console.log(b)
                ele += "<div class='display-flex' onclick='selectBookingForUser("+b[0]+")'>"
                ele += "<div class='' id='customer-name'>"+ b[0]+"</div>;&nbsp;"
                ele += "<div class='' id='theater-name'>"+   b[1]+"</div>;&nbsp;"
                ele += "<div class='' id='movie-name'>"+  b[2]+"</div>;&nbsp;"
                ele += "<div class='' id='movie-time'>"+  b[3]+"</div>;&nbsp;"
                ele += "<div class='' id='seat-selected'>"+  b[4]+"</div>;&nbsp;"
                ele += "<div class='' id='movie-time'>"+  b[5]+"</div>;&nbsp;"
                ele += "<div class='' id='seat-selected'>"+  b[6]+"</div>;&nbsp;"
                ele += "<div class='' id='seat-selected'>"+  b[7]+"</div>"
                ele += "</div>"
                ele += "<br>"
            }
            userbooking.innerHTML = ele
            
            
    })
    } 

    function selectBookingForUser(bookingId) {
        // if(bookingIdForCustomer != '') {
            var cancelbooking = document.getElementById("cancel-booking");
            cancelbooking.style.display = 'block'
        // }

        bookingIdForCustomer =  bookingId

   
    }



    function cancelBookingForUser() {

        console.log(bookingIdForCustomer)

        fetch(prefix+'/cancelTickets/'+bookingIdForCustomer, {
            method: 'GET',
           
        })
            .then(response => {
            console.log('cancelBookingForUser')
            console.log(response)
        })
    }

    function modifyBookingForUser(){
        var newCustomerName =  document.forms["CancelBookingFrom"]["new-name"].value;
        console.log(bookingIdForCustomer)
        fetch(prefix+'/updateTickets/'+bookingIdForCustomer+'/'+newCustomerName, {
            method: 'GET',
           
        })
            .then(response => {
            console.log('modifyBookingForUser')
            console.log(response)
        })
    }



