

# def dodaj(a, b):
#     return a + b


# wynik = dodaj(5, 3)
# print("wynik=", wynik)



# def podziel_poprzednie (wynik, b ):
#     return wynik / b

# wynik2 = podziel_poprzednie (wynik, 3)
# print ("wynik2=",wynik2)




# def heheszki ( wynik, wynik2, a ,b):
#     return (wynik + wynik2 + a - b)
# wynik3 = heheszki (wynik, wynik2,4,6 )
# print ("heheszki=", wynik3)



# wynik = 10
# wynik2 = 30
# liczba = 15
# a = 1


# def przypisz (wynik, wynik2,liczba,a ):    ##  P A R A M E T R Y  ## 
#     return (wynik + wynik2 / liczba -a )
# total = przypisz(wynik, wynik2,liczba,a )  ##  A R G U M E B T Y  -- Przy wywolaniu --  ##
# print(total)









# class Caluclator:
#     def add ( self , a ,b):
#         return a + b
#     def substitute (self,a,b):
#         return a - b
#     def multitply (self,a,b ):
#         return a *b
#     def divide (self, a,b):
#         if b == 0:
#             return("ERROR")
#         return a/b
    
# calc = Caluclator()
# calc2 = Caluclator()

# print (calc.add(4,4))
# print (calc.substitute(4,4))
# print (calc.multitply(4,4))
# print (calc.divide(4,4)) 


# print (calc2.add(4,10))
# print (calc2.substitute(4,10))
# print (calc2.multitply(4,10))
# print (calc2.divide(4,10)) 






# class Person:
#     def __init__(self, name, age, job):
#         self.name = name
#         self.age = age
#         self.job = job

#     def przedstaw_sie(self):
#         print(f"My name is {self.name} i am {self.age} old , my proffesion is {self.job}")

# p1 = Person("Emil", 27, "IT menager" )
# p2 = Person("Rafal", 39, "programmer")

# p1.przedstaw_sie()
# p2.przedstaw_sie()




# class Person:
#     def __init__(self, name , age = 18 , job = "rating" ):
#         self.name = name
#         self.age = age
#         self.job = job

# p1 = Person("Emil")
# p2 = Person("Rafal", 39, job = "programmer")
        


# print ( f"My name is {p1.name} , my age is {p1.age}, my job is {p1.job}" )
# print ( f"My name is {p2.name}, my age is  {p2.age}, my job is {p2.job}")








# class Polonez:
#     def hamuj(self):
#         print("ale lata")
#     def bokiem(self, strona):
#         print(f"leci bokiem w {strona}")      

# moj_polonez = Polonez()        
# moj_polonez1 = Polonez()

# moj_polonez.hamuj()
# moj_polonez1.bokiem("w prawo")



# class Polonez:
#     def __init__(self, name,hamuje, skreca ):
        
#         self.name = name
#         self.hamuje = hamuje
#         self.skreca = skreca

#     def moje_auto(self):
#         print(f"Moje auto {self.name} hamuje {self.hamuje} i skreca {self.skreca} ")    

#     def leci_bokiem (self, strona = "calkiem niezle w prawo"):
#         self.strona = strona     
#         print(f"Moje auto {self.name} leci bokiem {self.strona}") 


# pol1 = Polonez("Auto 1", "dobrze", "w prawo")
# pol2 = Polonez("Auto 2", "slabo", " w lewo")

# pol1.moje_auto()
# pol2.moje_auto()

# pol1.leci_bokiem()
# pol2.leci_bokiem()    



# class Calculator:
#     def add (self,a,b):
#         print (a + b)
#         return a+b
    
#     def sub (self,a,b):
#         print (a - b)
#         return a-b
        
    
    
# calc = Calculator()

# calc.add (4,4)
# calc.sub (4,2)










# class Robot: 
#     def __init__(self, name, move1, move2, move3,move4 ):
#         self.name = name
#         self.move1 = move1
#         self.move2 = move2
#         self.move3 = move3
#         self.move4 = move4
#         self.memory = [ 1,0,0,1,1,0,1,1,1 ]


#     def add (self,value):
#         self.memory.append(value)
#         self.content = (f"{self.name} add value {value}")
#         print (self.content)
#         return self.content
        
            

#     def my_robot(self):
#         self.command1 = (f"My robot - {self.name} do moves -  {self.move1}, {self.move2}, {self.move3}, {self.move4}, SM - {self.memory}")
#         print (self.command1)
#         return self.command1

#     def start_system1(self, method = "procedure"):
#         self.command2 =  (f"{self.name} Start system by {method} ")
#         print (self.command2)
#         return self.command2     
    
#     def start_system2(self, method = "auto"):
#         self.command3 =  (f"{self.name} Start system by {method} ")
#         print (self.command3)
#         return self.command3     



#     def diagnostic(self):
#         choose_method = input("Chose method of  diagnostic \n-auto \n-manual :")
#         if choose_method == "auto":
#             print("auto initializing")
#         if choose_method == "manual":
#             print("use manual diagno steps ")    


# rob1 = Robot("Robo1", "left", "right", "up", "down" )
# rob2 = Robot("Robo2", "up","down","left","right")

# rob1.add(10)
# rob2.add(20)

# rob1.my_robot()
# rob2.my_robot()

# rob1.start_system1()
# rob2.start_system2()

# rob1.diagnostic() 



######    ROBO    $$$$$$




class Robot: 
    def __init__(self, name,):
        self.name = name
        self.memory = {
                        "Robo1" : [ (0,1,0,1,0,0,1,0), (0,1,0,0,0,0,0,1), (0,1,0,0,0,1,1,0), (0,1,0,0,0,0,0,1), (0,1,0,0,1,1,0,0)],
                        "Robo2" : [ (0,1,0,0,1,0,0,1), (0,1,0,1,0,1,1,1), (0,1,0,0,0,0,0,1), (0,1,0,0,1,1,1,0)]}[name]
        self.moves =  {
                        "Robo1": ["down","up","left","down" ],
                        "Robo2": ["up","down","left", "right"]} [name]


        self.energy = {"Robo1":100,
                       "Robo2":100 
                       }[name]
        

    def add (self,value):
        self.memory.append(value)
        self.content = (f"{self.name} add value {value}")
        print (self.content)
        return self.content
        
    def add_move(self,move):
        self.moves.append(move)
        print(f"{self.name} learned new move {move}")
        


    def my_robot(self):
        self.command1 = (f"My robot - {self.name}  has {self.energy} HP , do moves - {self.moves} and SM - {self.memory}")
        print (self.command1)
        return self.command1

    def start_system1(self, method = "procedure"):
        self.command2 =  (f"{self.name} Start system by {method} ")
        print (self.command2)
        return self.command2     
    
    def start_system2(self, method = "auto"):
        self.command3 =  (f"{self.name} Start system by {method} ")
        print (self.command3)
        return self.command3     



    def diagnostic(self):
        choose_method = input("Chose method of  diagnostic \n-auto \n-manual :").strip().lower()
        if choose_method == "auto":
            status = "full safely"
            print(f"auto initializing, status - {status}")
            maintenance = input ("Want you auto-maintenance porcedure?: \n- yes \n- no: ").strip().lower()
            if maintenance == "yes":
                print("Start auto-maintenance")
                return maintenance
            else:
                print("Auto-maintenance skipped")
                return maintenance
        elif choose_method == "manual":
            status = "not safely"
            print(f"use manual diagnostic steps , status = {status} ")    
   
   

rob1 = Robot("Robo1", ) 
rob2 = Robot("Robo2", )

rob1.add(10)
rob2.add(20)
rob1.add_move("jump")

rob1.my_robot()
rob2.my_robot()

rob1.start_system1()
rob2.start_system2()

rob1.diagnostic() 


class Medical_Robot (Robot):

    def __init__(self,name):
        super().__init__(name)

        
    def lost_energy (self,lost):
        
        self.energy-=lost
        print(f" {self.name} has  {self.energy} HP because lost {lost} HP")
        return self.energy

    
    def heal(self, healing ):
        if self.energy<=100:
            self.energy = min(100,self.energy + healing )
            print(f"{self.name} healing - restore {healing}HP " )

    def my_med_rob(self):
        print(f"My Medical Robot {self.name} can healing status of energy - {self.energy}")


med1 = Medical_Robot("Robo1")        
med2 = Medical_Robot("Robo2")

med1.lost_energy(10)
med1.heal(20)

med1.my_med_rob()
med2.my_med_rob()

        




