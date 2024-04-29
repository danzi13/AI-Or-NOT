function submit_answer(id, answer) {
    user_answers[id].answer = answer
    $.ajax({
        url: "/update_userans",
        method: "POST",
        contentType: "application/json",
        data: JSON.stringify({ user_answers: user_answers }),
        error: function(xhr, status, error) {
            // Handle error response from the server
            console.error("Error updating variable on the server:", error);
        }
    });
}

function check_answer(selectedOption){
    console.log(selectedOption)
    if (selectedOption === undefined){
        if (document.getElementById("no_ans") != null) {
            document.getElementById("no_ans").remove();
        }
        $("#btn_row").append("<div id='no_ans' class='wrong_ans margin'>Please select an answer.</div>")
        return
    }
    submit_answer(item["id"], selectedOption)
    if (correct_answers[item["id"]]["answer"] == selectedOption) {
        document.getElementById("submitButton").remove();
        $("#btn_row").append("<button class='next_btn margin' type='submit'>Next</button>");
        $(".next_btn").click(function(e) {
            e.preventDefault();
            window.location.href = "/quiz/" + next_id;
        });
    } 
    else {
        document.getElementById("submitButton").remove();
        if (document.getElementById("no_ans") != null) {
            document.getElementById("no_ans").remove();
        }
        $("#btn_row").append("<div class='wrong_ans margin'>Incorrect Answer Selected: " + correct_answers[item["id"]]["reason"] + "<br>Correct Answer is " + correct_answers[item["id"]]["answer"] + "</div>").append("<div class=line-break>").append("<button class='next_btn margin' type='submit'>Next</button>");
        $(".next_btn").click(function(e) {
            e.preventDefault();
            window.location.href = "/quiz/" + next_id;
        });
    } 
    
}

$(document).ready(function(){
    // Add click event listener to submit button
    $("#submitButton").click(function(e){
        // Prevent the default form submission behavior
        e.preventDefault();
        
        // Get the value of the selected radio button
        var selectedOption = $(".choice:checked").val();
        
        // Display the value in the console (you can do anything else you want with it)
        check_answer(selectedOption)
    });
});