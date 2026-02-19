#!/bin/bash

archivos=$(ls)

for archivo in $archivos; do
	extensiones=$(echo $archivos | tr "." " " | awk '{print $2}')
	if [ "$extensiones" == "txt" ]; then
		rm $archivo
	else
		echo "El archivo $archivo no tiene extensión .txt, no se borra"
	fi
done
