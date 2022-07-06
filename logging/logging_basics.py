import logging

#Logging levels
# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.


logging.basicConfig(filename='./logging/test.log',level=logging.INFO,format='%(asctime)s:%(levelname)s:%(message)s')


class Employees:

    def __init__(self,first,last):
        
        self.first=first
        self.last=last

        logging.info('Created employees: {} - {}'.format(self.fullname,self.email))

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)


emp1=Employees('Anmol','Arora')
emp2=Employees("Manisha","Dang")
