import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine();
        String find_word = sc.nextLine();

        int cnt = 0;
        int idx = 0;
        while(idx<=word.length()-find_word.length()){
            if(word.substring(idx, idx+find_word.length()).equals(find_word)){
                cnt +=1;
                idx += find_word.length();
            }else{
                idx +=1;
            }
        }
        System.out.println(cnt);
    }
}