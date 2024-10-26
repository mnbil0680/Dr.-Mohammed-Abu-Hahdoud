using System.Linq;
using System.Numerics;
using System.Threading.Channels;
namespace ConsoleApp1
{
    internal class Program
    {

        static void Main()
        {

           

        }
    }
    public class clsDate
    {                                               //   0, 1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11, 12
        private static readonly int[] DaysToMonth365 = { 0, 31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30 };
        private static readonly int[] DaysToMonth366 = { 0, 31, 29, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30 };
        private int day;
        private int month;
        private int year;

        public clsDate(int day, int month, int year)
        {
            bool IsLeapYear = year % 4 == 0 && (year % 100 != 0 || year % 400 == 0);
            if ((year >= 1 && year <= 9999) && (month >= 1 && month <= 12))
            {
                int[] days = IsLeapYear ? DaysToMonth366 : DaysToMonth365;
                if (day >= 1 && day <= days[month])
                {
                    this.day = day;
                    this.month = month;
                    this.year = year;
                }
                else
                {
                    this.day = 1;
                    this.month = 1;
                    this.year = 1;
                }
            }
            else
            {
                this.day = 1;
                this.month = 1;
                this.year = 1;
            }
        }
        public clsDate(int year) : this(1, 1, year) { }
        public clsDate(int month, int year) : this(1, month, year) { }
        public void PrintDate()
        {

            Console.WriteLine(
                $"{day.ToString().PadLeft(2, '0')}" +
                $"/{month.ToString().PadLeft(2, '0')}" +
                $"/{year.ToString().PadLeft(4, '0')}"
                );
        }
        public string GetDate()
        {
            return $"{day.ToString().PadLeft(2, '0')}/{month.ToString().PadLeft(2, '0')}/{year.ToString().PadLeft(4, '0')}";
        }
    }
    public class clsEmplyee
    {
        private int ID;
        private clsEmplyee()
        {

        }
        private clsEmplyee(int id)
        {
            ID = id;
        }
        public static clsEmplyee create(int id)
        {
            return new clsEmplyee(id);
        }
    }
    public class clsDollar
    {
        private decimal _Amount;
        public decimal amount
        {
            get
            {
                return this._Amount;
            }
            private set
            {
                this._Amount = proccessValue(value);
            }
        }
        

        // this is a method instead of private set{}
        public void SetAmount(decimal value)
        {
            amount = value;
        }
        public bool IsZero => _Amount == 0;
        public decimal ConversionFactor { get; } = 1.99m;


        // this is a constructor
        public clsDollar(decimal Amount)
        {

            this._Amount= proccessValue(Amount);
        }
        private decimal proccessValue(decimal value) => value <= 0 ? 0 : Math.Round(value,2); 
    }
}
