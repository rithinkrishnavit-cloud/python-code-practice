def my_decorator(func):
    def msg():
        print("before function")
        func()
        print("after function")

    return msg


@my_decorator
def hello():
    print("Hello")


hello()
