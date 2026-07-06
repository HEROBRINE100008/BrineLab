#include <iostream>
#include <cmath>

int main()
{
	constexpr double INIT_TEMP {24.4444};
	double temp{INIT_TEMP};
	double redTemp{0};
	redTemp = round(temp * 100.0) / 100.0;
	std::cout << redTemp << "\n";
}
