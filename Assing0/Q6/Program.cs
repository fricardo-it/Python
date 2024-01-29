//Course: Scripting
//Student: Andraschko, Francisco Ricardo
//Activity: Assignment 0
//Date: 2023-09-11
//Question: 6

Console.WriteLine("Course: Scripting\nStudent: Andraschko, Francisco Ricardo\nActivity: Assignment 0\nQuestion: 6\n\n");
Console.WriteLine("Enter a positive integer number:");

_positive:
try
{
    Console.Write("\nNumber: ");
    int num = Convert.ToInt16(Console.ReadLine());

    Console.Write("\nCounting from 1 to {0}: \n", num);

    for (int i = 0; i < num; i++)
    {
        Console.WriteLine(i+1);
    }
}
catch (Exception e)
{
    Console.WriteLine("\n\tThe number is in incorrect format. Just use Integer Number.");
    goto _positive;
}

//exit
Console.WriteLine("\nPress any key to close... bye!");

Console.ReadKey();
