#!/usr/bin/sh 
TOPLEVEL=$(git rev-parse --show-toplevel) 
rm $TOPLEVEL/teste/foo/*.*
