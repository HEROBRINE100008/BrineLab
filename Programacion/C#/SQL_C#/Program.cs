int entrada(){
    Console.WriteLine("Introduce un número: ");
    while(true){
        if (int.TryParse(Console.ReadLine(), out int numero)) {
                return numero;
        } else
        {
            Console.WriteLine("No ta valido eso pai :("); 
            Console.WriteLine("Introduce un número: ");  
        }
    }
}

int numero_1 = entrada();
int numero_2 = entrada();

Console.WriteLine(numero_1);
Console.WriteLine(numero_2);
