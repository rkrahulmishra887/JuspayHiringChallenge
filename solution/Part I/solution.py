class Node:
	def __init__(self, value, parent = None):
		self.value = name
		self.child = []
		self.parent = parent
		self.locked = False
		self.locked_child_count = 0

		if parent:
			parent.addChild(self)

	def getChildren(self):
		return self.child[:]

	def addChild(self, child):
		if child not in self.child:
			self.child += [child]

	def setParent(self, parent):
		self.parent = parent

	def getParent(self):
		return self.parent

	def isLocked(self):
		return self.locked

	def setLock(self):
		self.locked = True

	def removeLock(self):
		self.locked = False


def lock(node):
	if node.isLocked() or node.locked_child_count != 0 :
		return False

	# checking for ancestor is locked
	parent_node = node.getParent()
	while parent_node:
		if parent_node.isLocked():
			return False
		parent_node = parent_node.getParent()

	# Below part will execute only if we can lock the node
    
	# incrementing 'locked_child_count' by 1 of all ancestor of node
	parent_node = node.getParent()
	while parent_node:
		parent_node.locked_child_count += 1
		parent_node = parent_node.getParent()

	node.setLock()
	return True

def unlock(node):
	if node.isLocked() == False:
		return False

	# Below part will execute only if we can unlock the node

	# decrementing 'locked_child_count' by 1 of all ancestor of node
	parent_node = node.getParent()
	while parent_node:
		parent_node.locked_child_count -= 1
		parent_node = parent_node.getParent()

	node.removeLock()
	return True