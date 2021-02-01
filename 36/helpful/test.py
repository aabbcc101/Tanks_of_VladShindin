#text_map2_2 = [1,2,3,4,[1,23,423],[3,23,32,13]]

b = [[char for char in range(5)] for row in range(9)]
print(dir(b))


#for j in range(len(b)):
    #for i in range(len(b[j])):
        #for k in range(len(b)):
            #print(i, end="")
        #print("\n")
    #print("\n")

text_map2_2 = [
    ['W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W'],
    ['W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W'],
    ['W','W','.','.','.','.','.','.','.','W','.','.','.','.','W','W'],
    ['W','W','.','.','.','.','.','W','.','W','.','.','.','.','W','W'],
    ['W','W','.','.','.','.','.','W','.','W','.','.','.','.','W','W'],
    ['W','W','.','.','.','.','.','.','.','.','.','.','.','.','W','W'],
    ['W','W','W','W','.','.','.','.','.','W','.','W','.','.','.','W'],
    ['W','W','W','W','.','W','.','W','W','W','W','.','W','W','W','W','mmmmmmmm'],
    ['W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W'],
    ['W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W'],
    ['W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W'],
    ['W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W']
    ]

for j in range(len(text_map2_2)):
    for i in range(len(text_map2_2[j])):
        print(text_map2_2[j][i], end="")
    print("")
print("\n")

empty = []
#for j in range(len(text_map2_2)):
for i in range(len(text_map2_2[0])):
    test = []
    for k in range(len(text_map2_2)):
        print(text_map2_2[k][i], end="")
        test.append(text_map2_2[k][i])
    print("")
    empty.append(test)
    
print('___________')
for i in empty:
    print(i)
    
    
    
    #print("\n") 
