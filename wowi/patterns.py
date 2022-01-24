class Singleton(type):
    """implement class for Singleton pattern
    declear metaclass as Singleton for the class you wanna be the only one object
    e.q.:
        class IWasTheOne(metaclass=Singleton)
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
