#include <iostream>

void Resultado(double result) {
	std::cout << "---------------------------------" << std::endl;
	std::cout << "Su resultado es: " << result << std::endl;
	std::cout << "---------------------------------" << std::endl;
}

double Suma(double n1, double n2)		{ return n1 + n2; }
double Resta(double n1, double n2)		{ return n1 - n2; }
double Multiplicacion(double n1, double n2)	{ return n1 * n2; }
double Division(double n1, double n2)		{ return n1 / n2; }

int main() {
	double num1, num2;
	int opcion;
	bool continuar = true;

	while (continuar) {
		std::cout << "\n----- Calculadora Simple V2 -----" << std::endl;
		std::cout << "1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Salir" << std::endl;
		std::cout << "Elija una operacion: ";
		std::cin >> opcion;

		if (std::cin.fail()) {
			std::cin.clear();
			std::cin.ignore(1000, '\n');
			std::cout << "\nError: Debes introdicir un número" << std::endl;
			continue;
		}

		if (opcion == 5) {
			continuar = false;
			std::cout << "Saliendo..." << std::endl;
			break;
		}

		if (opcion >= 1 && opcion <= 4) {
			std::cout << "Introduzca primer número: ";
			std::cin >> num1;
			std::cout << "Introduzca segudno número: ";
			std::cin >> num2;
		} else {
			std::cout << "\nError: Opcion no valida." << std::endl;
			continue;
		}

		if (opcion == 1)	Resultado(Suma(num1, num2));
		else if (opcion == 2)	Resultado(Resta(num1, num2));
		else if (opcion == 3)	Resultado(Multiplicacion(num1, num2));
		else if (opcion == 4){
			if (num2 != 0)	Resultado(Division(num1, num2));
			else std::cout << "\nError: No se puede dividir por cero." << std::endl;
		}
	}

	return 0;
}
