package lab3;
// This file defines class "Synch".  This class contains all the semaphores
// and variables needed to coordinate the instances of the Reader and Writer
// classes.  

import java.util.concurrent.*;

public class Synch {

  public static Semaphore mutex;
  public static Semaphore wrt;
  public static Semaphore read;
  public static int writecount = 0;
  public static int readcount = 0;
  public static int activewritecount = 0;
  public static int activereadcount = 0;

}  // end of class "Synch"

