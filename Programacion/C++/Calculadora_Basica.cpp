#include <iostream>
#include <ostream>

int main(){
	double num1, num2, resultado;
	char operacion;

	std::cout << "--- Calculadora Basica ---" << std::endl;

	std::cout << "Introduzca el primer número: ";
	std::cin >> num1;

	std::cout << "Introduzca el segundo número: " << std::endl;
	std::cin >> num2;

	std::cout << "Introduzca la operación (+, -, *, /): ";
	std::cin >> operacion;

	if (operacion == '+') {
		resultado = num1 + num2;
	} else if (operacion == '-') {
		resultado = num1 - num2;
	} else if (operacion == '*') {
		resultado = num1 * num2;
	} else if (operacion == '/') {
		if (num2 != 0) {
			resultado = num1 / num2;
		} else {
			std::cout << "No se puede dividir por cero" << std::endl;
			return 1;
		}
	}
	std::cout << "Resultado: " << resultado << std::endl;
	return 0;
}
