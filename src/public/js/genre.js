const data = {
    labels: Object.keys(countries),
    datasets: [{
        label: 'Country where this book is the most popular',
        backgroundColor: 'rgb(69, 103, 226)',
        borderColor: 'rgb(255, 99, 132)',
        data: Object.values(countries),
    }]
};

const config = {
    type: 'bar',
    data,
    options: {}
};

new Chart(document.getElementById('myChart'), config);


const headers = ["Country", "How many books"];
arr = Object.entries(list);
console.log(arr);
var table = $("<table class='table' />");
table[0].border = "1";

//Get the count of columns.
var columnCount = headers.length;

//Add the header row.
var row = $(table[0].insertRow(-1));
for (var i = 0; i < columnCount; i++) {
    var headerCell = $('<th scope="col" />');
    headerCell.html(headers[i]);
    // headerCell.html(`<a href=${headersLinks[i]}>${headers[i]}</a>`);
    row.append(headerCell);
}

//Add the data rows.
for (var i = 0; i < arr.length; i++) {
    row = $(table[0].insertRow(-1));
    var rowData = Object.values(arr[i]);

    for (var j = 0; j < columnCount; j++) {
        var cell = $("<td />");
        cell.html(rowData[j]);
        row.append(cell);
    }

    // var authorCell = $("<td />");
    // authorCell.html(`<a href='/authors/${rowData[j]}'>${rowData[j]}</a>`);
    // row.append(authorCell);    
}

var dvTable = $("#genreTable");
    dvTable.html("");
    dvTable.append(table);