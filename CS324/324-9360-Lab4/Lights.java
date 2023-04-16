package lab4;

public class Lights extends Thread {
	
	public static int westlight = 0;
	public static int eastlight = 0;
	
	public void run () {
		Synch.timeSim.threadStart();
		
		
		while(1==1) {
			
			int timer = 0;
			Synch.mutex.acquire();
			
			westlight = 1;
			eastlight = 0;
			
			
			while (timer < 20) {
				
				
				if (Synch.westq > 0) {
					
					Synch.west.release();
					Synch.mutex.release();
					Synch.timeSim.doSleep(1);
					Synch.mutex.acquire();
					Synch.westq--;
					
					
				}
				
				timer++;
			}
			
			Synch.mutex.release();
			//waiting for last car to cross
			Synch.timeSim.doSleep(150);
			
			Synch.mutex.acquire();

			westlight = 0;
			eastlight = 1;
			
			
			
			timer = 0;
			
			while (timer < 20) {
				
				
				if (Synch.eastq > 0) {
					
					Synch.east.release();
					Synch.mutex.release();
					Synch.timeSim.doSleep(1);
					Synch.mutex.acquire();
					Synch.eastq--;		
					
					
				}
				
				
				
				timer++;
			}
		
			Synch.mutex.release();
			//waiting for last car
			Synch.timeSim.doSleep(100);
			
			
			
			
			
		}
	}
}
