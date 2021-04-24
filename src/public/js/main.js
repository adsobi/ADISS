// tabelka z https://www.aspsnippets.com/Articles/Create-dynamic-HTML-Table-using-jQuery.aspx

const headers = ["Customer Id", "Name", "Country"];
const headersLinks = ["/page2", "/page3", "/page2"];
let arr = [];
$.ajax({
    url: ":api/getTable",
    success: (result)=>{
        arr = Object.values(result.table);
        var table = $("<table />");
        table[0].border = "1";

//Get the count of columns.
var columnCount = headers.length;

//Add the header row.
var row = $(table[0].insertRow(-1));
for (var i = 0; i < columnCount; i++) {
    var headerCell = $('<th/>');
    headerCell.html(`<a href=${headersLinks[i]}>${headers[i]}</a>`);
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
}

var dvTable = $("#dvTable");
    dvTable.html("");
    dvTable.append(table);
    },
    error: (result)=>{
        console.log(result);
    }
});

let chartData = {};
$.ajax({
    url: ":api/getChart",
    success: (result)=>{
        chartData=result.chart;
        const data = {
        labels: Object.keys(chartData),
        datasets: [{
            label: 'Most popular books genre',
            backgroundColor: 'rgb(69, 103, 226)',
            borderColor: 'rgb(255, 99, 132)',
            data: Object.values(chartData),
        }]
        };
        const config = {
        type: 'bar',
        data,
        options: {}
        };
        new Chart(
        document.getElementById('myChart'),
        config
        );
    },
    error: (result)=>{
        console.log(result);
    }
});


let doughnutChartData = {};
$.ajax({
    url: ":api/getDoughnutChart",
    success: (result)=>{
        doughnutChartData=result.chart;
        const data = {
        labels: Object.keys(doughnutChartData),
        datasets: [{
            label: 'Most popular books genre',
            backgroundColor: [
                'rgb(255, 99, 132)',
                'rgb(54, 162, 235)',
                'rgb(255, 205, 86)'
              ],
            data: Object.values(doughnutChartData),
        }]
        };
        const config = {
        type: 'doughnut',
        data,
        options: {}
        };
        new Chart(
        document.getElementById('myDoughnutChart'),
        config
        );
    },
    error: (result)=>{
        console.log(result);
    }
});