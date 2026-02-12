#Function
def function(param1:int, param2:int) -> int: 
    return param1 + param2

#Function as first class
def function_first_class():
    return

variable = function_first_class()
function_first_class()

#Function nested
def principal_function():
    name = "Jane"
    
    def function_nested():
        print(name)
        
    function_nested()
    
#Function of order superior (closure)
def greet():
    message = "Hello, World!"
    
    def print_message():
        print(message)
    
    return print_message