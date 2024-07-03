// problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&category=0&problem=834

import java.util.*;

class Main {
    public static void main(String args[]) {
        int N;
		int d;
		int m;
		int y;
        Scanner sc= new Scanner(System.in);

        while (true){
			N = sc.nextInt();
			d = sc.nextInt();
			m = sc.nextInt();
			y = sc.nextInt();

            if (N == 0 && d == 0 && m == 0 && y == 0)
				break;
				
			GregorianCalendar date = new GregorianCalendar(y , m - 1, d);
			
			date.add(Calendar.DATE, N);
			
			System.out.println(date.get(Calendar.DATE) + " " + (date.get(Calendar.MONTH) + 1) + " " + date.get(Calendar.YEAR));
        }
    }
}