// problem: https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=229&page=show_problem&problem=3098

import java.util.*;

class Main {
    public static void main(String args[]) {
        int N;
        int currentCase = 1;
		String inputDate;
        Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
        while (currentCase <= N){

			inputDate = sc.next();
            int month = Integer.parseInt(inputDate.substring(0,2));
            int day = Integer.parseInt(inputDate.substring(2,4));
            int year = Integer.parseInt(inputDate.substring(4,8));
			GregorianCalendar date = new GregorianCalendar(year , month - 1, day);
			date.add(Calendar.DATE, 40*7);

            month = date.get(Calendar.MONTH);
            day = date.get(Calendar.DATE);
            year = date.get(Calendar.YEAR);
            String sign = "";


            if (month == 0) {
                sign = day < 21 ? "capricorn" : "aquarius";
            } else if (month == 1) {
                sign = day < 20 ? "aquarius" : "pisces";
            } else if (month == 2) {
                sign = day < 21 ? "pisces" : "aries";
            } else if (month == 3) {
                sign = day < 21 ? "aries" : "taurus";
            } else if (month == 4) {
                sign = day < 22 ? "taurus" : "gemini";
            } else if (month == 5) {
                sign = day < 22 ? "gemini" : "cancer";
            } else if (month == 6) {
                sign = day < 22 ? "cancer" : "leo";
            } else if (month == 7) {
                sign = day < 23 ? "leo" : "virgo";
            } else if (month == 8) {
                sign = day < 22 ? "virgo" : "libra";
            } else if (month == 9) {
                sign = day < 22 ? "libra" : "scorpio";
            } else if (month == 10) {
                sign = day < 24 ? "scorpio" : "sagittarius";
            } else if (month == 11) {
                sign = day < 24 ? "sagittarius" : "capricorn";
            }

            String newMonth = month + 1 < 10 ? "0" + (month + 1) : Integer.toString(month + 1);
            String newDay = day < 10 ? "0" + day : Integer.toString(day);

			System.out.println(Integer.toString(currentCase) + " " + newMonth + "/" + newDay + "/" + year + " " + sign);
            currentCase += 1;
        }
    }
}