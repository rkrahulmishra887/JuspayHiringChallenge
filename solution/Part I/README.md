

# Part I

The problem is based on m-ary tree.
We have to perform two operation on the tree:
- Lock
- Unlock

### Lock
To  perform lock operation on a node in tree, the following condition must be satisfied:
> **1. Node should not have any locked children.**

> **2. Node should not have any locked ancestor.**

- If it satisfies two condition you should perform lock and return True
- If node is already locked then return False

### Unlock
To perform unlock It should satisfy only one condition:

> **1. If node is locked then unlock**

- If locked then unlock and return True
- If not locked then return False

__NOTE :  concider we have direct access to the node in a tree.__

>The solution I have attached will run in **O(h)** for normal tree and **O(log<sub>m</sub>n)** for m-array tree.