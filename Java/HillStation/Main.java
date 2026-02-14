class Hillstation{
    void location(){
        System.out.println("Location is :");
    }
    void famousfor(){
        System.out.println("Famous for :");
    }
}

class Manali extends Hillstation{
    void location(){
        System.out.println("Manai is in Himachol pradesh in India.");
    }
    void famousfor(){
        System.out.println("It is famous for adventure sports.");
    }
}

class Mussorie extends Hillstation{
    void location(){
        System.out.println("Mussorie is in Uttarkhand.");
    }
    void famousfor(){
        System.out.println("It is famous for eduacation instituition.");
    }
}

class Gulmarg extends Hillstation{
    void location(){
        System.out.println("Gulmarg is in J and k.");
    }
    void famousfor(){
        System.out.println("It is famous for skiing.");
    }
}

class Main{
    public static void main(String args[]){
        Hillstation A = new Hillstation();

        Hillstation M = new Hillstation();

        Hillstation Mu = new Hillstation();

        Hillstation G = new Hillstation();

        A.location();
        A.famousfor();

        M.location();
        M.famousfor();

        Mu.location();
        Mu.location();

        G.location();
        G.famousfor();
    }
}