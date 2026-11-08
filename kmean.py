'''
This program is a basic demo built to implement the working of k-mean clustering
K-mean clustering: Datapoints are grouped into cluster based on the distance between them and the mean of the cluster
  Initialy, datapoints are randomly assigned to cluster
  then the mean of each cluster is calculated
  the distance between points and mean is calculated and compared
  the datapoint is ressaisgned to the cluster with nearest mean
  this step is continued until the reassignment becomes constant
In this program I have considered only two cluster
''' 
import random

# initialising variables

a=[5,12,14,15,16,18,22,25,28,55]
b=[None]*len(a)
c1=0
n1=0
c2=0
n2=0

#randomly assigning to clusters

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
  print("Mean 1: ",u1,"Mean 2: ",u2)

  #Uncommand the below block of code to see the table

  # print(f"{'dtpt'} | {'dis frm M1'} | {'dis frm M2'}")
  # for i in range( len(a)):
  #    print(f"{a[i]:.3f} | {abs(a[i]-u1):.4f} | {abs(a[i]-u2):.4f}")

  # storing the old assignment
  c=b.copy()
  print("Old assignment: ",c)
  #reassignment
  for i in range(len(a)):       
    if abs(a[i]-u1)<abs(a[i]-u2):
      b[i]=1
    else:
      b[i]=2
  print("Newer Assignement=",b)
  return c,b

#Running the function until we get stable cluster
while True:
  c,b=mean(a,b,c1,n1,c2,n2)
  if c==b:
    print("Final cluster:",b)
    break

#Printing the elements grouped into their cluster
clust1=[]
clust2=[]

for i in range(len(a)):
  if b[i]==1:
    clust1.append(a[i])
  else:
    clust2.append(a[i])
print("Cluster 1: ",clust1)
print("Cluster 2: ",clust2)