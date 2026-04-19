Console.WriteLine("Introducir Voltios: ");
string entrada = Console.ReadLine();

double Volts = double.Parse(entrada);

Console.WriteLine("Introducir Amperios: ");
string entrada2 = Console.ReadLine();

double Amps = double.Parse(entrada2);

double resultado = Volts * Amps;

Console.WriteLine(resultado);