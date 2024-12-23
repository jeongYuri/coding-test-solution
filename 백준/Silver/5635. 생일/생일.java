import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine()); 
        String[][] info = new String[n][4];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            info[i][0] = st.nextToken(); 
            info[i][1] = st.nextToken(); 
            info[i][2] = st.nextToken(); 
            info[i][3] = st.nextToken(); 
        }

        Arrays.sort(info, new Comparator<String[]>() {
            @Override
            public int compare(String[] a, String[] b) {
                if (a[3].equals(b[3])) { 
                    if (a[2].equals(b[2])) { 
                        return Integer.parseInt(a[1]) - Integer.parseInt(b[1]); 
                    }
                    return Integer.parseInt(a[2]) - Integer.parseInt(b[2]); 
                }
                return Integer.parseInt(a[3]) - Integer.parseInt(b[3]); 
            }
        });

        System.out.println(info[n - 1][0] + '\n' + info[0][0]);
    }
}
