//Course: Scripting
//Student: Andraschko, Francisco Ricardo
//Activity: Assignment 0
//Date: 2023-09-11
//Question: 4

using System.Net.Cache;

Console.WriteLine("Course: Scripting\nStudent: Andraschko, Francisco Ricardo\nActivity: Assignment 0\nQuestion: 4\n\n");
_age:
Console.Write("Enter the User Age (in years):");

try
{
    int age = Convert.ToInt16(Console.ReadLine());

    if(age > 0 && age < 12)
    {
        Console.WriteLine("The user is a Child");
    }
    else if (age < 18)
    {
        Console.WriteLine("The user is a Young");
    }
    else if (age < 60)
    {
        Console.WriteLine("The user is a Adult");
    }
    else if (age >= 60)
    {
        Console.WriteLine("The user is a Senior");
    }
    else
    {
        Console.WriteLine("The age is out of range");
    }
}
catch (Exception e)
{
    Console.WriteLine("Age is in incorrect format. Just use Integer Number.");
    goto _age;
}

Console.WriteLine("\nPress any key to close... bye!");

Console.ReadKey();
