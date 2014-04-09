import java.util.ArrayList;

public class GameBoard {
	ArrayList<ArrayList<String>> board = new ArrayList<ArrayList<String>>();
	
	public void init(){
		for (int i = 0; i < 10 ; i++){
			ArrayList<String> rows = new ArrayList<String>();
			for (int j = 0; j < 10; j++){
				rows.add("-");
			}
			board.add(rows);
		}
		
		System.out.println(display());
	}
	
	public String display(){
		String s = "";
		for (int i = 0; i < 10 ; i++){
			String substring = "| ";
			for (int j = 0; j < 10; j++){
				substring = substring + board.get(i).get(j) + " ";
			}
			s = s + substring + "|\n";
		}
		s = s + "=======================\n| A B C D E F G H I J |";
		return s;
	}
}
