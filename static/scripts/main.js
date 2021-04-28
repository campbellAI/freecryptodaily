var id_1 = null;
var id_2 = null;
var id_3 = null;

function deal1() {
  var elem1 = document.getElementById("hole_card1"); 
  var pos_1x = 26;
  var pos_1y = 257;
  clearInterval(id_1);
  id_1 = setInterval(frame1, 10);
  function frame1() {
    if (pos_1y == 450) {
      clearInterval(id_1);
    } else {
      pos_1x = pos_1x + 2; 
      pos_1y++;
      elem1.style.left = pos_1x + 'px'; 
      elem1.style.top = pos_1y + 'px'; 
    }
}}

function deal2() {
  var elem2 = document.getElementById("hole_card2"); 
  var pos_2x = 26;
  var pos_2y = 257;
  clearInterval(id_2);
  id_2 = setInterval(frame2, 10);
  function frame2() {
    if (pos_2y >= 450) {
      clearInterval(id_2);
    } else {
      pos_2x = pos_2x + 3;
      pos_2y++;
      elem2.style.left = pos_2x + 'px'; 
      elem2.style.top = pos_2y + 'px'; 
    }
}}

function deal3() {
  var elem3 = document.getElementById("hole_card3"); 
  var pos_3x = 26;
  var pos_3y = 257;
  clearInterval(id_3);
  id_3 = setInterval(frame3, 10);
  function frame3() {
    if (pos_3y == 450) {
      clearInterval(id_3);
    } else {
      pos_3x = pos_3x + 4;
      pos_3y++; 
      elem3.style.left = pos_3x + 'px'; 
      elem3.style.top = pos_3y + 'px'; 
    }
}}

function deal() {
  deal1();
  deal2();
  deal3();
  document.getElementById("deal-btn").style.display = "none";
}

function flip_hole_card1() {
  setTimeout(function () {
    document.getElementsByClassName("card1-inner")[0].style.transform = "rotateY(180deg)"
  }, 2300)
}

function flip_hole_card2() {
  setTimeout(function () {
    document.getElementsByClassName("card2-inner")[0].style.transform = "rotateY(180deg)"
  }, 2500)
}

function flip_hole_card3() {
  setTimeout(function () {
    document.getElementsByClassName("card3-inner")[0].style.transform = "rotateY(180deg)"
  }, 2700)
}

