import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String text = br.readLine().toUpperCase();
        
        int[] count = new int[26];
        int max = 0;
        char result = '?';

        for (int i = 0; i < text.length(); i++) {
            int index = text.charAt(i) - 'A';
            count[index]++;
            if (max < count[index]) {
                max = count[index];
                result = text.charAt(i);
            } else if (max == count[index]) {
                result = '?';
            }
        }

        System.out.println(result);
    }
}