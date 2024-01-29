//Course: Scripting
//Student: Andraschko, Francisco Ricardo
//Activity: Assignment 0
//Date: 2023-09-11
//Question: 8

class Program
{
    static void Main()
    {
        Console.WriteLine("Course: Scripting\nStudent: Andraschko, Francisco Ricardo\nActivity: Assignment 0\nQuestion: 8\n\n");
        Console.WriteLine("Enter a positive integer number to calculate the factorial:");

        Console.Write("\nNumber: ");
        int num = Convert.ToInt16(Console.ReadLine());

        Console.Write("\nFactorial {0}! = {1}",num, factorialCalculate(num));
    }
    static int factorialCalculate(int num)
    {
        int result = 1;
        for (int i = 1; i <= num; i++)
        {
            result *= i;

        }
        return result;
    }
}