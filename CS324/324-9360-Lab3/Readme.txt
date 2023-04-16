Reader.java


Removed everything from previous what I focused on creating was making sure we get the mutex permissions then using the mutex permission and exclusive access we check if there are any active readers or writers if there are any  we add one to write count  which is how many readers are in queue, then if they are empty we put one read to active read count then allow read to read then after read is done we detract the number of active readers and check if the active read is 0 and there are write count waiting which allows us to make sure that reads finish before writes start then we allow write to happen and increase active write and decrease queue.


Writer.java
We basically use the same logic however we make sure that all the reads that could run simultaneously run before we release.


Synch.java
We adapted to have queues as well as a new semaphore.