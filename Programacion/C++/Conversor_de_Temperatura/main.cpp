#include <iostream>
#include <ostream>

using namespace std;

int main()
{
	int option{0};
	 while (true){
		cout << "Selecciona una opción\n1. °F\n2. °C\n3. K\n4. Salir\n";
		cout << "Ingrese un numero(1-4): ";
		cin >> option;

		cout << "Se ingresó " << option << "\n";
		break;
	}
}
