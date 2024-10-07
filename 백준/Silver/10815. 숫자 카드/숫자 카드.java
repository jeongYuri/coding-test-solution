import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Set<Integer> cardSet = new HashSet<>();
        for(int i=0;i<n;i++){
            cardSet.add(sc.nextInt());
        }
        int m = sc.nextInt();
        int[]res = new int[m];
        for(int i=0;i<m;i++){
            int card = sc.nextInt();
            if(cardSet.contains(card)){
                res[i] = 1;
            }else{
                res[i]= 0;
            }
        }
        for(int result : res){
            System.out.print(result + " ");
        }
        
    }
}