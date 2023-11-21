$(document).ready(function() {
   let offset  = {offset:"80%"}
$(".first-paragraph").waypoint(function(){
   $(".first-paragraph").addClass(
    "animate__animated animate__fadeInLeft"
   );
}, 
offset
);

$(".second-paragraph").waypoint(function(){
   $(".second-paragraph").addClass(
    "animate__animated animate__fadeInRightBig"
   );
}, 
offset
);

$(".third-paragraph").waypoint(function(){
   $(".third-paragraph").addClass(
    "animate__animated animate__fadeInUpBig"
   );
}, 
offset
);


$(".post-card").waypoint(function(){
   $(".post-card").addClass(
    "animate__animated animate__backInUp"
   );
}, 
offset
);

})