import java.util.Scanner;

public class Main{

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        try{
            System.out.println("Enter two numbers:");
            int x = sc.nextInt();
            int y = sc.nextInt();
            int z = x/y;
            System.out.println(x + " / " + y + " = " + z);
        }
        catch(ArithmeticException ex){
            System.out.println("---catch block---");
            System.err.println(ex.toString());
        }
        finally{
            System.out.println("---final block---");
            System.out.println("Application Designed and Developed by:");
            System.out.println("Tahsin Shanil and helprd by Amrita Dhar");
            sc.close();
        }
        System.out.println("DONE!");
    }
}