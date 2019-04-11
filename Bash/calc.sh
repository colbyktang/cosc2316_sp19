#! /bin/bash/
count=10
if [ $count -ne 10 ]
then
	echo "condition is true"
else
	echo "condition is false"
fi
n=1
while [ $n -le 10 ]
do
	echo "$n"
	n=$((n+1))
done
