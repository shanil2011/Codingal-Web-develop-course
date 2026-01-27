class Main {
  public static void main(String[] args) {

	int a=10;
	int b=5;
    System.out.println("==============Guess the Answers==========");

	System.out.println("Uninary Operator"+ (a++));
	System.out.println("Uninary Operator"+ (++b));
	System.out.println("Binary Operator");
	System.out.println("1+2 " +1+2);
	System.out.println("1+2 " +(1+2));
	System.out.println(1+2 +" =3");
	int increment = ++a * b++;
	System.out.println(increment);
	//uncomment the next lines to know the values
	//System.out.println("Current Value of a: " +a);
	//System.out.println("Current Value of b: " +b);
	System.out.println("Ternany Operator");
	int largestNumber=(a>b)?a:b;
	System.out.println("Largest of 2 numbers: "+largestNumber);

  }
}