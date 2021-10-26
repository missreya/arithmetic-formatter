import re 

###--------------- Error Statements ---------------###

def errors(error_test):
 
 if type(error_test) != list: 
     return "Error: Not a list."
 if len(error_test)> 5: 
     return "Error: Too many problems."

 for arith in error_test:
    if re.findall('[\*\/]+', arith): 
        return "Error: Operator must be '+' or '-'."
    elif re.findall('[a-zA-Z]+', arith): 
        return "Error: Numbers must only contain digits."
    elif re.findall('[\d][\d][\d][\d][\d]+', arith): 
        return "Error: Numbers cannot be more than four digits."
    elif type(arith) != str: 
        return "Error: Format must be in a string."