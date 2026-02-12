date = "01-01-2000"

def function_scope_local():
    #Scope local
    name = "John"
    return name

def principal_function():
    name = "Jane"
    
    def function_nested():
        print(name)
        
    function_nested()
    
principal_function()


def closure():
    message = "Hello, World!"
    
    def print_message(): 
        print(message)
        
    return print_message

closure_function = closure()
closure_function() # Output: Hello, World!