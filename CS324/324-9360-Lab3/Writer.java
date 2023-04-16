package lab3;
// This file defines class "writer".

// This code uses
//      class Semaphore, from the java.util.concurrent package in Java 5.0 which defines the behaviour of a 
//                           semaphore, including acquire and release operations.
//      class Synch, which defines the semaphores and variables
//                   needed for synchronizing the readers and writers.
//      class RandomSleep, which defines the doSleep method.


public class Writer extends Thread {
  int myName;  // The variable myName stores the name of this thread.
               // It is initialized in the constructor for class Reader.

  RandomSleep rSleep;  // rSleep can hold an instance of class RandomSleep.



  // This is the constructor for class Writer.  It has an integer parameter,
  // which is the name that is given to this thread.
  public Writer(int name) {
    myName = name;  // copy the parameter value to local variable "MyName"
    rSleep = new RandomSleep();   // Create and instance of RandomSleep.
  }  // end of the constructor for class "Writer"



  public void run () {
    for (int I = 0;  I < 5; I++) {

      // Get permission to write
      System.out.println("Writer " + myName + " wants to write");
      try{
        Synch.mutex.acquire();
      }
      catch(Exception e){}
      
      if(Synch.activereadcount > 0 || Synch.activewritecount > 0) {
        Synch.writecount++;
      }else {
        Synch.activewritecount++;
        Synch.wrt.release();
      }
      
      
      try{
          Synch.wrt.acquire();
      }catch(Exception e){} 
      
      
      
      // Simulate the time taken by writing.
      System.out.println("Writer " + myName + " is now writing");
      rSleep.doSleep(1, 200);
      System.out.println("Writer " + myName + " is done writing");
      
      Synch.activewritecount--;
      
      if(Synch.writecount > 0) {
        Synch.activewritecount++;
        Synch.writecount--;
        Synch.wrt.release();
      } else if (Synch.readcount > 0) {
        while(Synch.readcount > 0) {
          Synch.activereadcount++;
          Synch.readcount--;
          Synch.read.release();
        }
      }
      
      Synch.mutex.release();

      // Simulate "doing something else"
      rSleep.doSleep(1, 1000);
    } // end of "for" loop
  }  // end of "run" method
}  // end of class "Writer"

