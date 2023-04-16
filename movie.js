const selectSeatsList = new Set();
const prefix = 'http://127.0.0.1:8080'
let bookingIdForCustomer = ''
let selectedTheater = ''
let selectedMovie = ''
let selectedSeatsCustomer = ''

// Took this from https://www.w3schools.com/howto/howto_js_tabs.asp 
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

//   Display seated on ui
function showSeats(theaterId,movieId) {
    fetch(prefix+'/showSeats/'+theaterId+'/'+movieId, {
        method: 'GET',
       
    }).then(response => response.json())
    .then((data) => {
        selectSeatsList.clear()
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
        for(i=obj.row[0].charCodeAt(); i<= obj.row[1].charCodeAt(); i++) {
            rowList.push(String.fromCharCode(i))
        }
        for (row in rowList) {
            ele += "<div class=display-flex>"
        for (let i = 0; i < parseInt(obj.column[1]); i++) {
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
         }
         ele+="</div><br>"
        }
        seats.innerHTML = ele
}).catch( err => {
    alert('unable to fetch seats details')
  }) 
}

// select seats for user
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

// display selected seats for user
function showselectedseats(){
    var selectedSeats = document.getElementById("selected-seats");
    const myIterator = selectSeatsList.values();
    let selectedSeatString = "";
    for (const entry of myIterator) {
        selectedSeatString += entry;
        selectedSeatString += ",";
    }
    selectedSeatsCustomer = selectedSeatString
    ele = "<div class='display-flex cursor-pointer'> Selected Seats: &nbsp;"+selectedSeatString+"</div>"
    selectedSeats.innerHTML = ele
}

// populate area in dropdown
function showAreaDropdownItems() {
    var arealist = document.getElementById("area-list");
    ele =''
    fetch(prefix+'/getAreaList/', {
        method: 'GET',
    }).then(response => response.json())
    .then((data) => {
        for (row in data.rows) {
            r = data.rows[row]
            ele+=" <div class='cursor-pointer' onclick='selectArea("+ r[0]+")'>"+ r[0]+","+ r[1]+"</div>"
        }
        arealist.innerHTML = ele  
}).catch( err => {
    alert('unable to fetch area details')
  })
}

// select area from dropdown
function selectArea(areaCode) {
var theaterConatiner = document.getElementById("display-theater");
    theaterConatiner.style.display = 'block'
    showTheaters(areaCode)
}

// select theater on ui
function showTheaters(area) {
    ele =''
    var arealist = document.getElementById("theater-list");
    fetch(prefix+'/getTheratersList/'+area, {
        method: 'GET',
    }).then(response => response.json())
    .then((data) => {
        for (row in data.rows) {
            r = data.rows[row]
            ele+=" <div class='cursor-pointer' onclick='selectTheater("+ r[1]+")'>"+ r[0]+","+ r[1]+"</div>"
        }
        arealist.innerHTML = ele  
}).catch( err => {
    alert('unable to fetch theater details')
  })  
}

// select theater from the list
function selectTheater(theaterId) {
    selectedTheater = theaterId
    var movieConatiner = document.getElementById("display-movie");
    var movieListContainer = document.getElementById("movie-list");
    var ele =''
    movieConatiner.style.display = 'block'
    fetch(prefix+'/getMovieList/'+theaterId, {
        method: 'GET',
    }).then(response => response.json())
    .then((data) => {
        for (row in data.rows) {
            r = data.rows[row]
            ele+=" <div class='cursor-pointer' onclick='selectMovie("+ r[1]+","+r[2]+")'>"+ r[2]+","+ r[3]+"</div>"
        }
        movieListContainer.innerHTML = ele  
}).catch( err => {
    alert('unable to fetch movie details')
  })
}

// select movie from the list
function selectMovie(theaterId, movieId ) {
    selectedMovie = movieId
    var theaterSeatConatiner = document.getElementById("seat-selection-cotainer");
    theaterSeatConatiner.style.display = 'block'
    showSeats(theaterId, movieId)
}

// book tickets for user
function bookTickets( ) {
    customerName =document.forms["bookingFrom"]["booking-customer-name"].value;
    customerAge =document.forms["bookingFrom"]["age"].value;
    fetch(prefix+'/bookTickets/'+customerName+'/'+customerAge+'/'+selectedTheater+'/'+selectedMovie+'/'+selectedSeatsCustomer, {
        method: 'GET',
    }).then(response => response.json())
    .then((data) => {
        if(data.rows.length > 0){
            var bookedTicketCotainer = document.getElementById("booked-ticket-cotainer");
            bookedTicketCotainer.style.display = 'block'
            showBookedSeats(data.rows[0][0])
        } else {
            console.log(data.msg)
        }
}).catch( err => {
    alert('unable to book your  details')
  })
}

//show book tickets for user
function showBookedSeats(bookingIdForCustomer) {
    console.log('get tickets')
    console.log(bookingIdForCustomer)
    ele =''
        fetch(prefix+'/getTicket/'+bookingIdForCustomer, {
            method: 'GET',
        }).then(response => response.json())
        .then((data) => {
            console.log(data)
            var getTicketCotainer = document.getElementById("booked-ticket-content");
            getTicketCotainer.style.display = 'block'
                customerName= data.rows[0][3]
                theaterName = data.rows[0][1]
                movieName = data.rows[0][4]
                movieTime = data.rows[0][5]
                seats= data.rows[0][6]
                
                console.log(getTicketCotainer)
                ele =''
                ele += "<div class='' id='customer-name' > Customer Name: &nbsp;"+ customerName+"</div>"
                ele += "<div class='' id='theater-name' >Theater Name: &nbsp;"+ theaterName+"</div>"
                ele += "<div class='' id='movie-name' >Movie Name: &nbsp;"+ movieName+"</div>"
                ele += "<div class='' id='movie-time'>Show Timing: &nbsp;"+ movieTime+"</div>"
                ele += "<div class='' id='seat-selected'>Selected Seats: &nbsp;"+ seats+"</div>"
                getTicketCotainer.innerHTML = ele
    }).catch( err => {
        alert('unable to fetch details')
      })

}


//get bookings for customer
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
            for (var i in  data.rows) {
                b = data.rows[i]
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
            if(data.rows.length ==0) {
                alert('No details found')
            }
    }).catch( err => {
        alert('error fetching details')
      })
    } 

//select bookings for customer
    function selectBookingForUser(bookingId) {
            var cancelbooking = document.getElementById("cancel-booking");
            cancelbooking.style.display = 'block'
            var modifyuserbooking = document.getElementById("modify-booking");
            modifyuserbooking.style.display = 'block'
        bookingIdForCustomer =  bookingId
    }


//cancel bookings for customer
    function cancelBookingForUser() {
        fetch(prefix+'/cancelTickets/'+bookingIdForCustomer, {
            method: 'GET',
        })
            .then(response => {
            alert('Your booking has been cancelled')
        }).catch( err => {
            alert('error cancelling your bookings')
          })
    }
    function showModifyBooking(){
        var modifyBookingForm = document.getElementById("modifyBookingForm");
        modifyBookingForm.style.display = 'block'
    }

    //modify bookings for customer
    function modifyBookingForUser(){
        var newCustomerName =  document.forms["CancelBookingFrom"]["new-name"].value;
        fetch(prefix+'/updateTickets/'+bookingIdForCustomer+'/'+newCustomerName, {
            method: 'GET',
        }).then(response => {
            alert('Your booking has been modified')
        }).catch( err => {
            alert('error modifying your bookings')
          })
    }





