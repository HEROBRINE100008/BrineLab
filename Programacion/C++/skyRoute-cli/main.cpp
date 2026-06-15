#include <iostream>
#include <vector>
#include <string>

struct Vuelo{
	std::string code;
	std::string origin;
	std::string destination;
	double distance;
	std::string typePlane;
};

int main() {
	std::vector<Vuelo> listaVuelos;

	std::cout << "=== SkyLink Avionics ===\n";

	Vuelo nuevoVuelo;

	std::cout << "Introduzca el codigo de vuelo: ";
	std::cin >> nuevoVuelo.code;
	
	std::cout << "Introduzca el aeropueto de origen: ";
	std::cin >> nuevoVuelo.origin;

	std::cout << "Introduzca el aeropuerto de destino: ";
	std::cin >> nuevoVuelo.destination;

	std::cout << "Introduzca distancia en millas nauticas: ";
	std::cin >> nuevoVuelo.distance;

	std::cout << "Tipo de Aeronave (Grande / Pequeno): ";
	std::cin >> nuevoVuelo.typePlane;

	listaVuelos.push_back(nuevoVuelo);

	std::cout << "\nVuelo " << nuevoVuelo.code << " registrado\n";
	std::cout << "Total de vuelos en la base: " << listaVuelos.size();

	return 0;
}
