from threading import Thread, Lock

class Node:
	def __init__(self, name, parent = None):
		self.name = name
		self.children = []
		self.parent = parent
		self.locked = False
		self.locked_child_count = 0
		if parent:
			parent.addChild(self)
	
	def getChildren(self):
		return self.children[:]

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

	def __repr__(self):
		return str(self.name)


def lock(node, thread_lock):
	with thread_lock:
		if node.isLocked() or node.locked_child_count != 0 :
			return False
		node.setLock()

	locked_parent = None
	parent_node = node.getParent()
	while parent_node:
		with thread_lock:
			if parent_node.isLocked():
				locked_parent = parent_node
				break
			parent_node.locked_child_count += 1
		parent_node = parent_node.getParent()

	if locked_parent:
		parent_node = node.getParent()
		while parent_node != locked_parent:
			with thread_lock:
				parent_node.locked_child_count -= 1
			parent_node = parent_node.getParent()

	if locked_parent:
		with thread_lock:
			node.removeLock()
		return False
	return True

thread_lock = Lock()
t = Thread(target=lock, args = (node, thread_lock))

