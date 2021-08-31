#!/bin/bash
#echo $var
for ((DAYS = 1 ; DAYS <=31 ; DAYS++)); do
    sudo date -s "2021-9-$DAYS"
    var=$((3 + $RANDOM % 22))
    for ((HOURS = 1 ; HOURS < $var ; HOURS++)); do
        echo HOURS $HOURS
        sudo date -s "2021-9-$DAYS $HOURS:00:00"
        echo `/usr/games/fortune -sn 32` > vivek.txt
        git add .
        git commit -m "`/usr/games/fortune -sn 32`"
	done
done
