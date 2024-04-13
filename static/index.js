function display_results(data) {
    $("#result-list").empty();

    $.each(data, function (index, item) { 
        
        var result = $("<div class='row result-item'></div>")

        var col1 = $("<div class='col-md-2'></div>")
        col1.html(index + 1)
        result.append(col1)

        var col2 = $("<div class='col-md-3'></div>")
        var weapon_image = $("<img src=" + item["img"] + " alt='weapon image'>")
        col2.append(weapon_image)
        result.append(col2)

        var col3 = $("<div class='col-md-6'></div>")
        var name = $("<a href='/view/" + item["id"] + "'>" + item["name"] + "<\a>")
        col3.append(name)
        result.append(col3)

        var col4 = $("<div class='col-md-1'></div>")
        var delete_btn = $("<button class='btn btn-danger'>X</button>");
        delete_btn.prop("id", index)
        col4.append(delete_btn)
        result.append(col4)
        
        $("#result-list").append(result)
    });

    $(".btn-danger").click(function () { 
        var index = $(this).attr("id")
        var id = data[index]["id"]
        var send = {
            "id": id
        }
        
        
        $.ajax({
            type: "POST",
            url: "/delete",
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data: JSON.stringify(send),
            success: function (response) {
                data.splice(index, 1)
                $.each(data, function (i, item) { 
                    if (item["id"] > index) {
                        item["id"] -= 1
                    }
                });
                
                display_results(data)
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        });
    
    });

}

function check_input(input) {
    var valid = true
    if (input == "") {
        var warning = $("<div class='warning'>Please fill search keyword</div>")
        $("#warning").append(warning)
        valid = false
    } else if (input.replace(/\s+/g, "").length == 0) {
        var warning = $("<div class='warning'>Invalid spaces</div>")
        $("#warning").append(warning)
        valid = false
    }
    return valid
}

$(document).ready(function () {
    var indices = [7, 3, 5]; // Indices of items you want to concatenate from data array
    var filteredData = [];

    // Process data for specified indices
    $.each(indices, function(index, i) {
        filteredData.push(data[i]);
    });

    // Display the filtered data
    display_results(filteredData);
    
    // display_results(data)
    $("#searchbox").autocomplete({
        source: names
    });

    $(".search-btn").click(function () {
        
        var input = $("#searchbox").val()

        $("#warning").empty()
        valid = check_input(input)

        if (valid == true) {
            $("#result-list").empty();
            var search_key = {
                "search_key": input
            }

            // ajax call to search
            $.ajax({
                type: "POST",
                url: "search",
                dataType : "json",
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(search_key),
                success: function (response) {
                    var search_result = response["result"]

                    if (search_result.length == 0) {
                        $("#result-list").html("No results found.")
                    } else {
                        display_results(search_result)
                    }                
                },
                error: function(request, status, error){
                    console.log("Error");
                    console.log(request)
                    console.log(status)
                    console.log(error)
                }
            });
        }
        
    });
});