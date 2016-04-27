var line_chart = c3.generate({
    bindto: '#line-chart',
    axis: {
        x: {
            type: 'timeseries',
            tick: {
                fit: false,
                format: '%Y-%m-%d %H:%M:%S',
                count: 4
            }
        }
    },
    data: {
        x: 'x',
        columns: []
    }
});

var pie_chart = c3.generate({
    bindto: '#pie-chart',
    data: {
        columns: [],
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
                fit: false,
                format: '%Y-%m-%d %H:%M:%S',
                count: 4
            }
        },
        y: {show:false}
    },
    data: {
        x: 'x',
        columns: [],
        type: 'scatter',
        colors: {
            on: '#00ff00',
            off: '#ff0000',
        },
    },
    tooltip: {
        format: {
            value: function (value, ratio, id) {
                return '';
            }
        }
    }
});


function update_temperature_stream() {
    $.ajax({
        url: "/stream/temperature/?data_source="+$("#temperature-data-source").val(),
        success: function(result) {
            var data = result['data'].map(function(log) {
                return log.field1_data;
            });

            var timestamps = result['data'].map(function(log) {
                return log.timestamp * 1000;
            });

            line_chart.load({
                columns: [
                    ['x'].concat(timestamps),
                    ['temperature'].concat(data)
                ]
            });
        }
    });
}

update_temperature_stream();
var temperatureId = setInterval(update_temperature_stream, 60000);

function update_multi_data_stream() {
    $.ajax({
        url: "/stream/multi_data/?data_source="+$("#multi-data-source").val(),
        success: function(result) {
            pie_chart.load({
                columns: [
                    [result['data'].field1_name, result['data'].field1_data],
                    [result['data'].field2_name, result['data'].field2_data],
                    [result['data'].field3_name, result['data'].field3_data],
                    [result['data'].field4_name, result['data'].field4_data],
                    [result['data'].field5_name, result['data'].field5_data],
                ]
            });
        }
    });
}

update_multi_data_stream();
var multiDataId = setInterval(update_multi_data_stream, 60000);

function update_status_stream() {
    $.ajax({
        url: "/stream/status/?data_source="+$("#status-data-source").val(),
        success: function(result) {
            var timestamps = result['data'].map(function(log) {
                return log.timestamp * 1000;
            });

            var on = result['data'].map(function(log) {
                return log.field1_data == 1 ? 1 : null;
            });

            var off = result['data'].map(function(log) {
                return log.field1_data == 0 ? 1 : null;
            });

            dot_chart.load({
                columns: [
                    ['x'].concat(timestamps),
                    ['on'].concat(on),
                    ['off'].concat(off),
                ]
            })
        }
    });
}

update_status_stream();
var statusId = setInterval(update_status_stream, 60000);

// handle data source change events
$("#status-data-source").on("change", function() {
    update_status_stream();
    window.clearInterval(statusId);
    statusId = setInterval(update_status_stream, 60000);
});

$("#multi-data-source").on("change", function() {
    update_multi_data_stream();
    window.clearInterval(multiDataId);
    multiDataId = setInterval(update_multi_data_stream, 60000);
});

$("#temperature-data-source").on("change", function() {
    update_temperature_stream();
    window.clearInterval(temperatureId);
    temperatureId = setInterval(update_temperature_stream, 60000);
});
