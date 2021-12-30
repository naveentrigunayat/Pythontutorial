from abc import ABC, abstractmethod

class BaseEmployee(ABC):

    fname = ''
    lname = ''

    def getEmpName(self):
        print(self.fname + ' ' + self.lname)

    @abstractmethod
    def getBonus(self):
        pass


class PermanentEmployee(BaseEmployee):

    mName = ''
    monhtlySalary = 0    

    #overriding base class method
    #not complusory to override
    def getEmpName(self):
        print(self.fname + ' ' + self.mName + ' ' + self.lname)


    #overriding base class method
    #complusory to override
    def getBonus(self):
        print(self.monhtlySalary * 30)

    


class ContractEmployee(BaseEmployee):

    hourlySalary = 0

    #overriding base class method
    #complusory to override
    def getBonus(self):
        print(self.hourlySalary * 9 * 30)



p = PermanentEmployee()
p.fname = 'Sandeep'
p.lname = 'Trigunayat'
p.mName = 'R.'
p.monhtlySalary = 1000

#calling parent class's overriden method 
p.getEmpName()
#calling parent class's compulsory overriden method 
p.getBonus()

print('-------------')


c = ContractEmployee()
c.fname = 'Abhishek'
c.lname = 'Mishra'
c.hourlySalary = 50

#calling parent class's method
c.getEmpName()

#calling parent class's compulsory overriden method
c.getBonus()