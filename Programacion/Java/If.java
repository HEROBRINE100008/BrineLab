import java.util.Scanner;

public class If {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
        System.out.print("Pon cuanto tiene la chica");
        int edad = sc.nextInt();
        if (edad >= 18) {
            System.out.println("ta muy grande bro");
        } else {
            System.out.println("exaito");
        }}
    }
}
