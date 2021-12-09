#!/bin/bash
var=$((1 + $RANDOM % 30))
#echo $var

for ((DAYS = 10 ; DAYS <= 31 ; DAYS++)); do
    sudo date -s "2021-12-$DAYS"
    for ((HOURS = 1 ; HOURS < $var ; HOURS++)); do
        echo HOURS $HOURS
        sudo date -s "2021-12-$DAYS $HOURS:00:00"
        echo `/usr/games/fortune -sn 32` > vivek.txt
        git add .
        git commit -m "`/usr/games/fortune -sn 32`"
    done
done
