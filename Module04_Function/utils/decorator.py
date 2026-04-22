import time

def time_spent(func):
    def wrapper():

        # before.
        start = time.time_ns()

        func()

        # after.
        duration_ms = (time.time_ns() - start) // 1000
        print(f"function toke : {duration_ms}ms")


    return wrapper


@time_spent
def hello():
    print("my function")

hello()