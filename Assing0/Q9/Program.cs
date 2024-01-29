//Course: Scripting
//Student: Andraschko, Francisco Ricardo
//Activity: Assignment 0
//Date: 2023-09-11
//Question: 9

class Program
{
    static void Main()
    {
        //array
        int[] arr = RandomArray(10);

        Console.WriteLine("Course: Scripting\nStudent: Andraschko, Francisco Ricardo\nActivity: Assignment 0\nQuestion: 9\n\n");
        Console.WriteLine("Enter a int number to find into the array:");

        Console.Write("\nNumber: ");
        int num = Convert.ToInt16(Console.ReadLine());

        bool result = isContain(arr, num);

        if (result)
        {
            Console.WriteLine($"The digit {num} is in the array.");
        }
        else
        {
            Console.WriteLine($"The digit {num} is not in the array.");
        }
    }

    static int[] RandomArray(int size)
    {
        Random random = new Random();
        int[] arr = new int[size];

        for (int i = 0; i < size; i++)
        {
            arr[i] = random.Next(1, 20); // range 1..20
        }

        return arr;
    }

    static bool isContain(int[] arr, int num)
    {
        foreach (int number in arr)
        {
            if (number == num)
            {
                return true;
            }
        }
        return false;
    }
}