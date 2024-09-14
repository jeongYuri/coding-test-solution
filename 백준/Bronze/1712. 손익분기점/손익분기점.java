import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt(); //고정비용
        int b = sc.nextInt(); //가변비용
        int c = sc.nextInt(); // 판매가격
        if (b>=c){
            System.out.println(-1);
        }else{
            System.out.println((a/(c-b))+1);
        }
        sc.close();
    }
}