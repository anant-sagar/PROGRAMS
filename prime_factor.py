from tabnanny import check


num = int(input("enter a num"))
li=list()
li2=list()

def prime(n):
    for i in range(2,n):
        if n%i==0:
            return 0
            break
    return 1


def checkfactor():
    for i in li:
        if num %i==0:
            li2.append(i)
            
    
    
for i in range(1,num+1):
    var=prime(i)
    if var==1:
        li.append(i)
print(li)
checkfactor()
print(li2)
    
        
    
        
