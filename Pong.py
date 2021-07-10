"""
Created on Thu Apr 20 21:38:18 2017

@author: Ashail
"""

from __future__ import division
import random,os, pygame,sys,numpy,decimal

#create the paddel object
class paddle:
    def __init__(self,image,width,height,speedx):
        self.speedx=speedx
        self.image=image
        self.pos=image.get_rect().move(width,height)
        self.xmin=image.get_rect().left
        self.xmax=image.get_rect().right
        self.width=width
    def move(self,dt,predicted):
        self.pos.x=predicted
        
        if self.pos.right>=1000:   
            self.speedx = -1*self.speedx 
        if self.pos.left<=0:
            self.speedx=-1*self.speedx
  
#Create game object class   
class GameObject:   
    def __init__(self, image,width, height, speedx, speedy, angle):   
        self.speedx = speedx
        self.speedy = speedy
        self.image = image   
        self.pos = image.get_rect().move(width, height) 

        self.angle=angle
    def move(self,dt):   
        self.pos = self.pos.move(self.speedx*dt, self.speedy*dt)   
        if self.pos.x+(self.image.get_width()/2)>=1079:   
            self.speedx = -1*self.speedx 
        if self.pos.x -(self.image.get_width()/2)<=0:
            self.speedx=-1*self.speedx
        if self.pos.y-(self.image.get_height()/2)<=0:
            self.speedy=-1*self.speedy
        if self.pos.y+(self.image.get_height()/2)>=900:
            self.speedy=-1*self.speedy
   
#function to load an image   
def load_image(name):   
    path = os.path.join(name)   
    return pygame.image.load(path).convert()  

#Function to quit pygame
def quit (self):
    pygame.display.quit() 
    sys.exit()
    
# function to increment position based on speed, current position and time increment    
def incrementpos(predicted,currentx,speed,dt):
    if currentx>predicted:
        speed=-1*abs(speed)
    elif currentx<predicted:
        speed=1
    else:
        speed=speed
        
    if predicted!=currentx :
        newx= currentx+speed*dt
    else:
        newx=predicted
        
    if predicted> currentx+speed*dt and currentx>predicted:
        newx=predicted
    if predicted< currentx+speed*dt and currentx<predicted:
        newx=predicted
        
    return newx
   
 
def main():  
    t=0

#initialise    
    pygame.init()   
    screen = pygame.display.set_mode((1080,720))   

#load required images   
    player = load_image('puck.jpg')   
    background = load_image('white.jpg') 
    paddler= load_image('paddle.png')
   
#transform the images as required
    background = pygame.transform.scale2x(background)    
    background = pygame.transform.scale2x(background)
    player=pygame.transform.scale(player, (20, 20)) 
    paddler=pygame.transform.scale(paddler, (30,10 ))
    screen.blit(background, (0, 0)) 
    
#Declare all variabes outside the loop    
    ballx=[]
    bally=[]
    paddlex=[]
    paddley=[]
    objects2 = [] 
    objects1 = []
    X=numpy.zeros(shape=(1,5))
    bih=numpy.zeros(shape=(1,5))
    Yh=numpy.zeros(shape=(1,5))
    Who=numpy.zeros(shape=(5,1))
    S=numpy.zeros(shape=(1,5))
    DeltaWho=numpy.zeros(shape=(5,1))
    DeltaWih=numpy.zeros(shape=(5,5))
    Wih=numpy.zeros(shape=(5,5))
    AltError=numpy.zeros(shape=(1,5))
    bho=0
    error=[]
    Yo=0
    a,b=S.shape
    c,d=DeltaWih.shape
    paddlex=[]
    paddley=[]
    ballx=[]
    bally=[]

# Set random weights and biases between the values of 0.8 and 0.2
    if t<2:
        for i in range(5):
            for h in range(5):
                Wih[i][h]=float(decimal.Decimal(random.randrange(22, 80))/100)
                bih[0][h]=float(decimal.Decimal(random.randrange(22, 80))/100)
                Who[h][0]=float(decimal.Decimal(random.randrange(22, 80))/100)
                bho=float(decimal.Decimal(random.randrange(22, 80))/100)
 
# Set the objects from the onject definition as declared above   
    for x in range(1):   
        o = GameObject(player,random.randint(20,1000), random.randint(10,500), 1,1,30)
        p= paddle(paddler,random.randint(20,800),600,1)
        objects1.append(p)
        objects2.append(o)   

# Set the number of points to 0
    points=0


    

    while 1:  
        
# time delay required to ensure that the display renders ever 1 milisecond  
        pygame.time.delay(1)
        
# Add the catch case for if the quit button is pressed or the mouse clicked
        for event in pygame.event.get():   
            if event.type == pygame.QUIT: 
                pygame.quit() 
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                None
                
# Sets the points everytime the ball hits the paddle and ensures that the ball's speed is reversed 
        if o.pos.y+(p.image.get_height()/2)+(o.image.get_height()/2)==p.pos.y and o.pos.x>=p.pos.left and o.pos.x<=p.pos.right :
            o.speedy=o.speedy*-1
            points=points+1
            
# Resets the positions the moment the paddle misses the ball. The ball is set to a random position and the paddles is set to the center          
        if o.pos.y>p.pos.y :
            o.pos.right=random.randint(40,1000)
            o.pos.bottom=random.randint(40,90)
            p.pos.right=500
            
# Displys the ball and removes the ball image from the previous position it was at
            screen.blit(background,p.pos, p.pos)
            screen.blit(p.image, p.pos) 
            screen.blit(background, (0, 0)) 
            screen.blit(background, o.pos, o.pos) 
            screen.blit(o.image, o.pos)
            
# Reset the game when the paddle has hit the ball more than 5 times        
        if points>5:
            o.pos.right=random.randint(40,1000)
            o.pos.bottom=random.randint(40,90)
            p.pos.right=500
            screen.blit(background,p.pos, p.pos)
            screen.blit(p.image, p.pos) 
            screen.blit(background, (0, 0)) 
            screen.blit(background, o.pos, o.pos) 
            screen.blit(o.image, o.pos)
            points=0
            
#Add the data to a list so that a time series can be created            
        paddlex.append(p.pos.x)
        paddley.append(p.pos.y)
        ballx.append(o.pos.x)
        bally.append(o.pos.y)
            
            
#Sets the inputs of the neural network and normalises it      
        X[0][0]=ballx[t]/1080
        X[0][1]=bally[t]/720
        X[0][2]=paddlex[t]/1080
        X[0][3]=ballx[t-1]/1080
        X[0][4]=bally[t-1]/720

# set the learning rate of the neural network to 0.5        
        LearningRate=0.5 

  
#Calculate the effective Input
        S=numpy.matmul(X,Wih)
    
#Calculate ouput From Hidden Layer     
        for h in range(b):
            Yh[0][h]=(1/(1+numpy.exp(-1*S[0][h])))
        
#Calculating the input of the exit node
        for h in range(b):
            Yo=numpy.matmul(Yh,Who)+bho
#Increment the time  y the time step and set the predicted value as the output of the neural network scaled again        
        dt=1
        t=t+dt 
        predicted=Yo*1080

#Add the paddle and ball's position to the list to create a time series of its motion
        paddlex.append(p.pos.x)
        paddley.append(p.pos.y)
        ballx.append(o.pos.x)
        bally.append(o.pos.y)
        
#Update the position of the ball and paddle, and update the display 

        for o in objects2:  
            o.move(dt) 
            screen.blit(background, (0, 0)) 
            screen.blit(background, o.pos, o.pos) 
            screen.blit(o.image, o.pos)
        
        for p in objects1:  

            x1=incrementpos(predicted-p.image.get_width()/2,p.pos.x,p.speedx,dt)
            p.move(dt,x1) 
            screen.blit(background,p.pos, p.pos)
            screen.blit(p.image, p.pos) 

   
        pygame.display.update() 
       
         
#Error Calculation
        error.append((o.pos.x-Yo*1080)/1080)

        
#Changing Weights Between Ouput and Hidden Layer
        for h in range(b):
            DeltaWho[h][0]=LearningRate*error[t-1]*Yh[0][h]
            Who[h][0]+=DeltaWho[h][0]
            
        bho+=LearningRate*error[t-1]*bho
        
        
#Error for weights between input and hidden layer
        for h in range(b):
            AltError[0][h]=2*error[t-2]*Who[h][0]*Yh[0][h]*(1-Yh[0][h]);
        
        
#Update Weights between input and hidden layer
        for i in range(c):
            for h in range(b):
                DeltaWih[i][h]=LearningRate*AltError[0][h]*X[0][i]
                Wih[i][h]+=DeltaWih[i][h]

if __name__ == '__main__': main() 
