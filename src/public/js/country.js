
const headers = ["Book title", "Author"];

arr = Object.entries(list);
var table = $("<table class='table' />");
table[0].border = "1";

var columnCount = headers.length;

var row = $(table[0].insertRow(-1));
for (var i = 0; i < columnCount; i++) {
    var headerCell = $('<th scope="col" />');
    headerCell.html(headers[i]);
    row.append(headerCell);
}

for (var i = 1; i < arr.length; i++) {
    row = $(table[0].insertRow(-1));
    var rowData = Object.values(arr[i]);

    for (var j = 0; j < columnCount; j++) {
        var cell = $("<td />");
        cell.html(rowData[j]);
        row.append(cell);
    }
}

var dvTable = $("#booksTable");
    dvTable.html("");
    dvTable.append(table);