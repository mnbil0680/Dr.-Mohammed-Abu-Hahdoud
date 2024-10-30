using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Reflection.Metadata.Ecma335;
using System.Runtime.InteropServices;
using System.Threading;
using System.Threading.Tasks;

namespace AbuHadHoud
{
    internal class Program
    {
        enum enPassFail { Pass = 1, Fail = 2 }
        static void ReadNumber(out double A, out double B)
        {
            Console.Write("Please enter Rectangle width A : ");
            A = int.Parse(Console.ReadLine());

            Console.Write("Please enter Rectangle length B : ");
            B = int.Parse(Console.ReadLine());
        }

        static double CalculateRectangleArea(double A, double B)
        {
            return A * B;
        }



        static void PrintResult(double Area)
        {
           
            Console.WriteLine($"\nRectangle Area = {Area}");

        }
        static void Main(string[] args)

        {
            double A, B;
            ReadNumber(out A, out B);
            PrintResult(CalculateRectangleArea(A,B));

        }
    }
}