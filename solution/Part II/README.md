
# Part II


Let's say you are running the lock/unlock in a multi core machine. Now you want to let multiple threads to run lock() simultaneously. As we saw in part I, locking a node has multiple validations inside. While doing lock on two nodes cause a race condition. If yes, how will you solve it. In short, how do make the lock() function thread safe?

- Multiple threads running it simultaneously shouldn't not affect the correctness.
- Try to make the critical sections more granular. ie. don't create any big atomic/synchronized blocks that will make parallelism suffer.

**Notes:** 
- Multiple processes/threads will be running the same code by sharing the global memory of the tree, the except for the local variables which are private for the threads.
- Threads can interleave between every line of execution. But every line is atomic and it will not switch in the middle of executing a line. ie. operations like x++ or x = x + 1.. are automatically atomic (note: this is not always true in real life.. but assume this for simplifying this problem)
- You can use an instruction called atomic to force only one thread to execute a block of code for an object reference.  `atomic(objRef) { <block of code> }` Note1: if objRef is different between two threads, they can still execute this block of code in parallel. Note2: atomic is same as synchronized keyword in java.
- While it is easier to use atomic blocks, there is a way to solve this problem without using atomic! Don't worry about it now. If there is time, we will help you solve it that way too!

We have to change only Lock operation to run in mulithreaded machine.