# When to use class method and static methods?

class Item:
    @staticmethod
    def is_integer():
        '''
        Used in case of general func which is not
        related to the class
        '''
        pass

    @classmethod
    def instantiate(self):
        '''
        Should be something that is common to the class
        but not common to class instances, for example:
        instantiating a set of class instances from another
        file
        
        '''