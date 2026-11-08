import random
# initialising variables

a=[2.1, 2.3, 2.5, 2.8, 3.0, 3.2, 3.5, 3.8, 4.0, 4.2,
  12.0, 12.3, 12.5, 12.8, 13.0, 13.2, 13.5, 13.8, 14.0, 14.2,
  22.0, 22.2, 22.5, 22.7, 23.0, 23.2, 23.5, 23.8, 24.0, 24.2,
  32.0, 32.3, 32.5, 32.8, 33.0, 33.2, 33.5, 33.8, 34.0, 34.2,
  42.0, 42.3, 42.5, 42.8, 43.0, 43.2, 43.5, 43.8, 44.0, 44.2]
b=[None]*len(a)
c1=0
n1=0
c2=0
n2=0

#randomly assigning clusters


for i in range(len(a)):
  b[i]=random.randint(1,2)
print(b)

def mean(a,b,c1,n1,c2,n2):

  # calculating mean for each cluster
  for i in range(len(a)):
      if b[i]==1:
          c1=c1+1
          n1=n1+a[i]
      else:
          c2=c2+1
          n2=n2+a[i]

  u1=n1/c1
  u2=n2/c2
  print("u1",u1,"u2",u2)

  # storing the old assignment
  bb=b
  print("bb",b)
  #reassignment
  for i in range(len(a)):       
    if abs(a[i]-u1)<abs(a[i]-u2):
      b[i]=1
    else:
      b[i]=2

  print("b=",b)
  return bb,b

while True:
  bb,b=mean(a,b,c1,n1,c2,n2)
  if bb==b:
    print("final cluster:",b)
    break

        
