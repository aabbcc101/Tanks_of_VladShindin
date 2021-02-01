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
        self.text_map = [
            'WWWWWWWWWWWW',
            'W......W...W',
            'W...WW...W.W',
            'W.......WW.W',
            'W..W....W..W',
            'W..W...WWW.W',
            'W....W.....W',
            'WWW.WWWWWWWW',
            'WWWWWW....WW',
            'W..........W',
            'W....W...W.W',
            'W........W.W',
            'W..W.......W',
            'W..W...WWW.W',
            'W..........W',
            'WWWWWWWWWWWW'
        ]

        self.text_map2 = [
            'WWWWWWWWWWWWWWWW',
            'W..........W...W',
            'W........W.W...W',
            'W........W.W...W',
            'W..W....W..W...W',
            'W........W.W...W',
            'W....W.....W...W',
            'WWW.WWWWWWWWW.WW',
            'WWW.WW....WW...W',
            'W..............W',
            'W....W...W.W...W',
            'WWWWWWWWWWWWWWWW',
            'W..W.......W',
            'W..W...WWW.W',
            'W..........W',
            'WWWWWWWWWWWW'
        ]   
        
        self.text_map2_ = [
            'WWWWWWWWWWWWWWWW',
            'WWWWWWWWWWWWWWWW',
            'WW.......W....WW',
            'WW.....W.W....WW',
            'WW.....W.W....WW',
            'WW............WW',
            'WWWW.....W.W...W',
            'WWWW.W.WWWW.WWWW',
            'WWWWWWWWWWWWWWWW',
            'WWWWWWWWWWWWWWWW',
            'WWWWWWWWWWWWWWWW',
            'WWWWWWWWWWWWWWWW'#,
            #'WWW.WW....WW...W',
            #'W..............W',
            #'W....W...W.W...W',
            #'WWWWWWWWWWWWWWWW',
            #'W..W.......W',
            #'W..W...WWW.W',
            #'W..........W',
            #'WWWWWWWWWWWW'
        ]  
                
        self.text_map3 = [
            'WWWWWWWWWWWWWWWW',
            'W.....W....W...W',
            'W.....W..W.W...W',
            'W....WW..W.WW..W',
            'W..W.....WW....W',
            'W.WWW..w.W.W...W',
            'W....W.....W...W',
            'WWW.WWWWWWWW...W',
            'WWW.WW........WW',
            'W.........WW...W',
            'W....W...W.....W',
            'WWWWWWWWWWWWWWWW',
            'W..W.......W',
            'W..W...WWW.W',
            'W..........W',
            'WWWWWWWWWWWW'
        ]  
        
        self.text_map4 = [
            'WWWWWWWWWWWWWWWW',
            'W..W...........W',
            'W..WWWWW.W.....W',
            'W....WWW.WWW...W',
            'W..WWW.........W',
            'W......WWWWW...W',
            'W......W.......W',
            'WWW.WWWW.WWW.WWW',
            'WWWWWW....WWWWWW',
            'W..............W',
            'W....W...W.....W',
            'WWWWWWWWWWWWWWWW',
            'W..W.......W',
            'W..W...WWW.W',
            'W..........W',
            'WWWWWWWWWWWW'
        ]
        
        self.text_map5 = [
            'WWWWWWWWWWWWWWWW',
            'WWWWWWWWWWWWWWWW',
            'WW.......W....WW',
            'WW..W..W.W....WW',
            'WW..W..W.W....WW',
            'WW..W....W....WW',
            'WWW......W.W...W',
            'WWWW.W.W.WW.W.WW',
            'WWWW.WWW.WW...WW',
            'WWW..WWW.WW.WWWW',
            'WWWW.WWW....WWWW',
            'WWWWWWWWWWWWWWWW'#,
            #'WWW.WW....WW...W',
            #'W..............W',
            #'W....W...W.W...W',
            #'WWWWWWWWWWWWWWWW',
            #'W..W.......W',
            #'W..W...WWW.W',
            #'W..........W',
            #'WWWWWWWWWWWW'
        ]  
        
        self.space = 0
        
        self.world_map  = set()
        self.create_map()

    def create_map(self): #MUCH MORE FASTER
        world_map = []
        for j, row in enumerate(self.text_map2_):
            for i, char in enumerate(row):
                self.space +=1
                if char == 'W':
                    world_map.append((i * TILE, j * TILE))
        temp = tuple(world_map)
        self.world_map = temp
        #for i in temp:
            

            
    def create_map1(self): # SLOWLY
        self.world_map = set()
        for j, row in enumerate(self.text_map2_):
            for i, char in enumerate(row):
                self.space +=1
                if char == 'W':
                    self.world_map.add((i * TILE, j * TILE))
                #elif char == '.':
                    #self.space +=1

    def level_2_world_map(self):
        self.world_map = []
        for j, row in enumerate(self.text_map2):
            for i, char in enumerate(row):
                self.space +=1
                if char == 'W':
                    self.world_map.append((i * TILE, j * TILE))
        temp = tuple(self.world_map)
        self.world_map = temp
    
    def level_3_world_map(self):
        self.world_map = set()
        for j, row in enumerate(self.text_map3):
            for i, char in enumerate(row):
                self.space +=1
                if char == 'W':
                    self.world_map.add((i * TILE, j * TILE))
                    
    def level_4_world_map(self):
        world_map = []
        for j, row in enumerate(self.text_map4):
            for i, char in enumerate(row):
                self.space +=1
                if char == 'W':
                    world_map.append((i * TILE, j * TILE))
        temp = tuple(world_map)
        self.world_map = temp        
                    
    def level_5_world_map(self):
        world_map = []
        for j, row in enumerate(self.text_map5):
            for i, char in enumerate(row):
                self.space +=1
                if char == 'W':
                    world_map.append((i * TILE, j * TILE))
        temp = tuple(world_map)
        self.world_map = temp
