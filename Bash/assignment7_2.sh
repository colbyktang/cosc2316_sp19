#! /bin/bash/
read -p "Enter size: " size
i=1
sum=0
echo "Enter numbers"
while [ $i -le $size ]
do
	read num
	sum=$((sum + num))
	i=`expr $i + 1`
done
avg=$((sum / size))
printf "Average: %f\n" $avg
