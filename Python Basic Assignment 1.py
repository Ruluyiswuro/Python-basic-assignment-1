#!/usr/bin/env python
# coding: utf-8

# # 1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
# 
# *,'hello', -87.8,-,/,+,6
# 
# Ans :   *, -, +, / are expressions and 'hello', -87.8, 6 are values.

# # 2. What is the difference between string and variable?
# Ans: A Variable is used to store of information, a variable is created the moment you first assign a value to it.
#          Example: x = 5, y = "John". Here x and y are variables.
#     A String is a group of characters or a single character usually enclosed in Double quotes " " or single quotes ' '. Even triple quotes can be used in Python but generally used to represent multiline strings and docstrings. Example: my_string = 'Hello'

# # 3. Describe three different Data Types ?
# Ans: Three fundamental Data types in python are int, float, complex.
#     1. int data type: We can use int data type to represent whole numbers (integral values).
#     2. float data type: We can use float data type to represent floating point values (decimal values).
#     3. complex data type: Complex number is represented by complex class. It is specified as (real part) + (imaginary part)j.

# # 4. What is an expression made up of? What do all expressions do?
# Ans : An expression is a combination of operators and operands that is interpreted to produce some other value. In any programming language, an expression is evaluated as per the precedence of its operators. So that if there is more than one operator in an expression, their precedence decides which operation will be performed first. The interpreter evaluates the expression and displays the result.

# In[1]:


4*4+50-20 #is ab expression and python interpreter evaluates the expression to be 46.


# # 5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?
# Ans : An expression is a combination of operators and operands that is interpreted to produce some other value. An expression is evaluated as per the precedence of its operators. So that if there is more than one operator in an expression, their precedence decides which operation will be performed first.
#     A statement is a unit of code that has an effect, like creating a variable or displaying a value.When we type a statement, the interpreter executes it, which means that it does whatever the statement says. In general, statements don’t have values. A statement is an instruction that a Python interpreter can execute. There are mainly four types of statements in Python, Print statements, Assignment statements, Conditional statements and Looping statements.

# # 6. After running the following code, what does the variable bacon contain?
# bacon = 22
# 
# bacon + 1
# 
# Ans : The variable bacon is set to 22 .The expression bacon + 1 does not reassign the value in bacon (that would be the case if the expression is like bacon = bacon + 1 instead of bacon + 1)

# In[2]:


#Example 1
bacon = 22
bacon + 1
print(bacon)


# In[3]:


#Example 2
bacon = 22
bacon = 22+1
print(bacon)


# # 7. What should the values of the following two terms be?
# 
# 'spam' + 'spamspam'
# 
# 'spam' * 3
# 
# Ans: Both expressions evaluate to the string 'spamspamspam' Where as the first expression follows String Concatentation and the second expression follows String Multiplication

# In[4]:


print('spam'+'spamspam') #string concatenation
print('spam'*3) #string multiplication


# # 8. Why is eggs a valid variable name while 100 is invalid?
# Ans: As per python,Variable names cannot begin with a number. The python rules for naming a variable are :-
# 
# Variable name must start with a letter or the underscore character.
# Variable name cannot start with a number.
# Variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, & _ ).
# Variable names are case-sensitive (name, INEURON and ineuron are three different variables).
# The reserved words(keywords) cannot be used naming the variable.

# In[5]:


egg='Ineuron' # Valid variable Initialization
100='hello' # Invalid Variable Initialization
print(egg) #prints the value of egg i.e. Ineuron
print(100) # Raises a Syntax Error as 100 is not a valid variable name


# # 9.What three functions can be used to get the integer,floating-point number,or string version of a value?
# Ans : The int(),float(),and str() functions can be used to get the integer,floating-point number,string version of the value passed to them.

# # 10. Why does this expression cause an error? How can you fix it?
# 

# In[6]:


'I have eaten ' + 99 + ' burritos.'


# Ans : The cause of the error is 99. As 99 is not a string, it caused TypeError and must be converted to a string to fix the error.

# In[8]:


#Example : 
print('I have eaten ' + str(99) + ' burritos')


# In[ ]:




