#                                             Namespace


In Python, Namespace represents a memory block where names are mapped to objects.

Class Namespace – A class maintains it’s own namespace known as class namespace. In the class namespace, the names are mapped to class variables. 

Instance Namespace – Every instance have it’s own namespace known as instance namespace. 
In the instance namespace, the names are mapped to instance variables. 



class Mobile:
    fp = yes                            <----------------  Class Variable

realme = Mobile()
redmi = Mobile()
geek = Mobile()

Mobile.fp		# yes                     
realme.fp		# yes
redmi.fp		# yes
geek.fp		# yes



Mobile.fp	 = no
Mobile.fp		# no
realme.fp		# no
redmi.fp		# no
geek.fp		# no



realme.fp = Not Working
Mobile.fp		# no
realme.fp		# Not Working
redmi.fp		# no
geek.fp		# no




                           fp  ------>   no                              <-----------  Class Namespace 
                                     /   |    \
                                    /    |     \
                                   /     |      \
                                  /      |       \
                                 /       |        \
                            realme    redmi     geek                      <---------------  Instance Namespace
                               /
                              /
                        Not Working


