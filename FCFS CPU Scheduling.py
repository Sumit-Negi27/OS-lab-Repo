N=int(input("enter the no. of process: "))
print("Enter the Burst time of each process")
bt=[]
wt=[]
wt.append(0)
sum=0
avg=0
for i in range (0,N,1):
    print("P",i+1)
    bt.append(int(input("")))
print(bt)

for j in range (1,N,1):
    wt.append(bt[j])
print(wt)
print("Waiting time for processes: ")
for k in range (0,N-1,1):
    
    print("P",k+1,"= ",wt[k])
print("Avg Waiting will be :")



