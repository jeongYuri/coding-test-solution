import java.io.*;
import java.util.*;

public class Main {
    static class Gear {
        Deque<Integer> teeth = new LinkedList<>();
        
        public Gear(String s) {
            for (char c : s.toCharArray()) {
                teeth.add(c - '0');
            }
        }
        
        public void rotate(int direction) {
            if (direction == 1) {
                teeth.addFirst(teeth.removeLast());
            } else if (direction == -1) {
                teeth.addLast(teeth.removeFirst());
            }
        }
        
        public int getTop() {
            return teeth.getFirst();
        }
        
        public int getLeft() {
            return teeth.toArray(new Integer[0])[6];
        }
        
        public int getRight() {
            return teeth.toArray(new Integer[0])[2];
        }
    }
    
    public static void rotateGears(Gear[] gears, int gearNum, int direction, boolean[] visited) {
        visited[gearNum] = true;
        
        // 왼쪽 톱니바퀴 확인
        if (gearNum > 0 && !visited[gearNum - 1]) {
            if (gears[gearNum].getLeft() != gears[gearNum - 1].getRight()) {
                rotateGears(gears, gearNum - 1, -direction, visited);
            }
        }
        
        // 오른쪽 톱니바퀴 확인
        if (gearNum < 3 && !visited[gearNum + 1]) {
            if (gears[gearNum].getRight() != gears[gearNum + 1].getLeft()) {
                rotateGears(gears, gearNum + 1, -direction, visited);
            }
        }
        
        gears[gearNum].rotate(direction);
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        Gear[] gears = new Gear[4];
        for (int i = 0; i < 4; i++) {
            gears[i] = new Gear(br.readLine());
        }
        
        int k = Integer.parseInt(br.readLine());
        
        for (int i = 0; i < k; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int gearNum = Integer.parseInt(st.nextToken()) - 1;
            int direction = Integer.parseInt(st.nextToken());
            
            boolean[] visited = new boolean[4];
            rotateGears(gears, gearNum, direction, visited);
        }
        
        int score = 0;
        for (int i = 0; i < 4; i++) {
            if (gears[i].getTop() == 1) {
                score += (1 << i);
            }
        }
        
        System.out.println(score);
    }
}