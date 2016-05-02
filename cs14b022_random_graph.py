from numpy import random
import math
import numpy as np
import queue 

def gra(G,n,L):

  def degree(G,n):
    deg=[]
    c=0
    for i in range(n):
      for j in range(n):
        if G[i][j]==1:
          c=c+1
      deg.append(c)
      c=0
    return deg

  def max_deg(G,n):
    deg=degree(G,n)
    return max(deg)
  
  def avg_deg(G,n):
    deg=degree(G,n)
    return float(sum(deg)/n)

  def path(g,u,v,p,L):   #from previous project
    L.append(p)
    if u==v :
      return True
    neighbors=[]
    for j in range(1,n+1):
      if g[u-1][j-1] !=0 and j not in L:
        neighbors.append(j) 
    if len(neighbors)==0:
      return False
    for x in neighbors :
      if path(g,x,v,u,L) == True:
        return True
    return False 

  def connectivity(G,n):   #from previous project
    for i in range(n):
      for j in range(i+1,n):
        L=[]
        if path(G,i,j,i,L)== False:
          return False
    return True

  def neighbour(G):         #from previous project
    nbh=[[] for x in range(n)]
    for i in range(n):
      for j in range(n):
        if G[i][j]==1:
          nbh[i].append(j)
    return nbh

  
  def BFS(G,n):
    nbh=neighbour(G)
    D=[[float("inf") for x in range(n)]for x in range(n)]
    for i in range(n):
      for j in range(n):
        if i==j:
          D[i][j]=D[j][i]=0
    for u in range(n):
      Q=queue.Queue()
      Q.enqueue(u)
      while (Q.isEmpty()== False):
        curr=Q.dequeue()
        for node in nbh[curr]:
          if D[u][node]==float("inf"):
            D[u][node]=D[u][curr]+1
            Q.enqueue(node)
    maxes=[]
    for i in range(n):
      maxes.append(max(D[i]))
    return max(maxes) 
  
  L.append(avg_deg(G,n))
  L.append(max_deg(G,n))
  L.append(BFS(G,n))
  return L

x_axis_data=[]
max_deg1=[]
max_deg2=[]
diameter1=[]
diameter2=[]
connected1=[]
connected2=[]
avg_deg1=[]
avg_deg2=[]

def graph1(n):
  p=10.0/n
  m1=[[0 for x in range(n)]for x in range(n)]
  for i in range(n-1):
    for j in range(i+1,n):
      k=np.random.random_sample()
      if k<=p:
        m1[i][j]=m1[j][i]=1
  return m1

def graph2(n):
  g2=[[0 for x in range(n)]for x in range(n)]
  for u in range(n):
    d=random.randint(0,n)
    for i in range(d):
      k=random.randint(0,n)
      if g2[u][k]!=1 and u!=k:
        g2[u][k]=g2[k][u]=1
  return g2  

for n in range(11,200):
  x_axis_data.append(n)
  m1=graph1(n)
  m2=graph2(n)
  L1=[]
  L2=[]
  L1=gra(m1,n,L1)
  L2=gra(m2,n,L2)
  avg_deg1.append(L1[0])
  max_deg1.append(L1[1])
  diameter1.append(L1[2])
  if L1[2]==float("inf"):
    connected1.append(0)
  else:
    connected1.append(1)
  avg_deg2.append(L2[0])
  max_deg2.append(L2[1])
  diameter2.append(L2[2])
  if L2[2]==float("inf"):
    connected2.append(0)
  else:
    connected2.append(1)
  
import matplotlib.pyplot as plt

x_axis_data = np.array(x_axis_data)
max_deg1 = np.array(max_deg1)
max_deg2 = np.array(max_deg2)
diameter1 = np.array(diameter1)
diameter2 = np.array(diameter2)
connected1 = np.array(connected1)
connected2 = np.array(connected2)
avg_deg1 = np.array(avg_deg1)
avg_deg2 = np.array(avg_deg2)


plt.subplot(2,1,1)

plt.plot(x_axis_data, max_deg1, 'b-')
plt.title('graph1.1')
plt.ylabel('max degree')


plt.subplot(2, 1, 2)

plt.plot(x_axis_data, diameter1, 'b-')
plt.title('graph1.2')
plt.ylabel('diameter')
plt.show()

plt.subplot(2, 1, 1)

plt.plot(x_axis_data, connected1, 'b-')
plt.title('graph1.3')
plt.ylabel('connectivity')

plt.subplot(2,1,2)

plt.plot(x_axis_data, avg_deg1, 'b-')
plt.title('graph1.4')
plt.ylabel('avg degree')
plt.show()

plt.subplot(2,1,1)

plt.plot(x_axis_data, max_deg2, 'r-')
plt.title('graph2.1')
plt.ylabel('max degree')


plt.subplot(2, 1, 2)

plt.plot(x_axis_data, diameter2, 'r-')
plt.title('graph2.2')
plt.ylabel('diameter')
plt.show()

plt.subplot(2, 1, 1)

plt.plot(x_axis_data, connected2, 'r-')
plt.title('graph2.3')
plt.ylabel('connectivity')

plt.subplot(2,1,2)

plt.plot(x_axis_data, avg_deg2, 'r-')
plt.title('graph2.4')
plt.ylabel('avg degree')
plt.show()

