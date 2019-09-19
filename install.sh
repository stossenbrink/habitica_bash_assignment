#!/bin/bash

mkdir -p  ~/.habitica
cp base.py ~/.habitica/
if [ -z $1 ]
	then
	echo "Requires at least 1 argument"
	exit
fi;
echo '{"uid": "'$2'", "token": "'$3'"} ' > ~/.habitica/$1.json

#habitica custom script
x='python3 ~/.habitica/base.py ~/.habitica/'$1'.json'
echo $x
# execute and persist
alias $1='$x'
echo "alias $1='$x'" >> ~/.bashrc


