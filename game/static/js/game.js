$(document).ready(function(){
  $("#game_state_button").on("click", function() {
    $.ajax({
      url:"/game/data",
      dataType: 'json',
      type: 'GET',
      success: function(result) {
        $("#game_state_display").text("it works! game state is " + JSON.stringify(result.game_state));
    }});
  }); 
});
