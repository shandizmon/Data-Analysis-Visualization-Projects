// Get a reference to the table body
var tbody = d3.select("tbody");


// Select the submit button
var submit = d3.select("#submit");

submit.on("click", function() {

  // Prevent the page from refreshing
  
  d3.event.preventDefault();

  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#inlineFormInput");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");

  console.log(inputValue);

  var filteredData = dataSet.filter(incident => incident.datetime === inputValue);

  console.log(filteredData);
  $("#ufo").empty();
  filteredData.forEach((ufoReport) => {
    var row = tbody.append("tr");
    Object.entries(ufoReport).forEach(([key, value]) => {
      var cell = tbody.append("td");
      cell.text(value);
    });
  });
});

// BONUS: Refactor to use Arrow Functions!


// Console.log the weather data from data.js
// console.log(dataSet);

// // Step 1: Loop Through `data` and console.log each weather report object
// dataSet.forEach(function(weatherReport) {
//    console.log(weatherReport);
//  });

// // Step 2:  Use d3 to append one table row `tr` for each weather report object
// // Don't worry about adding cells or text yet, just try appending the `tr` elements.
// data.forEach(function(weatherReport) {
//   console.log(weatherReport);
//   var row = tbody.append("tr");

// });

// // Step 3:  Use `Object.entries` to console.log each weather report value
// data.forEach(function(weatherReport) {
//   console.log(weatherReport);
//   var row = tbody.append("tr");

//   Object.entries(weatherReport).forEach(function([key, value]) {
//     console.log(key, value);
//   });
// });

// // Step 4: Use d3 to append 1 cell per weather report value (weekday, date, high, low)
// data.forEach(function(weatherReport) {
//   console.log(weatherReport);
//   var row = tbody.append("tr");

//   Object.entries(weatherReport).forEach(function([key, value]) {
//     console.log(key, value);
//     // Append a cell to the row for each value
//     // in the weather report object
//     var cell = tbody.append("td");
//   });
// });

// // Step 5: Use d3 to update each cell's text with
// // weather report values (weekday, date, high, low)
// data.forEach(function(weatherReport) {
//   console.log(weatherReport);
//   var row = tbody.append("tr");
//   Object.entries(weatherReport).forEach(function([key, value]) {
//     console.log(key, value);
//     // Append a cell to the row for each value
//     // in the weather report object
//     var cell = tbody.append("td");
//     cell.text(value);
//   });
// });

