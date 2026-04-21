#!/usr/bin/python3

IAS = float(input("Introduzca la velocidad IAS"))

Alt = float(input("Introduzca la Altitud Crucero"))

Res = IAS + (IAS * 0.02 * Alt/1000)

print(Res)