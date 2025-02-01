import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Map<String, Integer> freq = new TreeMap<>();
        int total = 0;

        String line;
        while ((line = br.readLine()) != null && !line.isEmpty()) {
            freq.put(line, freq.getOrDefault(line, 0) + 1);
            total++;
        }

        for (Map.Entry<String, Integer> entry : freq.entrySet()) {
            System.out.printf("%s %.4f%n", entry.getKey(), (entry.getValue() * 100.0) / total);
        }
    }
}