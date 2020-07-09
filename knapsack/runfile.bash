#!/bin/bash

path=`ls ./data`
filePath=("ks_1000_0" "ks_10000_0" "ks_106_0" "ks_400_0" "ks_82_0")
for file in $path
do
	echo "---solving for $file--------------------"
	time py solver.py ./data/$file
done
