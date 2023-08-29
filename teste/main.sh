#!/usr/bin/sh 
TOPLEVEL=$(git rev-parse --show-toplevel) 
RPSE=$TOPLEVEL/rpse/rpse.py
TEST_TOPLEVEL="$TOPLEVEL/teste/foo" 

cp $TEST_TOPLEVEL/bar/* $TEST_TOPLEVEL
ls $TEST_TOPLEVEL
python3 $RPSE "$TEST_TOPLEVEL/bar01.mkv" "$TEST_TOPLEVEL/foo01.srt" || exit
printf "\n"
ls $TEST_TOPLEVEL/*.*
