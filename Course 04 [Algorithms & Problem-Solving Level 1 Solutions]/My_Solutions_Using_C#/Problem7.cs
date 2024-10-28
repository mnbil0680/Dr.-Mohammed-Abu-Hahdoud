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
        static int ReadNumber()
        {
            Console.Write("Please enter the number : ");
            int num = Convert.ToInt32(Console.ReadLine());
            return num;
        }
        static double CalculateHalfNumber(int Num)
        {
            return Convert.ToDouble( Num / 2.0);
        }
        static void PrintResult(double HalfNumber)
        {
            Console.WriteLine($"Half of {HalfNumber*2} is {HalfNumber}");
        }

        static void Main(string[] args)
        {
            PrintResult(CalculateHalfNumber(ReadNumber()));
        }
    }
}