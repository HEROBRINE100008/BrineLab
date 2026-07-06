#include <iostream>
#include <ostream>

using namespace std;

double temperature(double temp)
{
	cout << "Introduzca la temperatura: ";
	cin >> temp;
	return temp;
};

double F_a_C(double Farh) {return (Farh - 32) * 5 / 9;}
double F_a_K(double Farh) {return (Farh - 32) * 5 /9 + 273.15;}

int main()
{
	int option{0};
	 while (true){
		cout << "Selecciona una opción\n1. °F\n2. °C\n3. K\n4. Salir\n";
		cout << "Ingrese un numero(1-4): ";
		cin >> option;
		
		switch (option) {
			case 1: {
				int subOption{0};
				cout << "Selecciona una opción:\n1. °F a °C\n2. °F a K\n";
				cin >> subOption;
				if (subOption == 1) {
					cout << F_a_C(temperature(0)) << " °C\n";
				}else if (subOption == 2) {
					cout << F_a_K(temperature(0)) << " K\n";
				}
				break;
			}
			case 2:
				cout << "Funcion no implementada\n";
				break;
			case 3:
				cout << "Funcion no implementada\n";
				break;
			case 4:
				break;
		
		}
		cout << "Saliendo del programa...\n";
		break;
	}
}
