// Check if the countdown date is stored in localStorage
var storedCountDownDate = localStorage.getItem("countDownDate");

// Set the date we're counting down to
var countDownDate = storedCountDownDate ? parseInt(storedCountDownDate, 10) : new Date("January 28, 2026 00:00:00").getTime();

// Update the countdown every 1 second
var x = setInterval(function() {

  // Get the current date and time
  var now = new Date().getTime();

  // Calculate the distance between now and the countdown date
  var distance = countDownDate - now;

  // Calculate days
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  
  // Display the countdown in the "countdown" div
  document.getElementById("countdown").innerHTML = days + " days remaining ";

  // If the countdown is over, show the message
  if (distance < 0) {
    clearInterval(x);
    document.getElementById("countdown").innerHTML = "EXPIRED";
  }
}, 1000);

// If not stored, set the initial countdown date in localStorage
if (!storedCountDownDate) {
  localStorage.setItem("countDownDate", countDownDate);
}
