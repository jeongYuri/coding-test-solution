import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        sc.nextLine(); // 개행 문자 제거

        Set<String> office = new HashSet<>();
        
        for (int i = 0; i < t; i++) {
            String[] input = sc.nextLine().split(" ");
            String name = input[0];
            String state = input[1];

            if (state.equals("enter")) {
                office.add(name);
            } else {
                office.remove(name);
            }
        }

        // 모든 입력 처리가 끝난 후에 출력
        List<String> officeLog = new ArrayList<>(office);
        Collections.sort(officeLog, Collections.reverseOrder()); // 역순 정렬

        for (String name : officeLog) {
            System.out.println(name);
        }

        sc.close();
    }
}