
function prev_btn() {
    if (prev_id != -1) {
        $("#btns").append($("<form class='margin' action='/learn/" + prev_id + "' method='get' style='display: inline;'><button class='prev_btn' type='submit'>Previous</button></form>"))
    }
}

function curr_btn() {
    if (next_id != 6) {
        $("#btns").append($("<form class='margin' action='/learn/" + next_id + "' method='get' style='display: inline;'><button class='next_btn' type='submit'>Next</button></form>"))
    }
    else {
        $("#btns").append($("<form class='margin' action='/quiz_home' method='get' style='display: inline;'><button class='quiz_btn' type='submit'>Take Quiz</button></form>"))
    }
}

$(document).ready(function () {
    prev_btn()
    curr_btn()
});