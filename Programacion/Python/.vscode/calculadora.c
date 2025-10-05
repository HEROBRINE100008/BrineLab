#include <stdio.h>

int main() {
    int Operacion = 0;
    int Valor1, Valor2;
    float Resultado;

    // Pregunta al usuario qué tipo de operación quiere hacer
    do {
        printf("Elige una opción: 1. Sumar 2. Restar 3. Multiplicar 4. Dividir 5. Salir: ");
        scanf("%d", &Operacion);

        switch (Operacion) {
            case 1: // Suma
                printf("Dame el primer valor: ");
                scanf("%d", &Valor1);
                printf("Dame el segundo valor: ");
                scanf("%d", &Valor2);
                Resultado = Valor1 + Valor2;
                printf("Tu resultado es: %.2f\n", Resultado);
                break;

            case 2: // Resta
                printf("Dame el primer valor: ");
                scanf("%d", &Valor1);
                printf("Dame el segundo valor: ");
                scanf("%d", &Valor2);
                Resultado = Valor1 - Valor2;
                printf("Tu resultado es: %.2f\n", Resultado);
                break;

            case 3: // Multiplicación
                printf("Dame el primer valor: ");
                scanf("%d", &Valor1);
                printf("Dame el segundo valor: ");
                scanf("%d", &Valor2);
                Resultado = Valor1 * Valor2;
                printf("Tu resultado es: %.2f\n", Resultado);
                break;

            case 4: // División
                printf("Dame el primer valor: ");
                scanf("%d", &Valor1);
                printf("Dame el segundo valor: ");
                scanf("%d", &Valor2);
                if (Valor2 != 0) {
                    Resultado = (float)Valor1 / Valor2;
                    printf("Tu resultado es: %.2f\n", Resultado);
                } else {
                    printf("Error: No se puede dividir entre cero.\n");
                }
                break;

            case 5: // Salir
                printf("Saliendo del programa.\n");
                break;

            default:
                printf("Opción no válida. Inténtalo de nuevo.\n");
                break;
        }
    } while (Operacion != 5);

    return 0;
}
