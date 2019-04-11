read -p "Enter a prime number: " primeNumber
i=2
f=0
while test $i -le `expr $primeNumber / 2`
do
	if test `expr $primeNumber %2` -eq 0
	then
		f=1
	fi
i=`expr $i +1`
done

if test $f -eq 1
then
	echo "Not prime"
else
	echo "Prime"
fi
