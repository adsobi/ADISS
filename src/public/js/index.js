// tabelka z https://www.aspsnippets.com/Articles/Create-dynamic-HTML-Table-using-jQuery.aspx
const headers = ["Customer Id", "Name", "Country"];
const headersLinks = ["/page2", "/page3", "/page2"];

$(document).ready(()=>{

    let arr = [];
    $.ajax({
        url: ":api/getTable",
        success: (result)=>{
            arr = Object.values(result.table);
            var table = $("<table class='table' />");
            table[0].border = "1";

    //Get the count of columns.
    var columnCount = headers.length;

    //Add the header row.
    var row = $(table[0].insertRow(-1));
    for (var i = 0; i < columnCount; i++) {
        var headerCell = $('<th scope="col" />');
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


    // const data = {
    //     labels: Object.keys(genres),
    //     datasets: [{
    //         label: 'Most popular books genres',
    //         backgroundColor: 'rgb(69, 103, 226)',
    //         borderColor: 'rgb(255, 99, 132)',
    //         data: Object.values(genres),
    //     }]
    // };

    // const config = {
    //     type: 'bar',
    //     data,
    //     options: {}
    // };
    // new Chart(document.getElementById('myChart'), config);

    //genres was declared in index.html as value returned from flask
    const data = {
        labels: Object.keys(genres),
        datasets: [{
            label: 'Most popular books genres',
            backgroundColor: [
                'rgb(255, 99, 132)',
                'rgb(54, 162, 235)',
                'rgb(255, 205, 86)'
            ],
            data: Object.values(genres),
        }]
    };

    const config = {
        type: 'doughnut',
        data,
        options: {
            'onClick': function(evt, item){
                let indexOfElem = item[0].index;
                let nameOfElem = Object.keys(genres)[indexOfElem];
                alert(nameOfElem);
                window.location.href=(`/genres/${nameOfElem}`);
            }
        }
    };

    const canvas = document.getElementById('myDoughnutChart');
    new Chart(canvas, config);
})  
