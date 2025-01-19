import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.io.IOException;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args)throws IOException {
       Scanner sc = new Scanner(System.in);
       int n = sc.nextInt();
       int res = 0;
       if (n >= 4) {
        
        res = (n * (n - 1) * (n - 2) * (n - 3)) / 24;
    }
    System.out.println(res);
    }    
}