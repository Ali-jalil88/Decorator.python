def mydecorator(func):
    """
    This decorator adds functionality to print messages before and after the 
    execution of the wrapped function.
    
    Args:
    func (function): The function to be wrapped by the decorator.
    
    Returns:
    function: The wrapped function with added behavior.
    """

    def wrapper_function():
        print("Start : 1")
        func()
        print("finish : mydecorator ")
    return wrapper_function
def mydecorator2(func):

    """
    This decorator adds functionality to print messages before and after the 
    execution of the wrapped function.
    
    Args:
    func (function): The function to be wrapped by the decorator.
    
    Returns:
    function: The wrapped function with added behavior.
    """
    def wrapper_function():
        print("Start : 3")
        func()
        print("finish : mydecorator2 ")
    return wrapper_function

@mydecorator
@mydecorator2
def hello():
    """
    A simple function that prints a test message.
    """
    print("Done : test in mydecorator2 ")

print(hello())
