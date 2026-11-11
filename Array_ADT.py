C=5
a=[None]*C
count=0


def ins1():
    global count, C, a
    if count==C:
        print("Array is full, cannot insert"); return
    a[count]=input("Enter element ")
    count=count+1
    print(a)

def ins2():
    global count, C, a
    if count==C:
        print("Array is full, cannot insert"); return

    pos=int(input('Enter position:'))
    if 0< pos <= count:
        for i in range(count-1,pos-2,-1):
            a[i+1]=a[i]
        a[pos-1]=input('Enter value:')
        count=count+1
    else: 
        print('invalid position')
    print(a)

def dele1():
    global count, C, a
    if count==0:
        print("Array is empty, cannot delete"); return
    a[count]=None
    count=count-1
    print(a)

def dele2():
    global count, C, a
    if count==0:
        print("Array is empty, cannot delete"); return
    else:
        pos=int(input('Enter position:'))
        if 0< pos <= count:
            for i in range(pos-1,count-1,1):
                a[i]=a[i+1]
            count=count-1
            a[count]=None
        else: 
            print('invalid position')
    print(a)

def tra():
    print("Elements of array:")
    for i in range(C):
        print('a[',i,']=',a[i])

def upd():
    global count, C, a
    if count==0:
        print("Array is empty, cannot update"); return
    pos=int(input('Enter position:'))
    if 0< pos <= count:
        a[pos-1]=input('Enter value:')
    print(a)

def Lins():
    global count, C, a
    if count==0:
        print("Array is empty, cannot search"); return
    t=input('Enter element to search:')
    for i in range(count):
        if str(a[i])==t:
            print("Element found at position:",i+1); return
    print("Element not found")

def BinS():
    global count, C, a
    if count==0:
        print("Array is empty, cannot search"); return
    for i in range(count-1):
        for j in range(count-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    t,low,high=input('Enter element to search:'),0,count-1
    while low<=high:
        mid=(low+high)//2
        if str(a[mid])==t:
            print("Element found at position:",mid+1); return
        elif str(a[mid])<t:
            low=mid+1
        else:
            high=mid-1

        print("element not found")



        
            
    


while True:
   
    print("Menu\n------------\n1.Insert at end\n2. Insert at specific position\n2.Delete\n3.Traverse/Display\n4.Update\n5.Linear Search\n6.Binary Search")
    ch=int(input("Enter your choice: "))
    match(ch):
        case 1:
            
                ins1()
        case 2:
                ins2()
        case 3:
            dele1()
        case 4:
            dele2()
        case 5:
            tra()
        case 6:
            upd()
        case 7:
            Lins()
        case 8:
            BinS()



