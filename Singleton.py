"""
Concept : A class should have only single instance/object created in the entire lifecycle of an object
"""

class Singleton(type): # Using __call__ method
    """
    This is a metaclass, as you are inheriting from
    type class.
    Concept : 
    -> Every class which is inherting from type
    needs to be used as a metaclass.
    -> Metaclass actually creates a class(class object), as class 
    is also an object in Python
    """
    def __init__(cls, name, bases, namespace_attrs, **kwargs):
        """
        This method is used to initialize the class obj(cls/SingleObject)
        after it was created using __new__ method
        """
        # print "Actual class SingleObject is created and started initialization...."
        print("Actual class SingleObject is created and started initialization....")
        # super(type, cls).__init__(name, bases, namespace_attrs) # Python 2.x
        super().__init__(name, bases, namespace_attrs) # Python 3.x
        cls._instance = None
        # print "and the attributes of SingleObject class is {0} \n".format(dir(cls))
        print("and the attributes of SingleObject class is {0} \n".format(dir(cls)))


    def __call__(cls, *args, **kwargs):
        """
        cls -> SingleObject
        """
        # print "Creating the object of SingleObject class...."
        print("Creating the object of SingleObject class....")
        if not cls._instance:
            # Python 2.x
            # cls_instance = super(type, cls).__call__(*args, **kwargs) # SingleObject instance
            # Python 3.x
            cls_instance = super().__call__(*args, **kwargs) # SingleObject instance
            print(cls_instance, type(cls_instance) ,"\n")
            cls._instance = cls_instance
        return cls._instance


class SingleObject(metaclass=Singleton):
    # __metaclass__ = Singleton # Python 2.x
    pass

obj = SingleObject()

####################################################################################
class SingletonWay2(object): # Using __new__
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            print("Creating SingletonWay2 object/instance....")
            # cls._instance = super().__new__(cls, *args, **kwargs) # Python 3.x
            cls._instance = super(SingletonWay2, cls).__new__(cls, *args, **kwargs) # Python 2.x
            return cls._instance
        else:
            print("SingletonWay2 object/instance already exists...\n")
            return cls._instance

obj_new = SingletonWay2()
obj_new2 = SingletonWay2()

#####################################Limit the class count###########################################
class SingletonLimited(object):
    _object_count = 1
    _limit = 3

    def __new__(cls, *args, **kwargs):
        if cls._object_count > cls._limit:
            raise Exception("Maximum count reached....")
        # instance = super().__new__(cls, *args, **kwargs) # Python 3.x
        instance = super(SingletonLimited, cls).__new__(cls, *args, **kwargs) # Python 2.x
        print("Creating instance and count is {}".format(cls._object_count))
        cls._object_count += 1
        return instance

one = SingletonLimited()
two = SingletonLimited()
three = SingletonLimited()
four = SingletonLimited() # Should get error

