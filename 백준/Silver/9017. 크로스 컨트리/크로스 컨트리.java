import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        
        for(int tc = 0;tc<t;tc++){
            int n = Integer.parseInt(br.readLine());
            int[] numbers = new int[n];
            String[] inputs = br.readLine().split(" ");
            for(int j=0;j<n;j++){
                numbers[j] = Integer.parseInt(inputs[j]);
            }
            ArrayList<int[]> team = new ArrayList<>();
            for(int i=0;i<n;i++){
                team.add(new int[]{i+1,numbers[i]});
            }
            HashMap<Integer, Integer> teamCnt = new HashMap<>();
            for(int tm:numbers){
                teamCnt.put(tm,teamCnt.getOrDefault(tm,0)+1);
            }

            ArrayList<int[]>valid = new ArrayList<>();
            for(int[] arr:team){
                if(teamCnt.get(arr[1])>=6){
                    valid.add(new int[]{arr[0],arr[1]});
                }
            }
            Collections.sort(valid, (a,b)->Integer.compare(a[0], b[0]));
            ArrayList<int[]> reRanked =  new ArrayList<>();
            int newRank = 1;
            for(int [] arr:valid){
                reRanked.add(new int[]{newRank,arr[1]});
                newRank++;
            }
            HashMap<Integer,ArrayList<Integer>> ranking = new HashMap<>();
            for(int[] arr: reRanked){
                int rnk = arr[0];
                int tnum = arr[1];
                ranking.putIfAbsent(tnum,new ArrayList<>());
                ranking.get(tnum).add(rnk);
            }
            HashMap<Integer, Integer> ans = new HashMap<>();
            for(Map.Entry<Integer, ArrayList<Integer>> entry: ranking.entrySet()){
                int teamNum = entry.getKey();
                ArrayList<Integer> ranks = entry.getValue();
                int sum4 = 0;
                for(int i=0;i<4;i++){
                    sum4+= ranks.get(i);
                }
                ans.put(teamNum,sum4);
            }
            int minScore = Integer.MAX_VALUE;
            for(int val: ans.values()){
                if(val<minScore){
                    minScore = val;
                }
            }
            ArrayList<Integer> candidates = new ArrayList<>();
            for(Map.Entry<Integer,Integer> entry: ans.entrySet()){
                if(entry.getValue()==minScore){
                    candidates.add(entry.getKey());
                }
            }
            //동접시 5번째 주자 비교!
            if (candidates.size() > 1) {
                int best = Integer.MAX_VALUE;
                ArrayList<Integer> tmp = new ArrayList<>();
                for (int c : candidates) {
                    ArrayList<Integer> ranks = ranking.get(c);
                    int fifth;
                    if (ranks.size() < 5) {
                        fifth = Integer.MAX_VALUE;
                    } else {
                        fifth = ranks.get(4);
                    }
                    if (fifth < best) {
                        best = fifth;
                    }
                }
                for (int c : candidates) {
                    ArrayList<Integer> ranks = ranking.get(c);
                    int fifth = (ranks.size() < 5) ? Integer.MAX_VALUE : ranks.get(4);
                    if (fifth == best) {
                        tmp.add(c);
                    }
                }
                candidates = tmp;
            }

            if (candidates.size() > 1) {
                int best = Integer.MAX_VALUE;
                ArrayList<Integer> tmp = new ArrayList<>();
                for (int c : candidates) {
                    ArrayList<Integer> ranks = ranking.get(c);
                    int sixth;
                    if (ranks.size() < 6) {
                        sixth = Integer.MAX_VALUE;
                    } else {
                        sixth = ranks.get(5);
                    }
                    if (sixth < best) {
                        best = sixth;
                    }
                }
                for (int c : candidates) {
                    ArrayList<Integer> ranks = ranking.get(c);
                    int sixth = (ranks.size() < 6) ? Integer.MAX_VALUE : ranks.get(5);
                    if (sixth == best) {
                        tmp.add(c);
                    }
                }
                candidates = tmp;
            }
        
        int res = Integer.MAX_VALUE;
        for(int c: candidates){
            res = Math.min(res,c);
        }
        System.out.println(res);
    }
    }
}