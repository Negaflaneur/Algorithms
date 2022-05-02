##longest common sub-string 
# example : find the longest common sub-string between blue and clues
from pprint import pprint
import pandas as pd

word_1 = "blue"
word_2 = "clues"
print(word_1)
print (word_2)
grid = [[None] * (len(word_2) + 1) for i in range(len(word_1) + 1)]

for i in range(len(word_1) + 1):
    for j in range(len(word_2) + 1):
        if i == 0 or j == 0:
            grid[i][j] = 0
        elif word_1[i-1] == word_2[j-1]:
            grid[i][j] = grid[i-1][j-1] + 1
        else:
            grid[i][j] = max(grid[i][j-1], grid[i-1][j])

pprint(grid)
print("The length of word 1 is ", len(word_1))
print("The length of word 2 is ", len(word_2))
print("Longest common string is" , grid[len(word_1)][len(word_2)])