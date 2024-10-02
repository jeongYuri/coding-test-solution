import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] data = new int[n];
        
        for (int i = 0; i < n; i++) {
            data[i] = sc.nextInt();
        }

        int[] sortdata = Arrays.copyOf(data, n);
        Arrays.sort(sortdata);
        
        int[] answer = new int[n];
    
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (sortdata[j] == data[i]) {
                    answer[i] = j;
                    sortdata[j] = -1; 
                    break;
                }
            }
        }

        for (int i = 0; i < n; i++) {
            System.out.print(answer[i] + " ");
        }
        
        sc.close();
    }
}
