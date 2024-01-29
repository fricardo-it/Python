//Course: Scripting
//Student: Andraschko, Francisco Ricardo
//Activity: Assignment 0
//Date: 2023-09-11
//Question: 7

Console.WriteLine("Course: Scripting\nStudent: Andraschko, Francisco Ricardo\nActivity: Assignment 0\nQuestion: 7\n\n");
Console.WriteLine("Enter a positive integer number of lines:");

_positive:
try
{
    Console.Write("\nNumber: ");
    int num = Convert.ToInt16(Console.ReadLine());

    if (num <= 0)
    {
        Console.WriteLine("Please, use a positive number.");
        goto _positive;
    }
    else
    {
        Console.Write("\nPrinting lines: \n");

        for (int i = 1; i <= num; i++)
        {
            Console.WriteLine(new string('*', i));
        }
    }
}
catch (Exception e)
{
    Console.WriteLine("\n\tPlease, use a positive number...");
    goto _positive;
}

//exit
Console.WriteLine("\nPress any key to close... bye!");

Console.ReadKey();
