#include <iostream>

using namespace std;

int main() {
	double trainWeight,secUnit,maxWeight,loadWeight,result;
	char answer,answer2;

	cout << "Introduzca el peso de la locomotora: ";
	cin >> trainWeight;

	cout << "Lleva ténder?(s/n): ";
	cin >> answer;
	if (answer == 's' || answer == 'S') {
		cout << "Introduzca el peso del ténder: ";
		cin >> secUnit;
		
		cout << "Introduzca peso maximo que puede llevar: ";
		cin >> maxWeight;
		maxWeight -= (trainWeight + secUnit);
	} else {
		cout << "Introduzca peso maximo que puede llevar: ";
		cin >> maxWeight;
		maxWeight -= trainWeight;
	}
	do {
		cout << "Introduzca el peso de la carga: ";
		cin >> loadWeight;

		maxWeight -= loadWeight;

		if (maxWeight >= 0) {
			answer2 = '\0';

			cout << "El peso está en rango de capacidad de carga" << endl;
			cout << "Restante: " << maxWeight << "t" << endl;

			cout << "Quiere añadir más carga? (s/n): ";
			cin >> answer2;
		} else {
			cout << "Capacidad de carga sobrepasa por " << maxWeight << "t";
			break;
		}

	} while (answer2 == 's' || answer2 == 'S');
	return 0;
}
