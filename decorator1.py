def sum_decorator(func):
    def wrapper_function(x,y):
        print("Start : 1")
        result =func(x,y)
        print("Finish  : sum_decorator")
        return f" {result} \n {"sum_decorator :"} ( {"4 + 2 "} ) = {x+y}" 
    return wrapper_function

def minus_decorator(func):
    def wrapper_function(x,y):
        print("Start : 3")
        result =func(x,y) 
        print("Finish : minus_decorator")
        return f" {result} \n {"minus_decorator :"} ( {"4 - 2 "} ) = {x-y}" 
    return wrapper_function

def multi_decorator(func):
    def wrapper_function(x,y):
        print("Start : 5")
        result =func(x,y)
        print("Finish  : multi_decorator")
        return f" {result} \n {"multi_decorator :"} ( {"4 * 2 "} ) = {x*y}" 

    return wrapper_function

def divi_decorator(func):
    def wrapper_function(x,y):
        print("Start : 7")
        result = func(x,y)
        print("Finish  : divi_decorator")
        return f" {result} \n {"divi_decorator :"} ( {"4 / 2 "} ) = {x/y}" 

    return wrapper_function

@sum_decorator
@minus_decorator
@multi_decorator
@divi_decorator
def condition_use_decorator(x,y):
    if x >= 0 and y >= 0 :
        return "Done : test "
    else :
        return "Problem : test "
    
@sum_decorator
@minus_decorator
def condition1_use_decorator(x,y):
    if x >= 0 and y >= 0 :
        return "Done : test "
    else :
        return "Problem : test "

print(condition_use_decorator(4,2))
print("---------------------------")
print(condition_use_decorator(4,-2))
print("---------------------------")
print(condition1_use_decorator(5,2))