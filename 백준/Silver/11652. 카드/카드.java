
import java.util.TreeMap;
import java.util.Scanner;
public class Main {

     public static void main(String[] args) {
          Scanner sc = new Scanner(System.in);
          int n = sc.nextInt();
          TreeMap<Long, Integer> cardCnt = new TreeMap<>();

          for(int i=0;i<n;i++){
               long card = sc.nextLong();
               cardCnt.put(card, cardCnt.getOrDefault(card, 0)+1);
          }
          long mostF = 0;
          int maxCnt = 0;
          for (long card: cardCnt.keySet()){
               int cnt = cardCnt.get(card);
               if(cnt>maxCnt){
                    mostF = card;
                    maxCnt = cnt;
               }
          }
     System.out.println(mostF);
     sc.close();
     }
     
}