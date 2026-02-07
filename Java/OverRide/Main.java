class Parent
{
    public void sayHello()
    {
        System.out.println("Hello from the parent.");
    }
}
class Child extends Parent
{
    @Override
    public void sayHello()
    {
        System.out.println("Hello from the child.");
    }
}
class Main
{
    public static void main(String[] args)
    {
        Parent p = new Child();
        p.sayHello();
    }
}