from settings import *
import array

#text_map = [
    #'WWWWWWWWWWWW',
    #'W......W...W',
    #'W...WW...W.W',
    #'W.......WW.W',
    #'W..W....W..W',
    #'W..W...WWW.W',
    #'W....W.....W',
    #'WWW.WWWWWWWW',
    #'WWWWWW....WW',
    #'W..........W',
    #'W....W...W.W',
    #'W........W.W',
    #'W..W.......W',
    #'W..W...WWW.W',
    #'W..........W',
    #'WWWWWWWWWWWW'
#]

#world_map = set()
#for j, row in enumerate(text_map):
    #for i, char in enumerate(row):
        #if char == 'W':
            #world_map.add((i * TILE, j * TILE))


class World_map():
    def __init__(self):
       
        self.text_map2 = (
            ('W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W'),
            ('W','.','.','.','.','.','.','.','.','.','.','W','.','.','.','W'),
            ('W','.','.','.','.','.','.','.','.','W','.','W','.','.','.','W'),
            ('W','.','.','.','.','.','.','.','.','W','.','W','.','.','.','W'),
            ('W','.','.','W','.','.','.','.','W','.','.','W','.','.','.','W'),
            ('W','.','.','.','.','.','.','A','.','W','.','W','.','.','.','W'),
            ('W','.','.','.','.','W','.','.','.','.','.','W','.','.','.','W'),
            ('W','W','W','.','W','W','W','W','W','W','W','W','W','.','W','W'),
            ('W','W','W','.','W','W','.','.','.','.','W','W','.','.','.','W'),
            ('W','.','.','.','W','W','.','.','.','.','W','W','.','.','.','W'),
            ('W','.','.','.','.','.','.','.','.','.','.','.','.','.','.','W'),
            ('W','.','.','W','.','.','.','.','W','.','.','W','.','.','.','W'),
            ('W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W')
        ) 
        
        
        self.text_map2_ = [
            'WWWWWWWWWWWWWWWW',
            'WWWWWWWWWWWWWWWW',
            'WW.......W....WW',
            'WW.....W.W.A..WW',
            'WW.....W.W....WW',
            'WW......A.....WW',
            'WWWW.....W.W...W',
            'WWWW.W.WWWW.WWWW',
            'WWWWWWWWWWWWWWWW',
            'WWWWWWWWWWWWWWWW',
            'WWWWWWWWWWWWWWWW',
            'WWWWWWWWWWWWWWWW'
        ]  
                
        self.text_map3 = (
            ('W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W'),
            ('W','.','.','.','.','.','W','.','.','.','.','W','.','.','.','W'),
            ('W','.','.','.','.','.','W','.','.','W','.','W','.','.','.','W'),
            ('W','.','.','.','.','W','W','.','.','W','.','W','W','.','.','W'),
            ('W','.','.','W','.','.','.','.','.','W','W','.','.','.','.','W'),
            ('W','.','W','W','W','.','.','W','.','W','.','W','.','.','.','W'),
            ('W','.','.','.','.','W','.','.','.','.','.','W','.','.','.','W'),
            ('W','W','W','.','W','W','W','W','W','W','W','W','.','.','.','W'),
            ('W','W','W','.','W','W','.','.','.','.','.','.','.','.','W','W'),
            ('W','.','.','.','.','.','.','.','.','.','W','W','.','.','.','W'),
            ('W','.','.','.','.','.','.','.','.','.','.','.','.','.','.','W'),
            ('W','.','.','W','.','.','.','.','W','.','.','W','.','.','.','W'),
            ('W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W')
             
        ) 
        
        self.text_map4 = (
            ('W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W'),
            ('W','.','.','W','A','.','.','.','.','.','.','.','.','.','.','W'),
            ('W','.','.','W','W','W','W','W','.','W','.','.','.','.','.','W'),
            ('W','.','.','.','.','W','W','W','.','W','W','W','W','.','.','W'),
            ('W','.','.','W','W','W','.','.','.','.','.','.','.','.','.','W'),
            ('W','.','.','.','.','.','.','W','W','W','W','W','W','.','.','W'),
            ('W','.','.','.','.','.','.','W','.','.','.','.','.','.','.','W'),
            ('W','W','W','.','W','W','W','W','.','W','W','W','.','W','W','W'),
            ('W','W','W','W','W','W','.','.','.','.','W','W','W','W','W','W'),
            ('W','.','.','.','.','.','.','.','.','.','.','.','.','.','.','W'),
            ('W','.','.','.','.','W','.','.','.','W','.','.','.','.','.','W'),
            ('W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W')
             
        ) 
        
        self.text_map5 = (
            ('W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W'),
            ('W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W'),
            ('W','W','.','.','.','.','.','.','.','W','.','.','.','.','W','W'),
            ('W','W','.','.','W','.','.','W','.','W','.','.','.','.','W','W'),
            ('W','W','.','.','W','.','.','W','.','W','.','.','.','.','W','W'),
            ('W','W','.','.','W','.','.','.','.','W','.','.','.','.','W','W'),
            ('W','W','W','.','.','.','.','W','.','W','.','W','.','.','.','W'),
            ('W','W','W','W','.','W','.','W','.','W','W','.','W','.','W','W'),
            ('W','W','W','W','.','W','W','W','.','W','W','.','.','.','W','W'),
            ('W','W','W','W','.','W','W','W','.','W','W','.','W','W','W','W'),
            ('W','W','W','.','.','W','W','W','.','.','.','.','W','W','W','W'),
            ('W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W')             
        ) 

        
        self.text_map2_2 = [
            ['W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W'],
            ['W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W'],
            ['W','W','.','.','.','.','.','.','.','W','.','.','.','.','W','W'],
            ['W','W','.','.','.','.','.','W','.','W','.','.','.','.','W','W'],
            ['W','W','.','.','.','.','.','W','.','W','.','.','.','.','W','W'],
            ['W','W','.','.','.','.','.','.','.','.','.','.','.','.','W','W'],
            ['W','W','W','W','.','.','.','.','.','W','.','W','.','.','.','W'],
            ['W','W','W','W','.','W','.','W','W','W','W','.','W','W','W','W'],
            ['W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W'],
            ['W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W'],
            ['W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W'],
            ['W','W','W','W','W','W','W','W','W','W','W','W','W','W','W','W']
            ]

        
        self.space = 0
        self.world_map  = set()
        self.world_map_list = []
        self.world_map_left_to_right = []
        self.aid_list = []
        #self.world_map_list = array.array('')
        self.create_map()



    def create_map(self): #MUCH MORE FASTER'
        self.aid_list = []
        self.world_map_list = []
        for j, row in enumerate(self.text_map2_):
            temp = []
            for i, char in enumerate(row):
                self.space +=1
                if char == 'W':
                    temp.append((i * TILE,j * TILE))
                elif char == 'A':
                    self.aid_list.append([i * TILE,j * TILE])
            temp = tuple(temp)
            self.world_map_list.append(temp)
        self.world_map_list = tuple(self.world_map_list)
        self.world_map = self.world_map_list

        string_of_array = []
        
        for i in range(len(self.text_map2_2[0])):
            temp = []
            for k in range(len(self.text_map2_2)):
                #print(self.text_map2_2[k][i], end="")
                if self.text_map2_2[k][i] == 'W':
                    temp.append((k * TILE, i * TILE))
                    #print(self.text_map2_2[k][i], end="")
            temp = tuple(temp)
            string_of_array.append(temp)
        string_of_array = tuple(string_of_array)
        self.world_map_left_to_right = string_of_array      
        
        #for a in range(len(self.aid)):
            #print(self.aid[a][0])


    def level_2_world_map(self):
        self.space = 0
        self.aid_list = []
        self.world_map_list = []
        for j in range(len(self.text_map2)):
            temp = []
            for i in range(len(self.text_map2[j])):
                self.space +=1
                if self.text_map2[j][i] == 'W':
                    temp.append((i * TILE,j * TILE))
                elif self.text_map2[j][i] == 'A':
                    self.aid_list.append((i * TILE,j * TILE))
            temp = tuple(temp)
            self.world_map_list.append(temp)
        self.world_map_list = tuple(self.world_map_list)
        self.world_map = self.world_map_list

        string_of_array = []
        
        for i in range(len(self.text_map2[0])):
            temp = []
            for k in range(len(self.text_map2)):
                if self.text_map2[k][i] == 'W':
                    temp.append((k * TILE, i * TILE))
            temp = tuple(temp)
            string_of_array.append(temp)
        string_of_array = tuple(string_of_array)
        self.world_map_left_to_right = string_of_array 
    
    def level_3_world_map(self):
        self.space = 0
        self.aid_list = []
        
        self.world_map_list = []
        for j in range(len(self.text_map3)):
            temp = []
            for i in range(len(self.text_map3[j])):
                self.space +=1
                if self.text_map3[j][i] == 'W':
                    temp.append((i * TILE,j * TILE))
                elif self.text_map3[j][i] == 'A':
                    self.aid_list.append((i * TILE,j * TILE))
            temp = tuple(temp)
            self.world_map_list.append(temp)
        self.world_map_list = tuple(self.world_map_list)
        self.world_map = self.world_map_list

        string_of_array = []
        
        for i in range(len(self.text_map3[0])):
            temp = []
            for k in range(len(self.text_map3)):
                if self.text_map3[k][i] == 'W':
                    temp.append((k * TILE, i * TILE))
            temp = tuple(temp)
            string_of_array.append(temp)
        string_of_array = tuple(string_of_array)
        self.world_map_left_to_right = string_of_array 
                    
    def level_4_world_map(self):
        self.space = 0
        self.aid_list = []
        self.world_map_list = []
        for j in range(len(self.text_map4)):
            temp = []
            for i in range(len(self.text_map4[j])):
                self.space +=1
                if self.text_map4[j][i] == 'W':
                    temp.append((i * TILE,j * TILE))
                elif self.text_map4[j][i] == 'A':
                    self.aid_list.append((i * TILE,j * TILE))
            temp = tuple(temp)
            self.world_map_list.append(temp)
        self.world_map_list = tuple(self.world_map_list)
        self.world_map = self.world_map_list

        string_of_array = []
        
        for i in range(len(self.text_map4[0])):
            temp = []
            for k in range(len(self.text_map4)):
                if self.text_map4[k][i] == 'W':
                    temp.append((k * TILE, i * TILE))
            temp = tuple(temp)
            string_of_array.append(temp)
        string_of_array = tuple(string_of_array)
        self.world_map_left_to_right = string_of_array 
                    
    def level_5_world_map(self):
        self.space = 0
    
        self.aid_list = []
        self.world_map_list = []
        for j in range(len(self.text_map5)):
            temp = []
            for i in range(len(self.text_map5[j])):
                self.space +=1
                if self.text_map5[j][i] == 'W':
                    temp.append((i * TILE,j * TILE))
                elif self.text_map5[j][i] == 'A':
                    self.aid_list.append((i * TILE,j * TILE))
            temp = tuple(temp)
            self.world_map_list.append(temp)
        self.world_map_list = tuple(self.world_map_list)
        self.world_map = self.world_map_list

        string_of_array = []
        
        for i in range(len(self.text_map5[0])):
            temp = []
            for k in range(len(self.text_map5)):
                if self.text_map5[k][i] == 'W':
                    temp.append((k * TILE, i * TILE))
            temp = tuple(temp)
            string_of_array.append(temp)
        string_of_array = tuple(string_of_array)
        self.world_map_left_to_right = string_of_array 
