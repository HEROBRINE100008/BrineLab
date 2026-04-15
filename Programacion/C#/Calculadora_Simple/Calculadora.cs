public class Calculadora
{
    public double Numero_1 { get; set; }
    public double Numero_2 { get; set; }

    public double Suma() => Numero_1 + Numero_2;
    public double Resta() => Numero_1 - Numero_2;
    public double Multi() => Numero_1 * Numero_2;
    public double Division() {
        if (Numero_2 == 0) throw new DivideByZeroException("No se puede dividir por cero.");
        return Numero_1 / Numero_2;
    }
}