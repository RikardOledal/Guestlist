class ContextManager:
    '''Help me'''
    counter = 0
    def __init__(self, file_name):
        self.file_obj = open(file_name, "r")
    def __enter__(self):
        self.counter += 1
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()

class MyCounter:
    counter = 0

    @classmethod
    def get_num_of_usage(cls):
        return cls.counter
    
    def __enter__(self):
        self.counter += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing context, number of contexts is {self.counter}")
        return None

with MyCounter() as counter:
    print("Inside context manager suite.")
    print("Call context manager instance method to get countervalue:", counter.get_num_of_usage())
    print("Call context manager instance method to get countervalue:", counter.get_num_of_usage())

with MyCounter() as counter:
    print("Inside context manager suite.")
    print("Call context manager instance method to get countervalue:", counter.get_num_of_usage())