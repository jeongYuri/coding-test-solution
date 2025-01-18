import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<Student> students = new ArrayList<>();
        for(int i=0;i<n;i++){
            int country = sc.nextInt();
            int num = sc.nextInt();
            int score = sc.nextInt();
            students.add(new Student(country, num, score));
        }
        students.sort((s1,s2)->s2.score-s1.score);
        Map<Integer, Integer> medals = new HashMap<>();
        List<Student> winners = new ArrayList<>();
        for(Student student: students){
            if(winners.size()==3)break;
            int country = student.country;
            medals.putIfAbsent(country,0);
            if(medals.get(country)<2){
                winners.add(student);
                medals.put(country,medals.get(country)+1);
            }
        }
        for(Student winner : winners){
            System.out.println(winner.country +" "+ winner.num);
        }
    }
}
class Student {
    int country;
    int num;
    int score;
    public Student(int country, int num, int score){
        this.country = country;
        this.num = num;
        this.score = score;
    }

    
}