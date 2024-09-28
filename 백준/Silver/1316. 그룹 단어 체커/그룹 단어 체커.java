import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String [] words = new String[n];
        int cnt = 0;
        for(int i=0; i<n;i++){
            words[i] = sc.next();
        }
        for(String word : words){
            boolean is_group = true;
            for(int i=0;i<word.length()-1;i++){
                if (word.charAt(i) != word.charAt(i+1)){
                    if(word.indexOf(word.charAt(i+1),0)<i+1){
                        is_group = false;
                        break;
                    }
                }
            }
            if(is_group){
                cnt +=1;
            }
            
        }
        System.out.println(cnt);
        sc.close();
    }
}
