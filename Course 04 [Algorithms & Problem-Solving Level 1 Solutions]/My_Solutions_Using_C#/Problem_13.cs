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
        static void ReadNumber(out int Num1, out int Num2, out int Num3)
        {
            Console.Write("Please enter Number 1 : ");
            Num1 = int.Parse(Console.ReadLine());

            Console.Write("Please enter Number 2 : ");
            Num2 = int.Parse(Console.ReadLine());

            Console.Write("Please enter Number 3 : ");
            Num3 = int.Parse(Console.ReadLine());

        }

        static int MaxOf3Numbers(int Num1, int Num2, int Num3)
        {
            if (Num1 >= Num2 && Num1 >= Num3)
            {
                return Num1;
            }
            else if (Num2 >= Num1 && Num2 >= Num3)
            {
                return Num2;
            }
            else
            {
                return Num3;
            }
        }


        static void PrintResult(int Max)
        {
            Console.WriteLine($"The Maximum number is : {Max}");

        }
        static void Main(string[] args)

        {
            int N1, N2, N3;
            ReadNumber(out N1, out N2, out N3);
            PrintResult(MaxOf3Numbers(N1, N2, N3));
        }
    }
}