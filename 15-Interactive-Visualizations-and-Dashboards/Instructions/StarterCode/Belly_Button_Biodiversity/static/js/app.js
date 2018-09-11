function buildMetadata(sample) {
  // @TODO: Complete the following function that builds the metadata panel
    var selector = document.getElementById('selDataset');
    var url = "/names";
   // Use `d3.json` to fetch the metadata for a sample
    // Use d3 to select the panel with id of `#sample-metadata` 
    Plotly.d3.json(url, function(error, response) {
        if (error) return console.warn(error);
        var data = response;
        data.map(function(sample){
            var option = document.createElement('option')
            option.text = sample
            option.value = sample
            selector.appendChild(option)
        });
    });
};

    // Use `.html("") to clear any existing metadata
    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.
getSampleNames();

function optionChanged(sample){
  updatePie(sample);
  updateBubble(sample);
  updateMetadata(sample);
};

function updatePie(sample){
  var sampleURL ='/samples/${sample}'
  Plotly.d3.json(sampleURL,funtion(error,response)
      if (error) return console,log(error);
      var labels =[]
      var values=[]
      var hovers = []
      for i=0;i<10;i++){
          var label = response[0].otu_ids[i]
          labels.push(label);
          var value = response[1].sample_values[i]
          values.push(value);
          var label = response[0].otu_ids[i]
          labels.push(label);
      }
  )
}

    // BONUS: Build the Gauge Chart
    // buildGauge(data.WFREQ);

function buildCharts(sample) {

  // @TODO: Use `d3.json` to fetch the sample data for the plots

    // @TODO: Build a Bubble Chart using the sample data

    // @TODO: Build a Pie Chart
    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).
}

function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
