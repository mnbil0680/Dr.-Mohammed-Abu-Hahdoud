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
        struct stInfo
        {
            public string FirstName;
            public string LastName;
        }
        static stInfo ReadInfo()
        {
            stInfo Info = new stInfo();

            Console.Write("Please enter your First Name : ");
            Info.FirstName = Console.ReadLine();

            Console.Write("Please enter your Last Name : ");
            Info.LastName = Console.ReadLine();

            return Info;
        }
        static string GetFullName(stInfo Info)
        {
            string FullName = Info.FirstName + " " + Info.LastName;
            return FullName;
        }
        
        static void PrintFullName(string FullName)
        {
            Console.WriteLine($"\nYour Full Name is : {FullName} ");
        }

        static void Main(string[] args)
        {
            PrintFullName(GetFullName(ReadInfo()));
        }
    }
}