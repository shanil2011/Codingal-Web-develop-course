import java.util.Arrays;

public class Main{
    public static void main(String[] args){
      String[] names = {"Shanil", "Hasnat", "Sarjis", "Nahid", "Nasiruddin", "Abbas"};

      String Name = "Abbas";

      boolean found = Arrays.stream(names).anyMatch(name -> name.equals(Name));

       if(found) {
            System.out.println(Name + " Chandabaz has found.");
        } else {
            System.out.println(Name + " Chandabaz has not found.");
        }
    }
}