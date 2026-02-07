class Student
{
    int id;
    String name;
    float stipend;

    Student(int id, String name){
        this.id=id;
        this.name = name;
    }

    Student(int id, String name, float stipend){
        this.id = id;
        this.name = name;
        this.stipend = stipend;
    }

    void displayDetails(){
        System.out.println(this.id + " | "+ this.name + " | " + this.stipend);
    }
}
class Main
{
    public static void main(String[] args)
    {
        Student s1 = new Student(101, "John");
        Student s2 = new Student(102, "Jane", 1500.50f);
        Student s3 = new Student(103, "Doe", 2000.00f);

        s1.displayDetails();
        s2.displayDetails();
        s3.displayDetails();
    }
}