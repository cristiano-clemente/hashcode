from sys import argv

#opening the input file
f_in = open(argv[1], 'r')
first_line = f_in.readline()

#setting the input variables
row_count, column_count, min_ingredient, max_area = tuple(map(int, first_line.split(' ')))

#creating the pizza grid and populating it
grid = []
for i in range(row_count):
	grid.append(f_in.readline().rstrip())
print(grid)

#closing the file
f_in.close()


f_out = open('d_big_temp.out','w+')
num_slices = 0

#for each row, i reset the counters
for r in range(row_count):
	beg = 0
	end = 0
	mushroom_count = 0
	tomato_count = 0

	#while i’m not at the end of the row, i count if i have a tomato or a mushroom
	while end < column_count:
		if grid[r][end] == 'M':
			mushroom_count += 1
		elif grid[r][end] == 'T':
			tomato_count += 1
		end += 1

		#if the slice is too big, i must remove an ingredient
		if end - beg > max_area:
			if grid[r][beg] == 'M':
				mushroom_count -= 1
			elif grid[r][beg] == 'T':
				tomato_count -= 1
			beg += 1

		#if we have a valid slice, we log in the results and reset the variables, in order to continue searching for new valid slices on the same line
		if (end - beg <= max_area
			and mushroom_count >= min_ingredient
			and tomato_count >= min_ingredient):
			f_out.write('%s %s %s %s\n' % (r, beg, r, end - 1))
			num_slices += 1
			beg = end
			tomato_count = 0
			mushroom_count = 0

with open('d_big_temp.out', 'r') as f_temp:
    with open('d_big.out', 'w+') as f_out:
        f_out.write(str(num_slices)+'\n')
        for line in f_temp:
            f_out.write(line)

f_out.close()
