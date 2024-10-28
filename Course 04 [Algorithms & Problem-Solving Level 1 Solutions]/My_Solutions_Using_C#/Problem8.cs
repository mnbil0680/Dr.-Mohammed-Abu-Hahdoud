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
        enum enPassFail { Pass =1,Fail= 2 }
        static int ReadMark()
        {

            Console.Write("Please enter your Mark : ");
            int Mark = int.Parse(Console.ReadLine());

            return Mark;
        }
        static string CheckMark(int Mark)
        {
            if(Mark >= 50)
                return "Passed";
            else
                return "Failed";
        }
        static void PrintResult(int Mark)
        {
            Console.WriteLine($"\nYour Mark is {Mark} and you are {CheckMark(Mark)}");
        }
        static void Main(string[] args)
        {
            PrintResult(ReadMark());
        }
    }
}