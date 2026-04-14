public class Calculadora
{
    public double Numero_1 { get; set; }
    public double Numero_2 { get; set; }

    public double Suma() => Numero_1 + Numero_2;
    public double resta() => Numero_1 - Numero_2;
    public double multi() => Numero_1 * Numero_2;
    public double division() {
        if (Numero_2 == 0) throw new DivideByZeroException("No se puede dividir por cero.");
        return Numero_1 / Numero_2;
    }
}