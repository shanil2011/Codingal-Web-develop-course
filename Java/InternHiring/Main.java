import java.util.Scanner;

public class Main {

    public static Candidate getCandidateDetails(Scanner scanner) throws InvalidInternException {

        System.out.println("Enter the Candidate details:");

        System.out.print("Name: ");
        String name = scanner.nextLine();

        System.out.print("Gender: ");
        String gender = scanner.nextLine();

        System.out.print("Enter percentage in 10th: ");
        int percentage = scanner.nextInt();

        if (percentage < 50) {
            throw new InvalidInternException("Registration Failed. Percentage cannot be less than 50.");
        }

        Candidate candidate = new Candidate();
        candidate.setName(name);
        candidate.setGender(gender);
        candidate.setPercentage(percentage);

        return candidate;
    }

    public static void main(String[] args) {

        System.out.println("Welcome to InterHiring Tool");
        Scanner scanner = new Scanner(System.in);

        try {
            Candidate candidate = getCandidateDetails(scanner);
            System.out.println("Registration Successful");
        } catch (InvalidInternException e) {
            System.out.println(e.getMessage());
        }

        scanner.close();
    }
}

class Candidate {

    private String name;
    private String gender;
    private int percentage;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public int getPercentage() {
        return percentage;
    }

    public void setPercentage(int percentage) {
        this.percentage = percentage;
    }
}

class InvalidInternException extends Exception {

    public InvalidInternException(String message) {
        super(message);
    }
}