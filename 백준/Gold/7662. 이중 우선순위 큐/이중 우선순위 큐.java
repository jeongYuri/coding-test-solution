import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            int k = Integer.parseInt(br.readLine());
            PriorityQueue<Node> minHeap = new PriorityQueue<>();
            PriorityQueue<Node> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
            boolean[] visited = new boolean[k];

            for (int i = 0; i < k; i++) {
                String[] input = br.readLine().split(" ");
                char cmd = input[0].charAt(0);
                int n = Integer.parseInt(input[1]);

                if (cmd == 'I') {
                    Node node = new Node(n, i);
                    minHeap.offer(node);
                    maxHeap.offer(node);
                    visited[i] = true;
                } else {
                    if (n == 1) {
                        while (!maxHeap.isEmpty() && !visited[maxHeap.peek().index]) {
                            maxHeap.poll();
                        }
                        if (!maxHeap.isEmpty()) {
                            visited[maxHeap.poll().index] = false;
                        }
                    } else {
                        while (!minHeap.isEmpty() && !visited[minHeap.peek().index]) {
                            minHeap.poll();
                        }
                        if (!minHeap.isEmpty()) {
                            visited[minHeap.poll().index] = false;
                        }
                    }
                }
            }

            while (!minHeap.isEmpty() && !visited[minHeap.peek().index]) {
                minHeap.poll();
            }
            while (!maxHeap.isEmpty() && !visited[maxHeap.peek().index]) {
                maxHeap.poll();
            }

            if (!minHeap.isEmpty() && !maxHeap.isEmpty()) {
                System.out.println(maxHeap.peek().value + " " + minHeap.peek().value);
            } else {
                System.out.println("EMPTY");
            }
        }
    }

    static class Node implements Comparable<Node> {
        int value, index;

        Node(int value, int index) {
            this.value = value;
            this.index = index;
        }

        @Override
        public int compareTo(Node other) {
            return Integer.compare(this.value, other.value);
        }
    }
}