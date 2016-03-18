var dates = [
    '2013-01-01', '2013-01-02', '2013-01-03',
    '2013-01-04', '2013-01-05', '2013-01-06',
    '2013-01-07', '2013-01-08', '2013-01-09',
    '2013-01-10', '2013-01-11', '2013-01-12',
    '2013-01-13', '2013-01-14', '2013-01-15',
    '2013-01-16', '2013-01-17', '2013-01-18',
    '2013-01-19', '2013-01-20', '2013-01-21',
    '2013-01-22', '2013-01-23', '2013-01-24',
    '2013-01-25', '2013-01-26', '2013-01-27',
    '2013-01-28', '2013-01-29', '2013-01-30',]

var line_chart = c3.generate({
    bindto: '#line-chart',
    axis: {
        x: {
            type: 'timeseries',
            tick: {
                format: '%Y-%m-%d'
            }
        }
    },
    data: {
        x: 'x',
        columns: [
            ['x'].concat(dates),
            ['temperature', 30,34,29,31,27,15,21,22,18,17,10,11,12,20,8,7,1,17,29,35,38,28,20,10,20,25,35,28,29,30],
        ]
    }
});

var pie_chart = c3.generate({
    bindto: '#pie-chart',
    data: {
        columns: [
            ['label1', 30],
            ['label2', 120],
            ['label3', 20],
            ['label4', 50],
            ['label5', 10],
        ],
        type : 'pie',
    }
});

var dot_chart = c3.generate({
    size: {
        height: 150
    },
    bindto: '#dot-chart',
    axis: {
        x: {
            type: 'timeseries',
            tick: {
                format: '%Y-%m-%d'
            }
        },
        y: {show:false}
    },
    data: {
        x: 'x',
        columns: [
            ['x'].concat(dates),
            ["on", 1, 1, null, null, 1, 1, null, null, 1, 1, 1, null, 1, 1, null, 1],
            ["off", null, null, 1, 1, null, null, 1, 1, null, null, null, 1, null, null, 1, null],
        ],
        type: 'scatter',
        colors: {
            on: '#00ff00',
            off: '#ff0000',
        },
    }
});
