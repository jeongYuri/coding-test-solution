
import java.util.Scanner;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
public class Main {

     public static void main(String[] args) throws IOException {
          BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
          int[][] bingo = new int[5][5];
          int[][] talk = new int[5][5];
      
          for(int i=0;i<5;i++){
               StringTokenizer st = new StringTokenizer(br.readLine());
               for(int j=0;j<5;j++){
                    bingo[i][j] = Integer.parseInt(st.nextToken());
               }
          }
          for(int i=0;i<5;i++){
               StringTokenizer st = new StringTokenizer(br.readLine());
               for(int j=0;j<5;j++){
                    talk[i][j] = Integer.parseInt(st.nextToken());
               }
          }
          int count = 0;
          for(int i=0;i<5;i++){
               for(int j=0;j<5;j++){
                    int num = talk[i][j];
                    count ++;

                    for(int x = 0; x<5;x++){
                         for(int y = 0;y<5;y++){
                              if(bingo[x][y]==num){
                                   bingo[x][y] = 0;
                              }
                         }
                    }
                    if (check_bingo(bingo)>=3){
                         System.out.println(count);
                         return;
                    }

               }
          }
     
     }private static int check_bingo(int[][]board){
          int cnt = 0;
          for(int[] row : board){
               int sum = 0;
               for(int num:row){
                    sum += num;
               }
               if(sum==0){
                    cnt++;
               }
          }
          for(int c = 0;c<5;c++){
               int sum = 0;
               for(int r=0;r<5;r++){
                    sum+= board[r][c];
               }
               if(sum==0){
                    cnt++;
               }
          }

          int primarysum = 0;
          for(int i=0;i<5;i++){
               primarysum +=board[i][i];

          }if(primarysum ==0){
               cnt++;
          }
          int secondsum = 0;
          for(int i=0;i<5;i++){
               secondsum += board[i][4-i];
          }
          if(secondsum==0){
               cnt++;
          }
          return cnt;
     }
}