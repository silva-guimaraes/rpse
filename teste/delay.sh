#!/usr/bin/sh 
TOPLEVEL=$(git rev-parse --show-toplevel) 
TEST_TOPLEVEL="$TOPLEVEL/teste/foo" 

test_head(){
    head -n 2 $(ls $TEST_TOPLEVEL/$1/*.srt | sed -n '1p') 
}

cp $TEST_TOPLEVEL/bar/* $TEST_TOPLEVEL
test_head bar
python3 $TOPLEVEL/rpse "$TEST_TOPLEVEL/bar01.mkv" "$TEST_TOPLEVEL/foo01.srt" -d $1 || exit
printf "\n"
test_head .
