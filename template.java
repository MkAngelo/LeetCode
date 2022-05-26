import java.io.*;

public class Template {
	static final StdIn in = new StdIn();
	static final PrintWriter out = new PrintWriter(System.out);

	public static void main(String[] args){
		int t = in.nextInt();
		for(int i=1; i<=t; ++i){
			out.print("Case #" +i+": ");
			new Solver();
		}
		out.close();
	}

	static class Solver(){
		Solver() {
		}
	}
}