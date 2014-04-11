var turn = 1;
var A = 9;
var B = 9;
var C = 9;
var D = 9;
var E = 9;
var F = 9;
var G = 9;
var H = 9;
var I = 9;
var J = 9;


function create(){
	var main = document.getElementById("main");
	var code = "";
	for (var i=0;i<100;i++){
		var k = i;
		if (i < 10){
			k = "0" + k;
		}
		code = code+"<div id='id"+k+"' class='block'></div>"		
	}
	main.innerHTML = code;
}

function add(col){
	var token;
	
	if (turn == 1){
		token = 'red';
	}
	else{
		token = 'black';
	}
	
	var row;

	switch (col){

		case 0:
  			row = A;
  			A -= 1;
  			break;
		case 1:
 			row = B;
  			B -= 1;
  			break;
		case 2:
  			row = C;
  			C -= 1;
  			break;
		case 3:
  			row = D;
  			D -= 1;
  			break;
		case 4:
  			row = E;
  			E -= 1;
  			break;
		case 5:
  			row = F;
  			F -= 1;
  			break;
		case 6:
  			row = G;
  			G -= 1;
  			break;
  		case 7:
  			row = H;
  			H -= 1;
  			break;
		case 8:
  			row = I;
  			I -= 1;
  			break;
		case 9:
  			row = J;
  			J -= 1;
  			break;
	}
	if(row > -1){
		document.getElementById("id"+row+col).style.backgroundColor = token;
		turn *= -1;
	}		
	//document.getElementById("id"+col).innerHTML = 'X'
	
}

function reset(){
	create();
	A = B = C = D = E = F = G = H = I = J = 9;
	turn = 1;
}
