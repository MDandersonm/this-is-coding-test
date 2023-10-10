#거스름돈
n=1260
result= n//500 + ((n%500) //100) +  (((n%500) %100) //50)  + (((n%500) %100) %50) //10

count=0
array=[500,100,50,10]
for coin in array:
    count += n // coin
    n%=coin
print(count)