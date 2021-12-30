#                                   If Statement


It is used to execute an instruction or block of instructions only if a condition is fulfilled.
Syntax: -
	if (condition):                <------ First the condition is tested, If the condition is True
	      statement                <------ then the statements given after colon (:) are executed
	Rest of the Code

	if (condition):
	      statement1                  <------- Block of statement/ Group of statements/ Suite
	      statement2              <------- Block of statement/ Group of statements/ Suite
	Rest of the Code


If there is single statement it can be written in one line.
Ex:- if (condition): Statement



#                             Nested If Statement


Syntax :
	if (condition):
	       block of statements
	       if(condition):
	                 block of statements
	      if(condition):
	                 block of statements
	if(condition):
	      block of statements
	Rest of the code



#                          If Statement with Logical Operator


if ( (condition1) and (condition2) ):
	Statement
Rest of the Code

if ( (condition1) and (condition2) ):
	Block of Statements
Rest of the Code 

if ( (condition1) or (condition2) ):
	Statement
Rest of the Code



#                                 Indentation


Indentation refers to spaces that are used in the beginning of a statement. By default python puts 4 spaces but it can be changed by programmers.


if (condition):
____Statement
____if(condition):
________statement 1
________statement 2
____if(condition):
________Statement
if(condition):
____Statement 1
____Statement 2 
Rest of the code



#                                  If Else Statement

if… else statement is used when a different sequence of instructions is to be executed depending on the logical value(True/False) of the condition evaluated.
Syntax: - 


if(condition):
       Statement 1
else:
       Statement 2
Rest of the Code


if(condition):
         Statement 1
          Statement 2
else:
          Statement 3
          Statement 4
Rest of the Code



#                                    Nested If Else Statement

In nested if…. else statement, an entire if… else construct is written within either the body of the if statement or the body of an else statement.


if(condition_1):
           if(condition_2):
                        Statement 1
             else:
                       Statement 2
else:
          Statement 3
Rest of the Code


if(condition_1):
            if(condition_2):
	     Statement 1
             else:
	     Statement 2
else:
              if(condition_3):
	      Statement 3
               else:
	       Statement 4
Rest of the Code



#                                   if elif Statement


To show a multi-way decision based on several conditions, we use if elif statement.
if (condition_1):
         Statement 1
elif (condition_2):
        Statement 2
elif (condition_3):
        Statement 3
elif (condition_n):
       Statement n
Rest of the Code


#                                     if elif else Statement


To show a multi-way decision based on several conditions, we use if elif else statement.
if (condition_1):
         Statement 1
elif (condition_2):
        Statement 2
elif (condition_3):
        Statement 3
elif (condition_n):
       Statement n
else:
       Statements x
Rest of the Code





