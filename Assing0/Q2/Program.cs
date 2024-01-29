//Course: Scripting
//Student: Andraschko, Francisco Ricardo
//Activity: Assignment 0
//Date: 2023-09-11
//Question: 2

Console.WriteLine("Course: Scripting\nStudent: Andraschko, Francisco Ricardo\nActivity: Assignment 0\nQuestion: 2\n\n");
Console.WriteLine("Enter 2 Nums to SUM:");
//numbers
Console.Write("Num1: ");
double num1 = Convert.ToDouble(Console.ReadLine());
Console.Write("Num2: ");
double num2 = Convert.ToDouble(Console.ReadLine());
//sum and print result
Console.WriteLine("The SUM of Numbers: {0} and {1} is {2}",num1,num2,(num1+num2));
//exit
Console.WriteLine("\nPress any key to close... bye!");

Console.ReadKey();
