#include <iostream>
#include "calc.cpp"

using namespace std;

int main()
{
	int fahr, cels;
	
	cout << "Introduzca la temperatura en celsius: " << endl;
	cin >> cels;

	fahr = calc(cels);

	cout << "Son unos " << fahr << " °F" << endl;

	
}
