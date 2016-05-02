from tree import Tree,Node,counter,Nilnode

def left_rotate(tree, x,nil):

    y = x.right
    x.right = y.left
    tree.c.increment()
    if y.left != nil:
        y.left.p = x
    tree.c.increment()
    y.p = x.p
    if x.p == nil:
        tree.root = y
    elif x == x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    tree.c.increment()
    y.left = x
    x.p = y		

def right_rotate(tree, x,nil):

    y = x.left
    x.left = y.right
    tree.c.increment()
    if y.right != nil:
        y.right.p = x
    y.p = x.p
    tree.c.increment()
    if x.p == nil:
        tree.root = y
    elif x == x.p.right:
        x.p.right = y
    else:
        x.p.left = y
    tree.c.increment()    
    y.right = x
    x.p = y

def rb_insert(tree,z,nil):
	
	y = nil
	x = tree.root
	tree.c.increment()
	while x!=nil:
		y = x
		tree.c.increment()
		if z.key < x.key:
			x = x.left
		else:
			x = x.right
	z.p = y
	tree.c.increment()
	if y == nil:
		tree.root = z
	elif z.key < y.key :
		y.left = z
	else:
		y.right = z
	tree.c.increment()	
	z.left = nil
	z.right = nil
	z.color = "red"
	tree.c.increment()
	rb_insert_fixup(tree,z,nil)


def rb_insert_fixup(tree,z,nil):
	while z.p.color == "red":
		tree.c.increment()
		if z.p == z.p.p.left:
			y = z.p.p.right
			tree.c.increment()
			if y.color == "red":
				z.p.color == "black"
				y.color = "black"
				tree.c.increment()
				z.p.p.color = "red"
				z = z.p.p
				tree.c.increment()
			else:
				if z == z.p.right:
					z = z.p
					left_rotate(tree,z,nil)
				tree.c.increment()	
				z.p.color = "black"
				z.p.p.color = "red"
				right_rotate(tree,z.p.p,nil)
		else:
			y = z.p.p.left
			tree.c.increment()
			if y.color == "red":
				tree.c.increment()
				z.p.color == "black"
				y.color = "black"
				tree.c.increment()
				z.p.p.color = "red"
				z = z.p.p
			else:
				if z == z.p.left:
					z = z.p
					right_rotate(tree,z,nil)
				tree.c.increment()	
				z.p.color = "black"
				tree.c.increment()
				z.p.p.color = "red"
				left_rotate(tree,z.p.p,nil)			
	tree.root.color = "black"					
"""
def rb_transplant(tree,u,v,nil):
	if u.p ==nil:
		tree.root=v
	elif u ==u.p.left:
		u.p.left = v
	else:
		u.p.right = v
	v.p=u.p

def min_tree(tree,z,nil):
	while z.left is not nil:
		tree.c.increment()
		z = z.left
	return z


def rb_delete(tree,z,nil):
	y = z
	y_col = y.color
	if z.left ==nil:
		x = z.right
		rb_transplant(tree,z,z.right,nil)
	elif z.right == nil:
		x = z.left
		rb_transplant(tree,z,z.left,nil)
	else :
		y = min_tree(tree,z.right,nil)
	y_col = y.color
	x = y.right
	if y.p == z:
		x.p = y
	else :
		rb_transplant(tree,y,y.right,nil)
		y.right = z.right
		y.right.p = y
	rb_transplant(tree,z,y,nil)
	y.left = z.left
	y.left.p = y
	y.color = z.color
	if y_col == "black":
		rb_delete_fixup(tree,x,nil)

def rb_delete_fixup(tree,x,nil):
	while x!=tree.root and x.color=="black":
		if x == x.p.left:
			w = x.p.right
			if w.color == "red":
				w.color ="black"
				x.p.color = "red"
				left_rotate(tree,x.p,nil)
				w = x.p.right
			if w.left.color == "black" and w.right.color == "black":
				w.color="red"
				x = x.p
			elif w.right.color == "black":
				w.left.color == "black"
				w.color = "red"
				right_rotate(tree,w,nil)
				w = x.p.color
			w.color = x.p.color
			x.p.color = "black"
			w.right.color = "black"
			left_rotate(tree,x.p,nil)
			x = tree.root
		else:
			w = x.p.left
			if w.color == "red":
				w.color ="black"
				x.p.color = "red"
				right_rotate(tree,x.p,nil)
				w = x.p.left
			if w.right.color == "black" and w.left.color == "black":
				w.color="red"
				x = x.p
			elif w.left.color == "black":
				w.right.color == "black"
				w.color = "red"
				left_rotate(tree,w,nil)
				w = x.p.color
			w.color = x.p.color
			x.p.color = "black"
			w.left.color = "black"
			right_rotate(tree,x.p,nil)
			x = tree.root
	x.color = "black"

"""


    
    
