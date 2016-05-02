from Node import Node
class Tree(object):
  def __init__(self,c):
    self.root = None
    self.size = 0
    self.c=c

  def length(self):
    return self.size

  def __len__(self):
    return self.size

  def insert(self,key):
    if (self.root==None):
      self.c.increment()
      node= Node(key)
      self.root = node
      return
    else :
      self.c.increment()
      self.ins(key,self.root,None)
      return

  def ins(self,key,cr,cp):
    if (cr==None):
      self.c.increment()
      node= Node(key)
      node.pa=cp
      if key<cp.data:
        cp.lchild=node
      else : 
        cp.rchild=node
      return
    elif key<cr.data:
      self.c.increment()
      self.ins(key,cr.lchild,cr)
    else:
      self.c.increment()
      self.ins(key,cr.rchild,cr)
    return

  def search(self,key):
    if (self.root==None): 
      return None
    else:
      return self.sea(key,self.root)

  def sea(self,key,cr):
    if (cr==None):

      return None
    elif key<cr.data:
      
      return self.sea(key,cr.lchild)
    elif key>cr.data:
      return self.sea(key,cr.rchild)
    elif key==cr.data:
      return cr
 
  def successor(self,z):
    if z.rchild is not None:
      return self.mini(z.rchild)
	
  def mini(self,z):
     while z.lchild is not None:
       z = z.lchild
     return z

  def delete(self,key):
     if(self.search(key)):
       node=self.search(key)
       self.dele(node)
       return
  def dele(self,node):
       key = node.data
       if(node.lchild==None and node.rchild==None):
         if(key<node.pa.data):
           node.pa.lchild=None
	 else:
           node.pa.rchild=None
         return

       elif(node.lchild==None or node.rchild==None):
         if(key<node.pa.data):
           if(node.lchild):
             node.pa.lchild=node.lchild
           elif(node.rchild):
             node.pa.lchild=node.rchild
         elif(key>node.pa.data):
           if(node.lchild):
             node.pa.rchild=node.lchild
           elif(node.rchild):
             node.pa.rchild=node.rchild
       
       else :
         suc = self.successor(node)
         node.data = suc.data
         self.dele(suc)
        
       return     
           
  def inprint(self): 
    self.in_order_print(self.root)
  
  def in_order_print(self,root):
    if not root:
      return
    self.in_order_print(root.lchild)
    print root.data
    self.in_order_print(root.rchild)

class Counter(object):
	def __init__(self,count=0):
		self.count = count
	def increment(self):
		self.count+=1
	def reset(self):
		self.count = 0
	def query(self):
		return self.count
  
 
