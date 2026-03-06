#!/bin/bash

documento=frutas.txt

while read -r linea; do
    echo $linea
done < "$documento"