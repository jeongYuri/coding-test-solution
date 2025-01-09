import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        String res = "";
        int hab = 0;
        String[] arr = new String[n];
        for(int i=0;i<n;i++){
            arr[i] = br.readLine().trim();
        }

        for(int i=0;i<m;i++){
            int a = 0, g= 0,c = 0,t = 0;
            for(int j=0;j<n;j++){
                char ch = arr[j].charAt(i);
                if(ch=='T')t++;
                else if(ch=='A')a++;
                else if(ch=='G')g++;
                else if(ch=='C')c++;
                }
                int maxValue = Math.max(a, Math.max(g, Math.max(c, t)));
                if(maxValue==a){
                    res +='A';
                    hab +=c+g+t;
                }
                else if(maxValue==c){
                    res +='C';
                    hab += a+g+t;
                }
                else if(maxValue==g){
                    res +="G";
                    hab += a+c+t;
                }else if(maxValue==t){
                    res +='T';
                    hab+= a+c+g;
                }
            }
        System.out.println(res);
        System.out.println(hab);

        }
        }
    


