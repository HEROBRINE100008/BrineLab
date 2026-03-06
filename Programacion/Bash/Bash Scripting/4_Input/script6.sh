#!/bin/bash

read -p "Escribe 'actualizar' si quieres actualizar tu sistema: " decision

if [ "$decision" == "actualizar" ]; then
	sudo apt update
	sudo apt upgrade -y
	sudo apt autoremove -y
	echo "Actualización completa"
else
	echo "No se reconoce la instrucción"
	exit
fi
