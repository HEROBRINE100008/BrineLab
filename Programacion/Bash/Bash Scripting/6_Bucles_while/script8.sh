#!/bin/bash

contador=1

while [ "$contador" -lt 5 ]; do
    echo "En esta vuelta la variable vale $contador"
    ((contador++))
    
done