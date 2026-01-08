import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        double result;    //make everything a double to ensure correct outputs if decimals
        System.out.println("Enter first operand: ");
        double firstNum = scan.nextDouble();
        System.out.println("Enter second operand: ");
        double secondNum = scan.nextDouble();
        System.out.println("");          // all the calculator menu is right here
        System.out.println("Calculator Menu");
        System.out.println("---------------");
        System.out.println("1. Addition");
        System.out.println("2. Subtraction");
        System.out.println("3. Multiplication");
        System.out.println("4. Division");
        System.out.println("");
        System.out.println("Which operation do you want to perform?");
        double input = scan.nextDouble();   //this will scan what the user inputs

        if (input == 1) {   //these else if statements determine what function of the calculator the user needs
            result = firstNum+secondNum;
            System.out.println("The result of the operation is " + result + ". Goodbye!");


        } else if (input == 2) {
            result = firstNum-secondNum;
            System.out.println("The result of the operation is " + result + ". Goodbye!");

        } else if (input == 3) {
            result = firstNum*secondNum;
            System.out.println("The result of the operation is " + result + ". Goodbye!");


        } else if (input == 4) {
            result =firstNum/secondNum;
            System.out.println("The result of the operation is " + result + ". Goodbye!");


        }
        else {            // this else statement is shown when the user inputs an incorrect number
            System.out.println("");
            System.out.println("Error: Invalid selection! Terminating program.");


        }
    }
}
