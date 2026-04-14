using System;

namespace Calculadora_Simple
{
    class Program
    {
        static void Main(string[] args)
        {
            bool continuar = true;

            do
            {
                Console.WriteLine("===== Calculadora =====");
                Console.WriteLine("1. Suma");
                Console.WriteLine("2. Resta");
                Console.WriteLine("3. Multiplicación");
                Console.WriteLine("4. División");
                Console.WriteLine("5. Salir");
                Console.WriteLine("Presiona una tecla del 1 al 5: ");

                ConsoleKeyInfo tecla = Console.ReadKey(true);

                switch (tecla.Key)
                {
                    case ConsoleKey.D1:
                        Console.WriteLine("Sumas");
                        break;
                    case ConsoleKey.D2:
                        Console.WriteLine("Restas");
                        break;
                    case ConsoleKey.D3:
                        Console.WriteLine("Multiplicaciónes");
                        break;
                    case ConsoleKey.D4:
                        Console.WriteLine("Divisiones");
                        break;
                    case ConsoleKey.D5:
                        continuar = false;
                        break;

                }

            } while (continuar);

            Console.WriteLine("Saliste con exito.");
        }
    }
}
