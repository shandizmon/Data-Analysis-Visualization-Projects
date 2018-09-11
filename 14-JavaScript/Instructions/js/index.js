// Get a reference to the table body
var tbody = d3.select("tbody");


// Select the submit button
var submit = d3.select("#submit");

submit.on("click", function() {

  tbody.html("")
  // Prevent the page from refreshing
  
  d3.event.preventDefault();

  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#inlineFormInput");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");

  console.log(inputValue);

  var filteredData = dataSet.filter(incident => incident.datetime === inputValue);

  console.log(filteredData);
  // $("#ufo").empty();
  filteredData.forEach((ufoReport) => {
    var row = tbody.append("tr");
    Object.entries(ufoReport).forEach(([key, value]) => {
      var cell = tbody.append("td");
      cell.text(value);
    });
  });
});

  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#inlineFormInput");

  // Get the value property of the input element
  var inputValue = "1/1/2010";

  console.log(inputValue);

  var filteredData = dataSet.filter(incident => incident.datetime === inputValue);

  console.log(filteredData);
  // $("#ufo").empty();
  filteredData.forEach((ufoReport) => {
    var row = tbody.append("tr");
    Object.entries(ufoReport).forEach(([key, value]) => {
      var cell = tbody.append("td");
      cell.text(value);
    });
  });



