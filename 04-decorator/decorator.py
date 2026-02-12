def function_decorator(function):
    def function_wrapper():
        print("Inside the wrapper function")
        function()
        
    return function_wrapper

def function_test():
    print("Inside the test function")
    
# Add decorator as an instance of the function    
function_test = function_decorator(function_test)
function_test()

# Using the @ syntax to apply the decorator
@function_decorator
def function_test_2(): 
    print("Inside the test function 2")
    
function_test_2()