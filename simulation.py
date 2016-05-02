from tree import Tree,Node,counter,Nilnode
from redblack import right_rotate,left_rotate,rb_insert,rb_insert_fixup
from random import randint
import math

n_values = []
averages = []
x_axis = []

for k in range(1,50):
	n_values.append(int(math.floor(5*math.pow(1.2,k))))
	x_axis.append(math.log(int(math.floor(5*math.pow(1.2,k)))))

for i in n_values:
	n = int(i)
	counts = []
	count1 = counter()
	t = Tree(count1)
	nil_node = Nilnode()
	t.root = nil_node
	for j in range(0,n):
		k = randint(1,i)
		z = Node(k)
		rb_insert(t,z,nil_node)
		counts.append(t.c.query())
		t.c.reset()
	sum1 = 0
	for s in counts:
		sum1 = sum1+s
	average = float(sum1)/n
	averages.append(average)

import matplotlib.pyplot as plt
	
plt.scatter(x_axis,averages)
plt.title('Search Trees')
plt.ylabel('Avg Values')
plt.xlabel('log(n)')

plt.show()
