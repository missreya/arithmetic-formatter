def arithmetic_arranger(problems, answer_checker=False):
 import re

 from errors import errors 

 error_check_result = errors(problems)
 if error_check_result is not None:
     return error_check_result

 firstlist = list()
 secondlist = list()
 thirdlist = list()
 answerlist = list()

 for set in problems: #going by each problem
     set = set.replace(" ", "") #removes white spaces

     symbols = re.findall('[+-]', set) #this identifies if the symbol is a + or -
     symb = symbols[0]
        
     setsplit = set.split(symb) #splits into ("num", "num") by the "symb" 

     sortedset=sorted(setsplit, key=len) #find the length of the longest one
     longest = len(sortedset[-1]) #this will be used to figure out how much white space to use

     answer = str(eval(set))
     whitespace_ans = (longest+2-len(answer))*" "
     answerlist.append(whitespace_ans+answer)
    
     for i, num in enumerate(setsplit):
         if i == 0: 
             #this adds spaces for the first num of the set
            whitespace = (longest+2-len(num))*" "
            firstlist.append(whitespace+num)

         if i == 1:
             #this adds spaces for the second num of the set
            whitespace = (longest+1-len(num))*" "
            secondlist.append(symb+whitespace+num)
            thirdlist.append((longest+2)*"-")
                
 def stringing(mathline):
     mathstring=str()
     for i, items in enumerate(mathline):
        mathstring = mathstring + items 
        if i < (len(mathline)-1):
            mathstring = mathstring + "    "
     return(mathstring)

 if answer_checker == False:
     arranged_problems = stringing(firstlist)+"\n"+ stringing(secondlist) + "\n" + stringing(thirdlist)
     return arranged_problems
 elif answer_checker == True:
     arranged_problems = stringing(firstlist)+"\n"+ stringing(secondlist) + "\n" + stringing(thirdlist) + "\n" + stringing(answerlist)
     return arranged_problems
