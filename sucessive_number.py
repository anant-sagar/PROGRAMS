def new_func():
    num= input("enter a num")
    tup=list(tuple(num))
    li=[]
    temp=0
    count=0

    for i in range (0,len(tup)):
        i=int((tup[i]))
        li.append(i)
    
    for i in li:
        if temp<i:
            temp=i
            count+=1
        else:
            break;
            
            
    print(count)
            
    if count==len(num):
        print("number is sucessive")
        
    else:
        print("not sucessive")
        

new_func()
    