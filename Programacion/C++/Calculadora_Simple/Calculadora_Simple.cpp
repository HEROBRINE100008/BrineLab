#include <iostream>
#include <ostream>

int Resultado(double result) {
	std::cout << "Su resultado: " << result << std::endl;
	return 0;
}

double Suma(double n1,double n2) {
	double resultado = n1 + n2;
	return resultado;
}

double Resta(double n1,double n2) {
	double resultado = n1 - n2;
	return resultado;
}

double Multiplicacion(double n1,double n2) {
	double resultado = n1 * n2;
	return resultado;
}
double Division(double n1,double n2) {
	double resultado = n1 / n2;
	return resultado;
}

int main() {
	double num1, num2;
	int opcion;
	std::cout << "---- Calculadora Simple ---" << std::endl;
		
	std::cout << "1. Suma" << std::endl;
	std::cout << "2. Resta" << std::endl;
	std::cout << "3. Multiplicación" << std::endl;
	std::cout << "4. División" << std::endl;
	std::cout << "Elija una operación: " << std::endl;

	std::cin >> opcion;

	std::cout << "Introduzca el primer número: " << std::endl;
	std::cin >> num1;
	std::cout << "Introduzca el segundo número: " << std::endl;
	std::cin >> num2;

	if (opcion == 1) {
		Resultado(Suma(num1,num2));
	} else if (opcion == 2) {
		Resultado(Resta(num1,num2));
	} else if (opcion == 3) {
		Resultado(Multiplicacion(num1,num2));
	} else if (opcion == 4) {
		if (num2 != 0) {
			Resultado(Division(num1,num2));
		} else {
			std::cout << "No se puede dividir por cero" << std::endl;
			return 1;
		}
	}
	return 0;
}
