k=eval(input('no of processes'))
process=[]
x=list(range(0,k))
for n in range(0,k):
    x=input('enter process no:')
    y=eval(input('enter arrival time:'))
    z=eval(input('enter burst time:'))
    process.append([y,z,x])

process.sort()
sum=0
s=0
for n in range(0,k):
        print(process[n])
        g=sum
        sum=sum+process[n][1]
        print(process[n][2],"started at",g,"ended at",sum)
        wt=g - process[n][0];
        s=s+wt
      
p=s/k
print("waiting time=",p)
