// tabelka z https://www.aspsnippets.com/Articles/Create-dynamic-HTML-Table-using-jQuery.aspx

$(document).ready(()=>{
    let chartColors = [];

    for (const key of Object.entries(genres)) {
        chartColors.push("#"+Math.floor(Math.random()*16777215).toString(16));
    }
    //genres was declared in index.html as value returned from flask
    const data = {
        labels: Object.keys(genres),
        datasets: [{
            label: 'Most popular books genres',
            backgroundColor: chartColors,
            data: Object.values(genres),
        }]
    };

    const config = {
        type: 'doughnut',
        data,
        options: {
            responsive: true,
            'onClick': function(evt, item){
                let indexOfElem = item[0].index;
                let nameOfElem = Object.keys(genres)[indexOfElem];
                window.location.href=(`/genre/${nameOfElem}`);
            },
            plugins: {
                legend: {
                    labels: {
                        font: {
                            size: 18
                        }
                    }
                }
            }     
        }
    };

    const canvas = document.getElementById('myDoughnutChart');
    new Chart(canvas, config);
})  
