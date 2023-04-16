CISC 324 Lab 1
Batuhan Aktan
20229360

1.1  The problem with exercise 1 is that the code does not wait for the child to finish before displaying the output, what it does is compute 1+...+n/2 and doesn’t wait for (n/2+1)+...+n to compute and add to total.

1.3 The sum becomes incorrect when the sum of the second half ((n/2+1)+...+n) is a value that requires more than a byte to store, the reason for that is exit(v) can only store 1 byte in the v value, thus leading the program to not be able to store for more than 255 of unsigned values.

1.4 Switching the functions will not create a big difference in terms of functionality, it will still be able to compute the same amount however, the maximum value that this program can accommodate for will be larger since it becomes more difficult to reach a maximum value of 255 with smaller numbers since the child process now calculates the first half (1+...+n/2 ).

2.1 The reason is that the program tries to compute all of the processes at the same time without waiting for child processes to finish, so the children can never reach 5000 before exiting.

2.2 It would be 5000 since the program would have to run for at least 1 cycle at the bare minimum which would  increment till 5000.
