import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int [] score = new int[8];
        int [] temp = new int[5];
        int ans = 0;
        for(int i=0;i<8;i++){
            score[i] = sc.nextInt();
        }

        for(int i=0;i<5;i++){
            int maxIndex = 0;
            for(int j=1;j<8;j++){
                if (score[j]>score[maxIndex]){
                    maxIndex = j;
                }
            }
            ans += score[maxIndex];
            temp[i] = maxIndex+1 ;
            score[maxIndex] = -1;
        }
        Arrays.sort(temp);

        System.out.println(ans);
        for(int idx : temp){
            System.out.print(idx +" ");
        }
        
    }
}