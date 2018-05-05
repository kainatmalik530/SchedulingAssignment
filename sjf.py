k=eval(input('no of processes'))
process=[]
x=list(range(0,k))
for n in range(0,k):
    x=input('enter process no:')
    y=eval(input('enter arrival time:'))
    z=eval(input('enter burst time:'))
    process.append([z,y,x])

process.sort()
sum=0
s=0
for n in range(0,k):
        print(process[n])
        g=sum
        sum=sum+process[n][0]
        print(process[n][2],"started at",g,"ended at",sum)
        waitingt=g-process[n][1]
        s=s+waitingt
        
p=s/k
print("waitingtime=",p)
        
                
                 
