import java.io.*;
import java.util.*;
import java.util.regex.*;;
public class Main{
    public static void main(String[] args){
       Scanner sc = new Scanner(System.in);
       int n = sc.nextInt();
       int[] multi = new int[n];
       int con = 1;
       for(int i=0;i<n;i++){
            multi[i] = sc.nextInt();
            con += multi[i]-1;
       }
       System.out.println(con);

    }
}
