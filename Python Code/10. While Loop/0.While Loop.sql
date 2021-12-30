#                                    Loop Control Statements


Loop control statements are used when a section of code may either be executed a fixed number of times, or while some condition is true.
While
For


#                               while Loop


The while loop keeps repeating an action until an associated condition returns false.

Syntax:
	
	while (condition):               <----- Python Interpreter checks condition, If condition is True, then
	          Statement             <-----  Execute statements written after colon (:) 
	Rest of the Code



#                           while Loop with else



This repeatedly tests the condition and, if it is True, 
executes the Statement 1; if the condition is False (which may be the first time it is tested) 
the Statement 2 of the else clause, is executed and the loop terminates. The else suite will be always executed irrespective of the statements in the loop are executed or not. 

Syntax:
	while (condition):
	          Statement 1
	else:
	          Statement 2
	Rest of the Code



#                           Infinite while Loop


Syntax:
	while (True):
	          Statement
	Rest of the Code

	while (True):
	          Statement
	          if(condition): 
		    break
	Rest of the Code



#                          Nested While Loop


while(condition): 
	Statements
	while(condition):
		Statements
	Statements
Rest of Code
