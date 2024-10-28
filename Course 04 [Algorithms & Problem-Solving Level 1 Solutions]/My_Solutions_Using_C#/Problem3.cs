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
        enum enNumberType { odd = 1, even = 2 }
        static int ReadNum()
        {
            int num;
            Console.Write("Please enter your Number : ");
            num = Int32.Parse(Console.ReadLine());
            return num;
        }
        static enNumberType CheckNumberType(int num)
        {
            if (num % 2 == 0)
                return enNumberType.even;
            else
                return enNumberType.odd;
        }
        static void PrintNumberType(enNumberType NumberType)
        {
            if(NumberType == enNumberType.even)
                Console.WriteLine("\nNumber is Even.");
            else
                Console.WriteLine("\nNumber is Odd.");
        }

        static void Main(string[] args)
        {
            PrintNumberType((CheckNumberType(ReadNum())));
        }
    }
}