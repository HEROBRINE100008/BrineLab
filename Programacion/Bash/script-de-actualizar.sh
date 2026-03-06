#!/bin/bash

read -p "Escribe 'actualizar' si quieres actualizar tu sistema: " decision

if [ "$decision" == "actualizar" ]; then
	read -p "En que distro estas?:
    1. Arch
    2. Debian
    : " decision2

    if [ "$decision2" == "1" ]; then
        sudo pacman -Syu --noconfirm
        sudo pacman -Rns $(pacman -Qdtq) --noconfirm


    elif [ "$decision2" == "2" ]; then
        sudo apt update
	    sudo apt upgrade -y
	    sudo apt autoremove -y
	    echo "Actualización completa"

    else
	    echo "No se reconoce la instrucción"
	    exit

    fi

else
	echo "No se reconoce la instrucción"
	exit
    
fi
