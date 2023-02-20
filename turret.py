import time
import json

class Turret:
    def __init__(self):#,nick):
        #self.nickname = 'nick' #json
        #self.id_number = 'MFT0001' #json
        #self.status = 'ready' #json
        #self.power = 'on' #json
        # search and attack, warning, shutdown, noshoot, on, broken
        #self.status_degree = [0,0]
        
        #self.__degree_x = 0 
        #self.degree_z = 0
        #self.whereabout = (0,0,0, '') 
        
        #self.armed_granade = True
        #self.armed = True
        
        
        #temporaty 
        self.trigger = False 
        self.trigger_granade = False
        
        self.steps_of_degrees = 5
        
        self.it_has_magazines = 2
        self.bullets_in_a_magazine = 10
        self.bullets = self.bullets_in_a_magazine
        self.count_shoots = 0
        
        self.it_has_magazines_of_granades = 4
        self.granades_in_a_magazine = 2
        self.granades = self.granades_in_a_magazine

        
        with open('turret.json') as f:
           self.nickname =  json.loads(f.readline())
           self.id_number =  json.loads(f.readline())
           self.status =  json.loads(f.readline())
           self.power =  json.loads(f.readline())        
           self.__degree_x =  json.loads(f.readline())
           self.degree_z =  json.loads(f.readline())
           self.whereabout =  json.loads(f.readline())
                     
    def write_to_json(self):
        with open('turret.json','w') as f:
            f.write(json.dumps(self.nickname)+'\n')
            f.write(json.dumps(self.id_number)+'\n')
            f.write(json.dumps(self.status)+'\n')
            f.write(json.dumps(self.power)+'\n')
            f.write(json.dumps(self.__degree_x)+'\n')
            f.write(json.dumps(self.degree_z)+'\n')
            #f.write(json.dumps(self.armed_granade)+'\n')
            #f.write(json.dumps(self.armed)+'\n')
            f.write(json.dumps(self.whereabout)+'\n')
        pass
        
    def name(self):
        print(f'ID = {self.id_number}')
        print(f'name = {self.nickname}')
        
#you can set and show the location
    def set_location(self):
        self.whereabout = (int(input("x=")),
                           int(input("y=")),
                           int(input('z=')),
                           input('use words = '))
    
    def get_location(self):
        print(f'the whereabout = {self.whereabout}')
                           

#set degrees
    def set_degrees(self, x, z):
        if self.check_x_y(x,z) == False:
            print('I have found an error')
        else:
            self.__degree_x = x
            self.degree_z = z
        
 #get dergees
    def degrees(self):
        print(f'self.degree_x = {self.__degree_x}')
        print(f'self.degree_z = {self.degree_z}') 
    
# it used for a movement
    def move(self, direction):
        #print('direction')
        if direction == 'left':
            self.__degree_x -=1
        if direction == 'right':
            self.__degree_x +=1
        if direction == 'down':
            self.degree_z -=1
        if direction == 'up':
            self.degree_z +=1
        pass
   
#checking for wrong asignment 
    def check_x_y(self,goal_x, goal_z):
        min_z = 0
        max_z = 180
        # checking Z wrong or not
        if goal_z < min_z:
            print("error z < 0")
            return False
        elif goal_z > max_z:
            print("error z > 180")
            return False

        max_x = 360
        min_x = 0
        # checking X wrong or not
        if goal_x < min_x:
            print("error x < 0")
            return False
        elif goal_x > max_x:
            print("error x > 360")
            return False
        return True
    
    #go to the goal
    def move_to_the_degree(self, goal_x, goal_z):
        #checking for wrong asignment
        self.check_x_y(goal_x, goal_z)
            
        #movement to the small side along X
        max_x = 360
        min_x = 0
        if self.__degree_x < goal_x:
            left = self.__degree_x - goal_x + 360
            right = -self.__degree_x + goal_x
            print(f'x_status = {self.__degree_x }')
            print(f'left = {left} and right ==== {right}')
            if right < left:
                print("plus")
                side = "plus"
            elif left <= right:
                print("minus")
                side = "minus"
        if self.__degree_x > goal_x:
            left = self.__degree_x - goal_x
            right = max_x - self.__degree_x + goal_x
            print(f'x_status = {self.__degree_x }')
            print(f'left = {left} and right = {right}')
            if right < left:
                print("plus")
                side = "plus"
            elif left <= right:
                print("minus")
                side = "minus"
        
        # do it until reach goals
        while (self.__degree_x != goal_x) or (self.degree_z != goal_z):
            if self.__degree_x == goal_x:
                pass
            else:
                if side == 'plus':
                    self.__degree_x += self.steps_of_degrees
                elif side == 'minus':
                    self.__degree_x -= self.steps_of_degrees
                if self.__degree_x == 360:
                    self.__degree_x = 0
            if self.degree_z == goal_z:
                pass
            else:   
                if self.degree_z > goal_z:
                    #move('down')
                    self.degree_z -= self.steps_of_degrees
                elif self.degree_z < goal_z:
                    #move('up')   
                    self.degree_z += self.steps_of_degrees
            # show me what you got
            self.degrees()
            
# set X value
    def func(self, goal_x):
        #movement to the small side
        max_x = 360
        min_x = 0
        if self.__degree_x < goal_x:
            left = self.__degree_x - goal_x + 360
            right = -self.__degree_x + goal_x
            print(f'x_status = {self.__degree_x }')
            print(f'left = {left} and right ==== {right}')
            if right < left:
                print("plus")
                side = "plus"
                #return side, right
            elif left <= right:
                print("minus")
                side = "minus"
        if self.__degree_x > goal_x:
            left = self.__degree_x - goal_x
            right = max_x - self.__degree_x + goal_x
            print(f'x_status = {self.__degree_x }')
            print(f'left = {left} and right = {right}')
            if right < left:
                print("plus")
                side = "plus"
            elif left <= right:
                print("minus")
                side = "minus"
            
 # get zero zero coordinates

    def get_zero(self):
        self.move_to_the_degree(0,0)
        pass
    
# manual movement    
# you need to develop more righter solution
# I woul like to control with arrows

    def manual_set_coordinates(self):
        print('enter H for a help')
        listen = input()
        while listen != 'q':
            temp_x = self.__degree_x
            temp_z = self.degree_z
            
            if listen == 'd':
                temp_x = self.__degree_x + self.steps_of_degrees
                if temp_x == 360:
                    temp_x = 0
                self.set_degrees(temp_x, temp_z)
                # show me what you got
                self.degrees()
                
            elif listen == 'a':
                temp_x = self.__degree_x - self.steps_of_degrees
                if temp_x == -self.steps_of_degrees:
                    temp_x = 355
                self.set_degrees(temp_x, temp_z)
                # show me what you got
                self.degrees()
                
            elif listen == 'w':
                temp_z = self.degree_z + self.steps_of_degrees
                self.set_degrees(temp_x, temp_z)
                 # show me what you got
                self.degrees()
                
            elif listen == 's':
                temp_z = self.degree_z - self.steps_of_degrees
                self.set_degrees(temp_x, temp_z)
                # show me what you got
                self.degrees()
            elif listen == 'h':
                print('"w" = increase z "s" = discrease z "d" = increase x "a" = discrease x\n',
                    '"1" -a shot "2" - line shoots "R" - reload \n"0" - get to zero x decrees\n',
                    '"P" -turn on or off "U" -change status "Q" -exit\n',
                    '"3" - granade "T" - relaod granade "9" - show_all_cartridges')
            
            elif listen == '0':
                self.get_zero()
                
            elif listen == '1':
                self.one_shot()
            elif listen == '2':
                self.line_shot()
            elif listen == '3':
                self.granade()
            elif listen == '9':
                self.show_all_cartridges()
            elif listen == 'r':
                self.reload_gun()
            elif listen == 't':
                self.reload_granade()
            elif listen == 'p':
                self.switch_power()
            elif listen == 'u':
                self.set_status()
                self.get_status()
                
            elif listen == 'q':
                self.write_to_json()
                break
            else:
                print(" wrong value to control")
            
            self.write_to_json()
 
            # show me what you got
            #self.degrees()
            # NEW circle
            listen = input()
      
    # shoting mode 1
    def show_me_bullets(self):
         print(f'It has {self.bullets} bullets and  {self.it_has_magazines}\n whole bullets is {self.bullets + self.it_has_magazines * self.bullets_in_a_magazine}')
    
    def show_all_cartridges(self): 
        self.show_me_bullets()
        self.show_me_granades()
    
    def one_shot(self):
        self.trigger = True
        if self.trigger == True and self.bullets != 0:
            print('a shot')
            self.count_shoots +=1
            self.bullets -=1
            self.show_me_bullets()
        else:
            self.armed = False
            print('we need a reload')
        self.trigger = False

    # shoting mode 2
    
    def line_shot(self):
        self.trigger = True
        if self.trigger == True and self.bullets >= 3:
            time.sleep(0.25)
            self.count_shoots +=3
            self.bullets -=3
            print('shot in line')
            self.show_me_bullets()
        elif self.trigger == True and self.bullets == 2:
            time.sleep(0.15)
            self.count_shoots +=2
            self.bullets -=2
            print('shot in line')
            self.show_me_bullets()
        elif self.trigger == True and self.bullets == 1:
            self.count_shoots +=1
            self.bullets -=1
            print('shot in line')
            self.show_me_bullets()
        else:
            self.armed = False
            print('we need a reload')
        self.trigger = False
   
       # reloading 
    
    def reload_gun(self):
        if self.it_has_magazines > 0:
            self.it_has_magazines -= 1
            if self.bullets > 0:
                print(f'you have lost {self.bullets} bullets')
            self.bullets = self.bullets_in_a_magazine 
            print('armed')
        else:
            print('no magazines')
        
    # shoting mode 3
    def show_me_granades(self):
         print(f'It has {self.granades} granades and  whole {self.it_has_magazines_of_granades}\n')
    

    def granade(self):
        
        self.trigger_granade = True
        if self.trigger_granade == True and self.granades > 0:
            print('throw granade')
            self.granades -=1
            self.show_me_granades()
        else:
            print('we need a reload')
        self.trigger_granade = False
        
    
    #reloading granade
    
    def reload_granade(self):
        if self.it_has_magazines_of_granades > 0:
            self.it_has_magazines_of_granades += self.granades 
            if  self.it_has_magazines_of_granades >= self.granades_in_a_magazine:
                self.it_has_magazines_of_granades -= self.granades_in_a_magazine
                self.granades = self.granades_in_a_magazine
            elif  self.it_has_magazines_of_granades < self.granades_in_a_magazine:
                self.granades = it_has_magazines_of_granades
            print('armed with granades')
            self.show_me_granades()
        else:
            print('no magazines of granades')

    
    # power on / off
    
    def switch_power(self):
        if self.power == 'off':
            self.power = 'on'
        elif self.power == 'on':
            self.power = 'off'
        print(f'power = {self.power}')

# changing status

    def set_status(self):
        print(" 1 -ready\n 2 - search and destroy\n",
            "3 - warning\n",
            "4 - noshoot\n",
            '5 - broken\n')
        temp = input('status = ')
        if temp == '1':
            self.status = 'ready'
        elif temp == '2':
            self.status = 'search and destroy'
        elif temp == '3':
            self.status = 'warning'
        elif temp == '4':
            self.status = 'noshoot'
        elif temp == '5':
            self.status = 'broken'
        else:
            print('something wrong')

# print status

    def get_status(self):
        print(f'status = {self.status}')
        
        
