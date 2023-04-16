Lights.java


Created a new class to regulate the traffic lights independently. This class extends threads so we can simultaneously run it along the rest. First of all it runs forever just like regular lights and it alternates the green lights, starting with west first. Then while one side is green we start sending release signals as long as there is a car in que for that direction, and we sleep 1 in between to accommodate for later reacting drivers. Timer is 20 cycles of the code. It reduces the que by 1 every time the signal is sent. Then after the last one it waits 150 ms to accommodate for travelling car and does the exact same for the other side.


Car.java
Added the queueing up function with blocks. We have if the light is red or if there is a car in queue add to que ability and this adds a block signal to west (directional semaphore). Which can be signaled to be released through lights.java.