#!/usr/bin/sh bash

if [ "$1" = 'e' ]; then
    rm teste/*.*
    exit
fi

cp teste/clone/* teste/.
ls teste/*.*
python3 rpse "teste/$1" "teste/$2" -d 100000\
    && printf "\n" && ls teste/*.*

