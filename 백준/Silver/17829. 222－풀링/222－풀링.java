import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int [][] arr = new int[n][n];
        for(int i =0;i<n;i++){
            String[] inputs = br.readLine().split(" ");
            for(int j = 0;j<n;j++){
                arr[i][j] = Integer.parseInt(inputs[j]);
            }
        }

        int currentSize = n;
        int[][] currentArr  = arr; //초기 배열
        while(currentSize>1){
            int newSize = currentSize/2;
            int[][] newArr = new int[newSize][newSize];

            for(int i = 0;i<newSize;i++){
                for(int j = 0;j<newSize;j++){
                    int x = i*2;
                    int y = j*2;

                    int[] temp ={
                        currentArr[x][y],
                        currentArr[x][y+1],
                        currentArr[x+1][y],
                        currentArr[x+1][y+1]
                    };

                    Arrays.sort(temp);
                    newArr[i][j] = temp[2]; //정렬 후 두번째로 큰 값 선택함!
                }
            }
            currentArr = newArr;
            currentSize = newSize;
        }
        System.out.println(currentArr[0][0]);


    }
}