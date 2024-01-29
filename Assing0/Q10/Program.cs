//Course: Scripting
//Student: Andraschko, Francisco Ricardo
//Activity: Assignment 0
//Date: 2023-09-11
//Question: 10

class Program
{
    static void Main()
    {
        //array
        string word = "abcd";

        Console.WriteLine("Course: Scripting\nStudent: Andraschko, Francisco Ricardo\nActivity: Assignment 0\nQuestion: 9\n\n");
        Console.WriteLine("Enter a 4-letter word (from 'a' to 'z'):");

        Console.Write("\nWord: ");
        string passw = Console.ReadLine();

        if (passw.Length != 4)
        {
            Console.WriteLine("Please enter a 4-letter word.");
        }
        else if (IsValidWord(passw))
        {
            if (passw == word)
            {
                Console.WriteLine("Congrats! Right word: " + word);
            }
            else
            {
                Console.WriteLine("Sorry, wrong word. ");
            }
        }
        else
        {
            Console.WriteLine("Please enter a word containing only lowercase letters ('a' to 'z').");
        }
    }

    static bool IsValidWord(string word)
    {
        foreach (char letter in word)
        {
            if (letter < 'a' || letter > 'z')
            {
                return false;
            }
        }
        return true;
    }
}
