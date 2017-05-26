""" Initialize an n-by-m list of lists of empty strings using list multiplication, e.g. word_table = [[''] * n] * m. What happens when you set one of its values, e.g. word_table[1][2] = "hello"? Explain why this happens. Now write an expression using range() to construct a list of lists, and show that it does not have this problem."""
from tabulate import tabulate

n = 4
m = 5

word_table = [["test"]*n ]*m # each item at rank k within the sublists is a reference to the same string 

word_table2 = [[ "test" for i in range(n)] for j in range(m)] # will re-launch the inner loop and instanciate a different object for each cell of the matrix

print(word_table)
word_table[1][2] = "hell"
word_table2[1][2] = "hell"

print(tabulate(word_table))
print(tabulate(word_table2))

