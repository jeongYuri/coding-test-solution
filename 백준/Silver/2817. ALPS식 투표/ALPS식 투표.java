import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static final BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws IOException {

        int numParticipants = Integer.parseInt(br.readLine());
        int numStaffs = Integer.parseInt(br.readLine());

        List<Staff> staffs = new ArrayList<>();
        List<Double> allScores = new ArrayList<>();

        for (int i = 0; i < numStaffs; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            int votes = Integer.parseInt(st.nextToken());

            if (votes < numParticipants * 0.05) continue;

            Staff staff = Staff.of(name, votes);
            staffs.add(staff);
            allScores.addAll(staff.getScores());
        }

        allScores.sort(Comparator.reverseOrder());
        int topCount = Math.min(14, allScores.size());
        List<Double> topScores = allScores.subList(0, topCount);

        for (double score : topScores) {
            for (Staff staff : staffs) {
                if (staff.hasScore(score)) {
                    staff.receiveChip();
                    break; 
                }
            }
        }

        staffs.sort(Comparator.comparing(Staff::getName));
        staffs.forEach(System.out::println);
    }

    static class Staff {
        private final String name;
        private final int votes;
        private final List<Double> scores;
        private int chips = 0;

        private Staff(String name, int votes, List<Double> scores) {
            this.name = name;
            this.votes = votes;
            this.scores = scores;
        }

        public static Staff of(String name, int votes) {
            List<Double> list = new ArrayList<>();
            for (int i = 1; i <= 14; i++) {
                list.add((double) votes / i);
            }
            return new Staff(name, votes, list);
        }

        public List<Double> getScores() {
            return scores;
        }

        public boolean hasScore(double score) {
            return scores.contains(score);
        }

        public void receiveChip() {
            chips++;
        }

        public String getName() {
            return name;
        }

        @Override
        public String toString() {
            return name + " " + chips;
        }
    }
}
