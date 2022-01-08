class MyCounter:
    counter = 0

    @classmethod
    def get_num_of_usage(cls):
        return cls.counter
    
    def __enter__(self):
        MyCounter.counter += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing context, number of contexts is {self.counter}")
        return None

with MyCounter() as counter:
    print("Inside context manager suite.")
    print("Call context manager instance method to get countervalue:", counter.get_num_of_usage())

with MyCounter() as counter:
    print("Inside context manager suite.")
    print("Call context manager instance method to get countervalue:", counter.get_num_of_usage())