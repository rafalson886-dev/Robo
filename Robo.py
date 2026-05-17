


######    ROBO    ######




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

        




