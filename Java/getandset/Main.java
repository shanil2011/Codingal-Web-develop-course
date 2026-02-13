class Student{
    private String name;
    public String getName(){
        return name;
    }
    public void setName(){
        this.name = name;
    }
}
class Main{
    public static void main(String[] args) {
        Student s=new Student();
        s.setname("Aanish @Codingal");
        System.out.println(s.getname());
    }
}
