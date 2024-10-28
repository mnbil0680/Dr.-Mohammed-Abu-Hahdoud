using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net.Http;
using System.Threading;
using System.Threading.Tasks;

namespace AbuHadHoud
{
    internal class Program
    {
        static string ReadName()
        {
            string Name;
            Console.Write("Please enter your Name : ");
            Name = Console.ReadLine();
            return Name;
        }

        static void PrintName(string Name)
        {
            Console.WriteLine($"\nYour Name Is : {Name}");
        }
        static void Main(string[] args)
        {
            PrintName(ReadName());
        }
    }
}