#!/bin/bash
var=$((1 + $RANDOM % 10))
#echo $var

for ((DAYS = 1 ; DAYS <= 30 ; DAYS++)); do
    sudo date -s "2021-10-$DAYS"
    for ((HOURS = 1 ; HOURS < $var ; HOURS++)); do
        echo HOURS $HOURS
        sudo date -s "2021-10-$DAYS $HOURS:00:00"
        echo `/usr/games/fortune -sn 32` > vivek.txt
        git add .
        git commit -m "`/usr/games/fortune -sn 32`"
    done
done
