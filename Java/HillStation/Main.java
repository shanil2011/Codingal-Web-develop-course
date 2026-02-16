class HillStation {

void location() {

System.out.println("Location is:");

}

void famousFor() {

System.out.println("Famous for:");

}

}

class Manali extends HillStation {

void location() {

System.out.println("Manali is in Himachal Pradesh, India.");

}

void famousFor() {

System.out.println("It is famous for adventure sports.");

}

}

class Mussoorie extends HillStation {

void location() {

System.out.println("Mussoorie is in Uttarakhand.");

}

void famousFor() {

System.out.println("It is famous for educational institutions.");

}

}

class Gulmarg extends HillStation {

void location() {

System.out.println("Gulmarg is in Jammu and Kashmir.");

}

void famousFor() {

System.out.println("It is famous for skiing.");

}

}

class Main {

public static void main(String args[]) {

HillStation M = new Manali();

HillStation Mu = new Mussoorie();

HillStation G = new Gulmarg();

M.location();

M.famousFor();

Mu.location();

Mu.famousFor();

G.location();

G.famousFor();

}

}