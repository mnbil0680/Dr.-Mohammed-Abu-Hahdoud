using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Threading;
using System.Threading.Tasks;

namespace AbuHadHoud
{
    internal class Program
    {
        static void ReadNumber(out int Num1, out int Num2, out int Num3)
        {
            Console.Write("Please enter Number 1 : ");
            Num1 = int.Parse(Console.ReadLine());

            Console.Write("Please enter Number 2 : ");
            Num2 = int.Parse(Console.ReadLine());

            Console.Write("Please enter Number 3 : ");
            Num3 = int.Parse(Console.ReadLine());

        }

        static int SumOf3Numbers(int Num1, int Num2, int Num3)
        {
            return Num1 + Num2 + Num3;
        }
        static void PrintResult(int Total)
        {
            Console.WriteLine($"\nThe sum of Total numbers is  : {Total}");
        }
        static void Main(string[] args)

        {
            int N1, N2, N3;
            ReadNumber(out N1, out N2, out N3);
            PrintResult(SumOf3Numbers(N1,N2,N3));
        }
    }
}