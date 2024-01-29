//Course: Scripting
//Student: Andraschko, Francisco Ricardo
//Activity: Assignment 0
//Date: 2023-09-11
//Question: 3

Console.WriteLine("Course: Scripting\nStudent: Andraschko, Francisco Ricardo\nActivity: Assignment 0\nQuestion: 3\n\n");
Console.WriteLine("Enter 4 Nums to calculate:");
//numbers
Console.Write("Num1: ");
double num1 = Convert.ToDouble(Console.ReadLine());
Console.Write("Num2: ");
double num2 = Convert.ToDouble(Console.ReadLine());
Console.Write("Num3: ");
double num3 = Convert.ToDouble(Console.ReadLine());
Console.Write("Num4: ");
double num4 = Convert.ToDouble(Console.ReadLine());
//calculate and print result
Console.WriteLine("The formula \"output = ({0} * ({1} - {2}))/{3}\", the result is: {4}", num1, num2, num3, num4, (num1 * (num2 - num3)) / num4);
//exit
Console.WriteLine("\nPress any key to close... bye!");

Console.ReadKey();
