import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;
import java.util.List;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder left = new StringBuilder(br.readLine());
        Stack<Character> right  = new Stack<>();
        int n = Integer.parseInt(br.readLine());

        for(int i=0;i<n;i++){
            String[] command = br.readLine().split(" ");
            char cmd = command[0].charAt(0);
            switch (cmd) {
                case 'L':
                    if(left.length() >0){
                        right.push(left.charAt(left.length()-1));
                        left.deleteCharAt(left.length()-1);
                    }
                    break;
                case 'D':
                    if(!right.isEmpty()){
                        left.append(right.pop());
                    }
                    break;
                case 'P':
                    left.append(command[1].charAt(0));
                    break;
                case 'B':
                    if(left.length()>0){
                        left.deleteCharAt(left.length()-1);
                    }
                    break;
            }
        }
        StringBuilder result = new StringBuilder(left);
        while (!right.isEmpty()) {
            result.append(right.pop());
        }

        System.out.println(result);
        }
        }
    

