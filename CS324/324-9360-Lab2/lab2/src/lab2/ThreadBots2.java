package lab2;

public class ThreadBots2
{

	int Identity; //This integer variable will be the thread identifier
    char init_char;//This character will be used by each thread as the first letter in the password
    char[] alph = {'a', 'b' , 'c' , 'd' , 'e' , 'f' , 'g' , 'h' , 'i' , 'j' , 'k' , 'l' , 'm' , 'n' , 'o' , 'p' , 'q' , 'r' , 's' , 't' , 'u' , 'v' , 'w' , 'x' , 'y' ,'z'};
	//Here we redefine the default constructor of this class.
	//By default it has no arguments, but in this example
	//We are using two arguments
	public ThreadBots2(int id, char c) 
	{
		//Here we retrieve the value of the identity passed by the main class
		Identity = id;
		//Here we retrieve the value of the character passed by the main class
		init_char = c;
	}
	
	public int main()
	{	
		//Here is where you write the code that should crack the password
		for (int i = 0; i < 26; i++)
		{
			char letter1 = alph[i];
		
			for(int j = 0; j < 26; j++)
			{
				char letter2 = alph[j];
		
				for(int k = 0; k < 26; k++)
				{
					char letter3 =  alph[k];
		
					for(int l = 0; l < 26; l++) 
					{
						char letter4 = alph[l];
		
						String finalString  = "" + init_char + letter1 + letter2 + letter3 + letter4 + ThreadAttacker.challenge;
						if(ThreadAttacker.captured == finalString.hashCode()) 
						{
							ThreadAttacker.found = true;
							System.out.println("Solved By: " + Integer.toString(Identity));
							System.out.println(System.currentTimeMillis() - ThreadAttacker.startTime + "ms");
							return 1;
						}
					}
				}
		
			}
		
		
		}
		return 1;
	}
}
