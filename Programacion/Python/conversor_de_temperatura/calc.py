# Calculos de Farenheit
def F_a_C(f): return (f - 32) * 5 / 9
def F_a_K(f): return (f - 32) * 5 / 9 + 273.15
# Calculos de Celsius
def C_a_F(c): return (c * 9 / 5) + 32
def C_a_K(c): return c + 273.15
# Calculos de Kelvin
def K_a_F(k): return (k - 273.15) * 9 / 5 + 32
def K_a_C(k): return k - 273.15


if __name__ == "__main__":
    # Farenheit
    print(F_a_C(float(79)))
    print(F_a_K(float(79)))
    # Celsius
    print(C_a_F(float(26)))
    print(C_a_K(float(26)))
    # Kelvin
    print(K_a_F(float(300)))
    print(K_a_C(float(300)))
