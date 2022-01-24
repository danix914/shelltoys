from datetime import datetime


class ExecuteTime:
    EXECUTE_TIME_STR = '''******************
*** execute [{}] time: {}
******************'''

    def __init__(self, *sub):
        self.sub = sub

    def __call__(self, func):
        def exe_time(*args, **kargs):
            if self.sub:
                func_name = ' '.join(self.sub)
            else:
                func_name = func.__name__
            t1 = datetime.now()
            result = func(*args, **kargs)
            t2 = datetime.now()
            print(self.EXECUTE_TIME_STR.format(func_name, t2 - t1))
            return result
        return exe_time
