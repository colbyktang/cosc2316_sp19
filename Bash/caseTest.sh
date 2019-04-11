#!/bin/bash
echo "Enter A to add numbers"
echo "Enter S to subtract numbers"
echo "Enter Q to quit"
x=5
y=5
read -p "Enter your choice: " reply

case $reply in 
	A|a|ADD) echo "Adding $x and $y"
		echo $(($x + $y)) ;;
	S|s|SUB) echo "Subtracting $x and $y"
		echo $(($x - $y)) ;;
	q|Q|QUIT) echo "Quitting program!"
		exit 0 ;;
	*) echo "Invalid choice!"; exit 1 ;;
esac
