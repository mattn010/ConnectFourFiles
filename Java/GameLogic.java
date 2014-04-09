import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;


public class GameLogic {

	GameBoard gb = new GameBoard();
	Player p1 = new Player();
	Player p2 = new Player();
	int pTurn = 1;
	boolean endgame = false;
		
	public void Start(){
		gb.init();
		createPlayers();
		while(!endgame){
			turn();
			System.out.println(gb.display());
		}
	}
	
	private void turn() {
		
		Player p;
		if (pTurn == 1){
			p = p1;
		}
		else{
			p = p2;
		}
		System.out.println(p.name+" please enter a column: ");
		String col = "";
		BufferedReader br = new BufferedReader( new InputStreamReader(System.in));
		try {
			col = br.readLine();		
		} catch (IOException e) {
			e.printStackTrace();
		}
		add(col.toUpperCase(), p);	
		
	}

	private void add(String c, Player p) {
		int column = -1;
		switch (c){
			case("A"): column = 0;
				break;
			case("B"): column = 1;
			   break;
			case("C"): column = 2;
			   break;
			case("D"): column = 3;
			   break;
			case("E"): column = 4;
			   break;
			case("F"): column = 5;
			   break;
			case("G"): column = 6;
			   break;
			case("H"): column = 7;
			   break;
			case("I"): column = 8;
			   break;
			case("J"): column = 9;
			   break;
			default: column = -1;
		}
		
		System.out.println(column);
		if (column == -1){
			System.out.println("Please enter a valid column letter!");
		}
		else if (gb.board.get(0).get(column) != "-"){
			System.out.println("Column is full!");
		}
		else{
			int i = 9;
			while(i > -1){
				if (gb.board.get(i).get(column) == "-" ){
					ArrayList<String> a = gb.board.get(i);
					a.set(column, p.token);
					gb.board.set(i, a);
					pTurn *= -1;
					if(checkForWin(i, column, p)){
						endgame = true;
					}
					break;
				}
				else{
					i--;
				}
			}
		}
		
	}

	private boolean checkForWin(int r, int c, Player p) {
		if(checkW(r, p) || checkH(c, p) || checkD1(r, c, p) || checkD2(r, c, p)){
			return true;
		}
		return false;
	}
	
	private boolean checkW(int r, Player p){
		for (int i = 0; i < 7; i++){
			if (gb.board.get(r).get(i) == p.token &&
					gb.board.get(r).get(i+1) == p.token &&
					gb.board.get(r).get(i+2) == p.token &&
					gb.board.get(r).get(i+3) == p.token){
				System.out.println(p.name+" has won!");
				return true;				
			}
		}
		return false;
	}
	
	private boolean checkH(int c, Player p){
		for (int i = 0; i < 7; i++){
			if (gb.board.get(i).get(c) == p.token &&
					gb.board.get(i+1).get(c) == p.token &&
					gb.board.get(i+2).get(c) == p.token &&
					gb.board.get(i+3).get(c) == p.token){
				System.out.println(p.name+" has won!");
				return true;				
			}
		}
		return false;
	}
	
	private boolean checkD1(int r, int c, Player p){
		int r1 = r;
		int c1 = c;
		while(r1 < 9 && c1 > 0){
			r1 += 1;
			c1 -= 1;
		}
		if(r1 <= 2 || c1 >= 7){
			return false;
		}
		else{
			for (int i = r1; i > 2; i--){
				for (int j = c1; j < 7; j++){
					if (gb.board.get(i).get(j) == p.token &&
							gb.board.get(i-1).get(j+1) == p.token &&
							gb.board.get(i-2).get(j+2) == p.token &&
							gb.board.get(i-3).get(j+3) == p.token){
						System.out.println(p.name+" has won!");
						return true;
					}
				}
			}
		}
		
		return false;
	}
	
	private boolean checkD2(int r, int c, Player p){
		int r1 = r;
		int c1 = c;
		while(r1 > 0 && c1 > 0){
			r1 -= 1;
			c1 -= 1;
		}
		if(r1 >= 7 || c1 >= 7){
			return false;
		}
		else{
			for (int i = r1; i < 7; i++){
				for (int j = c1; j < 7; j++){
					if (gb.board.get(i).get(j) == p.token &&
							gb.board.get(i+1).get(j+1) == p.token &&
							gb.board.get(i+2).get(j+2) == p.token &&
							gb.board.get(i+3).get(j+3) == p.token){
						System.out.println(p.name+" has won!");
						return true;
					}
				}
			}
		}
		
		return false;
	}

	public void createPlayers(){
		p1.id = 1; p2.id = -1;
		p1.token = "X"; p2.token = "O";
		p1.name = "Player 1"; p2.name = "Player 2";
	}
	
}

class Player{
	String name = "";
	int id = 0;
	String token = "";
}