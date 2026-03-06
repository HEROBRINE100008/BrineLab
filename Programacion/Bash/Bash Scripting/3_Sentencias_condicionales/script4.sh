#!/bin/bash

usuario=$(whoami)

if [ "$usuario" == "root" ]; then
	echo "Estas ejecutando el script como root"
elif [ "$usuario" == "herobrine" ]; then
	echo "Estas ejecutando el script como herobrine"
else
	 echo "Ninguno de los 2 usuarios ejecutó el script"
fi
