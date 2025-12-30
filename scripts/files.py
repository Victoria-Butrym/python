# 'w' - write
# 'a' - append
# 'r' - read
# 
# file = open('data/text.txt', 'w')

# file.write('kuku zdorova')
# file.write('!!')

# file.close()





# data = input('Enter your text: \n')

# file = open('data/input.txt', 'a')
# file.write(data + '\n')

# file.close()





file = open('data/input.txt', 'r')

# print(file.read())
# print(file.read(4))

for line in file:
    print(line)

file.close()
