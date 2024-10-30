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
        enum enPassFail { Pass =1,Fail=2 }
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
        static double CalculateAverage(int Num1, int Num2, int Num3)
        {
            return SumOf3Numbers(Num1, Num2, Num3) / 3.0;
        }

        static enPassFail CheckAverage(double Average)
        {
            if (Average >= 50)
                return enPassFail.Pass;
            else
                return enPassFail.Fail;
        }
        static void PrintResult(double Average)
        {
            Console.WriteLine($"\nYour average is {Average}");
            if (CheckAverage(Average) == enPassFail.Pass)
                Console.WriteLine("You passed");
            else
                Console.WriteLine("You failed");

        }
        static void Main(string[] args)

        {
            int N1, N2, N3;
            ReadNumber(out N1, out N2, out N3);
            PrintResult(CalculateAverage(N1,N2,N3));
        }
    }
}