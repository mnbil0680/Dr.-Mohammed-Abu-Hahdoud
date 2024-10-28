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
        // Here i Wrote static because Static Main Deals with static method only
        static void PrintName(string Name)
        {
            Console.WriteLine($"\nYour Name Is : {Name}");
        }
        static void Main(string[] args)
        {
            PrintName("Mohamed");
        }
    }
}