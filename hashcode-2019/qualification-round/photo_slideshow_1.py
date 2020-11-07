from sys import argv

with open(str(argv[1])+'.txt', 'r') as f_in:
    photo_count = int(f_in.readline())
    all = []
    vert = []
    i = 0
    for i in range(photo_count):
        photo = f_in.readline().rstrip().split(" ")
        if photo[0] == "H":
            all.append([int(photo[1]), [x for x in photo[2:]], (i,)])
        else:
            vert.append([int(photo[1]), [x for x in photo[2:]], (i,)])
        i += 1
f_in.close()

while len(vert) > 1:
    max_tags, id = 0, 0
    for i in range(1, len(vert)):
        union = list(set(vert[0][1]+vert[id][1]))
        num_tags = len(union)
        if num_tags > max_tags:
            max_tags = num_tags
            id = i
    all.append([max_tags, union, (vert[0][2][0], vert[id][2][0])])
    vert.pop(id)
    vert.pop(0)

not_chosen = list(range(len(all)))

# [num_tags, [tags], (id0,id1)]
tags = {}
for i in range(len(all)):
    for tag in all[i][1]:
        if tag not in tags:
            tags[tag] = (i,)
        else:
            tags[tag] += (i,)

def score(i0, i1):
    x = len(set(all[i0][1]) & set(all[i1][1]))
    y = len(set(all[i0][1]) - set(all[i1][1]))
    z = len(set(all[i1][1]) - set(all[i0][1]))
    return min(x, y, z)

def write_out(i):
    if len(all[i][2]) == 1:
        f_out.write('%d\n' % (all[i][2][0]))
    else:
        f_out.write('%d %d\n' % (all[i][2][0], all[i][2][1]))

f_out = open(str(argv[1])+'.out', 'w+')
f_out.write(str(len(all))+'\n')

write_out(0)
not_chosen.remove(0)

#not_chosen = [0,1,2,3,4,5,...]
curr_i = 0
for i in range(1,len(all)-1): #len(all)-2 times
    max_score, winner_i, = 0, 0
    temp = (curr_i,)
    for tag in all[curr_i][1]:
        for tg_i in tags[tag]:
            if (tg_i not in temp) and (tg_i in not_chosen):
                temp += (tg_i,)
                curr_score = score(curr_i, tg_i)
                if curr_score >= max_score:
                    max_score = curr_score
                    winner_i = tg_i
    if winner_i == 0: #winner not found
        winner_i = not_chosen[0]
    write_out(winner_i)
    not_chosen.remove(winner_i)
    curr_i = winner_i

write_out(not_chosen[0])

f_out.close()
