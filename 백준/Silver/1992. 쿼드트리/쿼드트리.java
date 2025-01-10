import java.io.*;
import java.util.*;

public class Main {
    static char[][] board;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
        int n = Integer.parseInt(br.readLine());
        board = new char[n][n];
        for(int i=0;i<n;i++){
            board[i] = br.readLine().toCharArray();
        }
        String res = compress(0,0,n);
        System.out.println(res);
        }
        private static String compress(int y, int x, int size){
            char start = board[y][x];
            for(int i=y;i<y+size;i++){
                for(int j=x;j<x+size;j++){
                    if(board[i][j]!=start){
                        int half = size/2;
                        String topLeft = compress(y, x, half);
                        String topRight = compress(y, x+half, half);
                        String bottomLeft = compress(y+half, x, half);
                        String bottomRight = compress(y+half, x+half, half);

                        return "("+topLeft+topRight+bottomLeft+bottomRight+")";
                    }
                }
            }
            return String.valueOf(start);
        }
        }
    


