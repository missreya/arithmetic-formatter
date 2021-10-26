# This entrypoint file to be used in development. Start by reading README.md

from pytest import main

from arithmetic_arranger import arithmetic_arranger


problems = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
print(arithmetic_arranger(problems))

problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
print(arithmetic_arranger(problems, True))

problems = ["32 * 8", "1 - 3801"]
print(arithmetic_arranger(problems))
#Returns Error: Operator must be '+' or '-'

problems = ["32 + 8", "12304 - 3801"]
print(arithmetic_arranger(problems, True))
#Returns Error: Numbers cannot be more than four digits. 

problems = ["32 + 8", "three + five"]
print(arithmetic_arranger(problems, True))
#Returns Error: Numbers must only contain digits.

# Run unit tests automatically
main()
