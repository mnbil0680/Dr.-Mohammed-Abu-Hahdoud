using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Reflection.Metadata.Ecma335;
using System.Threading;
using System.Threading.Tasks;

namespace AbuHadHoud
{
    internal class Program
    {
        enum enPassFail { Pass = 1, Fail = 2 }
        static void ReadNumber(out int Num1, out int Num2)
        {
            Console.Write("Please enter Number 1 : ");
            Num1 = int.Parse(Console.ReadLine());

            Console.Write("Please enter Number 2 : ");
            Num2 = int.Parse(Console.ReadLine());
        }

        static void Swap(ref int Num1, ref int Num2)
        {
            int Temp = Num1;
            Num1 = Num2;
            Num2 = Temp;

        }


        static void PrintResult(int Num1 , int Num2)
        {
            Console.WriteLine("");
            Console.WriteLine($"Number 1 = {Num1}");
            Console.WriteLine($"Number 2 = {Num2}");

        }
        static void Main(string[] args)

        {
            int Num1, Num2;
            ReadNumber(out Num1, out Num2);
            PrintResult(Num1, Num2);
            Swap(ref Num1, ref Num2);
            PrintResult(Num1, Num2);

        }
    }
}