import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine().trim());

        List<Word> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            list.add(new Word(br.readLine().trim(), i));
        }

        Collections.sort(list);

        String prefix = "";
        int minIdx = Integer.MAX_VALUE;

        for (int i = 0; i < n - 1; i++) {
            Word w1 = list.get(i);
            Word w2 = list.get(i + 1);

            int len = getPrefixLen(w1.text, w2.text);

            if (len > prefix.length() || (len == prefix.length() && Math.min(w1.idx, w2.idx) < minIdx)) {
                prefix = w1.text.substring(0, len);
                minIdx = Math.min(w1.idx, w2.idx);
            }
        }

        List<Word> res = new ArrayList<>();
        for (Word w : list) {
            if (w.text.startsWith(prefix)) {
                res.add(w);
            }
        }

        res.sort(Comparator.comparingInt(w -> w.idx));

        System.out.println(res.get(0).text);
        System.out.println(res.get(1).text);
    }

    private static int getPrefixLen(String s1, String s2) {
        int len = Math.min(s1.length(), s2.length());
        int i = 0;
        while (i < len && s1.charAt(i) == s2.charAt(i)) {
            i++;
        }
        return i;
    }

    // 단어 + 인덱스 저장
    static class Word implements Comparable<Word> {
        String text;
        int idx;

        public Word(String text, int idx) {
            this.text = text;
            this.idx = idx;
        }

        @Override
        public int compareTo(Word o) {
            return this.text.compareTo(o.text);
        }
    }
}