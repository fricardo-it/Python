//Course: Scripting
//Student: Andraschko, Francisco Ricardo
//Activity: Assignment 0
//Date: 2023-09-11
//Question: 5

using System.Net.Cache;

internal class Program
{
    private static void Main(string[] args)
    {
        //variables
        double sideA, sideB, sideC, result = 0;
    

        Console.WriteLine("Course: Scripting\nStudent: Andraschko, Francisco Ricardo\nActivity: Assignment 0\nQuestion: 5\n\n");
        //entries
        Console.Write("Enter the 3 sides of possible triangle and discovery if it is:");

    _sideA:
        try
        {
            Console.Write("\nSide A: ");
            sideA = Convert.ToDouble(Console.ReadLine());
        }
        catch (Exception e)
        {
            Console.WriteLine("\n\tSide is in incorrect format. Just use a Number.");
            goto _sideA;
        }

    _sideB:
        try
        {
            Console.Write("\nSide B: ");
            sideB = Convert.ToDouble(Console.ReadLine());
        }
        catch (Exception e)
        {
            Console.WriteLine("\n\tSide is in incorrect format. Just use a Number.");
            goto _sideB;
        }

    _sideC:
        try
        {
            Console.Write("\nSide C: ");
            sideC= Convert.ToDouble(Console.ReadLine());
        }
        catch (Exception e)
        {
            Console.WriteLine("\n\tSide is in incorrect format. Just use a Number.");
            goto _sideC;
        }

        // calculate

        if ((Math.Abs(sideB - sideC) < sideA && sideA < (sideB + sideC)) || 
            (Math.Abs(sideA - sideC) < sideB && sideB < (sideA + sideC)) ||
            (Math.Abs(sideA - sideB) < sideC && sideC < (sideA + sideB)))
        {
            Console.WriteLine("\n\tThe Triangle exist to sides: {0}, {1}, {2}", sideA, sideB, sideC);
        }
        else
        {
                Console.WriteLine("\n\tThe Triangle do not exist to sides: {0}, {1}, {2}", sideA, sideB, sideC);
        }

        Console.WriteLine("\nPress any key to close... bye!");

        Console.ReadKey();
    }
}