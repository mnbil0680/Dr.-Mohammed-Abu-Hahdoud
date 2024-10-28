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
            public int Age;
            public bool HasDrivingLicense;
            public bool HasRecommendation;
        }
        static stInfo ReadInfo()
        {
            stInfo Info = new stInfo();

            Console.Write("\nPlease enter your age : ");
            Info.Age = Int32.Parse(Console.ReadLine());

            // enter (true) or (false)
            Console.Write("\nDo you have a driving license : ");
            Info.HasDrivingLicense = Convert.ToBoolean(Console.ReadLine());

            // enter (true) or (false)
            Console.Write("\nDo you have a Recommendation  : ");
            Info.HasRecommendation = Convert.ToBoolean(Console.ReadLine());

            return Info;
        }
        static bool IsAccepted(stInfo Info)
        {
            if(Info.HasRecommendation)
                return true;
            else
                return Info.HasDrivingLicense && Info.Age > 21;
            
        }
        static void PrintResult(stInfo Info)
        {
            if (IsAccepted(Info))
            {
                Console.WriteLine("\nHired");
            }
            else
            {
                Console.WriteLine("\nRejected");
            }
        }
        static void Main(string[] args)
        {
            PrintResult(ReadInfo());
        }
    }
}