//Course: Scripting
//Student: Andraschko, Francisco Ricardo
//Activity: Assignment 0
//Date: 2023-09-11
//Question: 11

using System;
using System.Collections.Generic;

class Person
{
    public string Name { get; set; }
    public int Age { get; set; }

    public Person(string name, int age)
    {
        Name = name;
        Age = age;
    }
}

class Student : Person // student derivated from Person
{
    public double Midterm { get; set; }
    public double Final { get; set; }
    public double Project { get; set; }

    public Student(string name, int age, double midterm, double final, double project) : base(name, age)  // aditionals arguments from Person
    {
        Midterm = midterm;
        Final = final;
        Project = project;
    }

    public double CalculateAverage()
    {
        // Calculate the average of midterm, final, and project grades
        return (Midterm + Final + Project) / 3.0;
    }
}

class Program
{
    static void Main()
    {
        //lists of stuents --> for this, statics values!
        List<Student> students = new List<Student>
        {
            new Student("Francisco", 41, 85, 90, 78),
            new Student("Bruno", 35, 95, 92, 95),
            new Student("Daniel", 22, 92, 85, 89)
        }; 


        double overallAverage = CalculateOverallAverage(students);
        Console.WriteLine("Student Grades:");
        foreach (var student in students)
        {
            Console.WriteLine($"{student.Name} ({student.Age} years old) - Average: {student.CalculateAverage():F2}"); //2 decimal cases
        }

        Console.WriteLine($"\nOverall Average of Students: {overallAverage:F2}"); //2 decimal cases
    }

    static double CalculateOverallAverage(List<Student> students)
    {
        double totalAverage = 0;
        foreach (var student in students)
        {
            totalAverage += student.CalculateAverage();
        }

        return totalAverage / students.Count;
    }
}
