using System;

namespace Calculadora_Simple
{
    class Program
    {
        public static double Input(string num)
        {
            Console.WriteLine($"Introduce el {num} número: ");
            while (true)
            {
                if (double.TryParse(Console.ReadLine(), out double numero))
                {
                    return numero;
                }
                else
                {
                    Console.WriteLine("Entrada no valida");
                    Console.WriteLine($"Introduce el {num} número: ");
                }
            }
        }
        static void Main(string[] args)
        {
            bool continuar = true;

            do
            {
                Calculadora simCal = new Calculadora();

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
                        simCal.Numero_1 = Input("primer");
                        simCal.Numero_2 = Input("segundo");
                        Console.WriteLine($"Resultado: {simCal.Suma()}");
                        Console.WriteLine("Presione una tecla para continuar...");
                        Console.ReadKey(true);
                        break;
                    case ConsoleKey.D2:
                        simCal.Numero_1 = Input("primer");
                        simCal.Numero_2 = Input("segundo");
                        Console.WriteLine($"Resultado: {simCal.Resta()}");
                        Console.WriteLine("Presione una tecla para continuar...");
                        Console.ReadKey(true);
                        break;
                    case ConsoleKey.D3:
                        simCal.Numero_1 = Input("primer");
                        simCal.Numero_2 = Input("segundo");
                        Console.WriteLine($"Resultado: {simCal.Multi()}");
                        Console.WriteLine("Presione una tecla para continuar...");
                        Console.ReadKey(true);
                        break;
                    case ConsoleKey.D4:
                        simCal.Numero_1 = Input("primer");
                        simCal.Numero_2 = Input("segundo");
                        try 
                        {
                            Console.WriteLine($"Resultado: {simCal.Division()}");
                        }
                        catch (DivideByZeroException ex)
                        {
                            Console.WriteLine($"Error: {ex.Message}");
                        }
                        Console.WriteLine("Presione una tecla para continuar...");
                        Console.ReadKey(true);
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
