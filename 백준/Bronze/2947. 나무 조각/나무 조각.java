import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] x = new int[5];
        
        for (int i = 0; i < 5; i++) {
            x[i] = sc.nextInt();
        }
        
        boolean sorted = false;
        
        while (!sorted) {
            sorted = true;
            for (int j = 0; j < 4; j++) {
                if (x[j] > x[j + 1]) {
                    int temp = x[j];
                    x[j] = x[j + 1];
                    x[j + 1] = temp;
                    
                    for (int i = 0; i < 5; i++) {
                        System.out.print(x[i] + " ");
                    }
                    
                    System.out.println();
                    sorted = false;
                }
            }
        }
    }
}