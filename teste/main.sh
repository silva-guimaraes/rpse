#!/usr/bin/sh 
TOPLEVEL=$(git rev-parse --show-toplevel) 
TEST_TOPLEVEL="$TOPLEVEL/teste/foo" 

cp $TEST_TOPLEVEL/bar/* $TEST_TOPLEVEL
ls $TEST_TOPLEVEL
python3 $TOPLEVEL/rpse "$TEST_TOPLEVEL/bar01.mkv" "$TEST_TOPLEVEL/foo01.srt" || exit
printf "\n"
ls $TEST_TOPLEVEL/*.*
