import java.util.*;

public class Main {
    static List<String> wordSplit(String word) {
        int n = word.length();
        List<String> results = new ArrayList<>();
        for (int i = 1; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                String part1 = word.substring(0, i);
                String part2 = word.substring(i, j);
                String part3 = word.substring(j);
                results.add(part1 + " " + part2 + " " + part3);
            }
        }
        return results;
    }

    static String wordReverse(String word) {
        return new StringBuilder(word).reverse().toString();
    }

    static String hab(List<String> parts) {
        StringBuilder sb = new StringBuilder();
        for (String part : parts) {
            sb.append(part);
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.next(); // 단어 입력받기

        List<String> splitWords = wordSplit(word);
        List<String> reverseRes = new ArrayList<>();

        for (String parts : splitWords) {
            String[] individualParts = parts.split(" ");
            List<String> reverseParts = new ArrayList<>();

            for (String part : individualParts) {
                reverseParts.add(wordReverse(part));
            }

            String res = hab(reverseParts);
            reverseRes.add(res);
        }

        Collections.sort(reverseRes); // 사전순 정리
        if (!reverseRes.isEmpty()) {
            System.out.println(reverseRes.get(0));
        }

        sc.close();
    }
}