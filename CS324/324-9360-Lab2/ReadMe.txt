Batuhan Aktan
Lab 2
CISC 324
*The code is compiled in Eclipse the files that have been used are in the lab2/src/lab2


1. Thread 3 with the initial letter of v solved it first.


2. The 3 threads are connected to one another through their parent process which shares certain variables with them, in this code the threads have access to the variables captured, challenge, found and startTime, each with different circumstances where, captured gives us the password and the user name, the challenge giving us the user name, found giving the thread the status of the password cracking and finally start time giving the thread the starting time of the code in ms.


3. To demonstrate this we can comment out the threaded portion (lines 30-40) and uncomment the code between the lines 42-56 and this portion shows an increase of 42.8% on average in terms of solution speed which is measured in ms and printed to stdout averaging around 50ms whereas the multi threaded portion averaging around 35ms


4. The order of the testing variables changing from i,t,v to i,v,t shows a significant increase in the speed of the program, where the i,t,v is averaging around 50ms, the i,v,t averages around 39ms, which is closer to multithreaded portion, however, it is still not on the same level, multithreaded portion is the fastest program averaging 35ms.