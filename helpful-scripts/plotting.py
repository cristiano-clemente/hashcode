import matplotlib.pyplot as plt

with open('NAME_OF_INPUT_FILE_GOES_HERE.in', 'r') as f_in:
    #setting the input variables
    first_line = f_in.readline()
    row_count, column_count, var3, var4 = [int(x) for x in first_line.split()]

    #grid is of type [[],[],[],...]
    grid = []
    for i in range(row_count):
        new_line = f_in.readline().rstrip()
        #new_line = new_line.replace('T','1')
        #new_line = list(new_line)
        #new_line = [int(x) for x in new_line]
        #print(new_line)
        grid.append(new_line)

#plotting
plt.imshow(grid)
plt.show()
