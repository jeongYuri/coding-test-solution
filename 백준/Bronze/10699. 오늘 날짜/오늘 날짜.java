import java.io.*;
import java.util.*;
import java.time.*;
public class Main{
    static int[] arr = new int[4];
	static int max = -1;
	static String love = "LOVE";
	static String win = "";
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		LocalDate now = LocalDate.now();//현재 날짜 구하기
		LocalDate seoul = LocalDate.now(ZoneId.of("Asia/Seoul"));

		System.out.println(seoul);
		
    }
       

    
}