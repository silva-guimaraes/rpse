#!/usr/bin/sh 
TOPLEVEL=$(git rev-parse --show-toplevel) 
TEST_TOPLEVEL="$TOPLEVEL/teste/foo" 

cp $TEST_TOPLEVEL/bar/* $TEST_TOPLEVEL
ls $TEST_TOPLEVEL
python3 $TOPLEVEL/rpse "$TEST_TOPLEVEL/$1" "$TEST_TOPLEVEL/$2"\
    -txt || exit
printf "\n"
ls $TEST_TOPLEVEL/*.*
