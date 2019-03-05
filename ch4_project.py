spam = ['apple','bananas','tofu','cats']
def dot_print(spam):
  for i in range(len(spam)-1):
    print(spam[i],end=', ')
  print("and "+spam[-1])
#dot_print(spam)

grid = [[0, 1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 0, 0],
        [0, 1, 1, 0, 0, 0],]
def re_draw(grid):
  len_x = len(grid[0]) #6
  len_y = len(grid)    #7
  print(" x= {} y = {}".format(len_x,len_y))
  for i in range(len_x):
    for j in range(len_y):
      print(grid[j][i],end="")
    print("")
re_draw(grid)