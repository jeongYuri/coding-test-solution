import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        String n = input[0];
        int b = Integer.parseInt(input[1]);
        int res = Integer.parseInt(n, b);
        System.out.println(res);
        }
    }
