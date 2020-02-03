
input = open('input.txt')
output = open('output.txt', 'w+')


for line in input:
    line.rstrip('\n')
    state = line.split(',')
    status = state[1].replace('\n','')

    if status == 'Dirty':
        output.write('Suck\n')
    elif state[0] == 'A':
        output.write('Right\n')
    elif state[0] == 'B':
        output.write('Left\n')

input.close()
output.close()

