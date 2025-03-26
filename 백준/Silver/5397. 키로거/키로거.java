import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for(int i = 0;i<t;i++){
            String keylogger = br.readLine();
            Stack<Character> left_Stacks = new Stack<>();
            Stack<Character> right_Stacks = new Stack<>();

            for(char c: keylogger.toCharArray()){
                if(c=='-'){
                    if(!left_Stacks.isEmpty()){
                        left_Stacks.pop();
                    }
                }else if(c=='<'){
                    if(!left_Stacks.isEmpty()){
                        right_Stacks.push(left_Stacks.pop());
                    }
                }else if(c=='>'){
                    if(!right_Stacks.isEmpty()){
                        left_Stacks.push(right_Stacks.pop());
                    }
                }else{
                    left_Stacks.push(c);
                }
            }
            StringBuilder sb = new StringBuilder();
            while (!left_Stacks.isEmpty()) {
                sb.append(left_Stacks.pop());
            }
            sb.reverse();  

            while (!right_Stacks.isEmpty()) {
                sb.append(right_Stacks.pop());
            }

            System.out.println(sb.toString());
        }
    }     
}
    
