from cmu_graphics import *
import cmu_graphics


from random import randrange
import math

def onAppStart(app):
    app.width = 1000
    app.fieldWidth=app.width
    app.fieldHeight=400
    app.color='white'
    app.inputPower=192
    app.percentage=0
    app.ballX=97
    app.ballY=327
    app.opacity=0
    
    #if i wanna do random
    #a=randrange(400,950 )
    a=900
    #velocity accounts for the angel change
    app.deltaAngle=math.pi/4
    app.velocityX=3.725*math.cos(app.deltaAngle)
    app.velocityY=3.725*math.sin(app.deltaAngle)
    app.accerlation=1.90*math.sin(app.deltaAngle)
    app.oldVelocityY=app.velocityY
    app.targetCX=a
    app.time=0
    app.launch=False
    app.inputPowerPercentage=0
    app.distance=100
    #star scores
    app.star1='grey'
    app.star2='grey'
    app.star3='grey'
    app.starsOpacity=0
    #so you can actually get a 3 star
    app.lastTime=False
    app.count=0
    #obstacles location
    app.obstacleRX=500
    app.obstacleRY=250
    app.obstacleHeight=50
    app.obstacleWidth=50
    app.hitObstacleX=False
    app.hitObstacleY=False
    app.oldTime=0
    app.countHit=0
    app.b=750
    app.countHit=0
    #angle display feature
    app.displayY=370
    app.displayX=320
def redrawAll(app):
    #background 
    drawRect(0,0,app.fieldWidth,app.fieldHeight-100,fill=gradient(rgb(133,89,136),rgb(107,73,132),rgb(72,52,117)
    ,rgb(43,47,119),rgb(20,24,82),rgb(7,11,52), start='bottom'))
    drawCircle(50,33,30,fill=rgb(178,171,159))
    drawCircle(59,29,26,fill=gradient(rgb(20,24,82),rgb(7,11,52), start='bottom'))
    drawRect(0,app.fieldHeight-100,app.fieldWidth,100,fill=rgb(11,162,20))
    
    #canon
    drawCircle(65,348,10,fill='red',rotateAngle=-20)
    drawRect(50,325,50,20,fill='grey', rotateAngle=-20 )
    drawOval(97,327,10,20,fill='grey',rotateAngle=-20 )
    drawOval(97,327,5,10,fill='black',rotateAngle=-20)
    drawCircle(50,344,10,fill='grey',rotateAngle=-20)
    drawCircle(47,350,10,fill='red')
    
    #power bar
    drawRect(40,375,200,15)
    drawRect(44,377,192,10,fill='white')
    drawRect(44,377,app.inputPower,10,fill=app.color)
    
    #Target
    drawOval(app.targetCX,350,70,70,fill='red')
    drawOval(app.targetCX,350,50,50,fill='white')
    drawCircle(app.targetCX,350,10,fill='red')
    
    #ball
    drawCircle(app.ballX,app.ballY,5,fill='lightGrey',opacity=app.opacity)
    
    #stars
    drawStar(500,40,30,5,fill=app.star3,opacity=app.starsOpacity,border='white')
    drawStar(560,80,30,5,fill=app.star2,opacity=app.starsOpacity,border='white')
    drawStar(440,80,30,5,fill=app.star1,opacity=app.starsOpacity,border='white')
    
    #obstacles
    drawRect(app.obstacleRX,app.obstacleRY,app.obstacleWidth,app.obstacleHeight,fill='darkRed',border='black')
    #Triangle
    drawPolygon(500,250,525,225,550,250,fill='darkRed',border='black')
    #Angle display
    drawLine(280,390,app.displayX,app.displayY,fill='white')
    drawLine(280,390,320,390,fill='white')
    #power display:
    drawLabel(app.inputPowerPercentage*100//1,160,360,fill='white')
    #73
    
def onMouseDrag(app,mouseX,mouseY):
    if 377<mouseY<387:
        if 44<mouseX<236:
            app.inputPower=mouseX-44
            if .33<app.inputPower/192<.66:
                app.color=gradient('green','yellow',start='left')
            elif app.inputPower/192>.66:
                app.color=gradient('green','yellow','red',start='left')
            else:
                app.color=gradient('green','greenYellow',start='left')
    app.inputPowerPercentage=app.inputPower/192

def onKeyPress(app,key ):
    if key=='space':
        powerControl(app)
        app.launch=True
        app.opacity=100 
        
    if key=='r':
        app.launch=False
        app.ballX=97
        app.ballY=327
        app.opacity=0
        app.acceleration=2
        app.velocityX=3.725
        app.velocityY=3.725
        app.time=0
        app.starsOpacity=0
        app.star1='grey'
        app.star2='grey'
        app.star3='grey'
        app.hitObstacleX=False
        app.hitObstacleY=False
        app.countHit=0
        app.displayY=370
        app.displayX=320
        app.countHit=0
        app.accerlation=1.90*math.sin(app.deltaAngle)
        
    if  key=='up':
        if app.deltaAngle>=math.pi/2:
            app.deltaAngle=math.pi/2
            app.displayY=360
            app.displayX=280
        else:
            app.deltaAngle+=math.pi/180
            app.displayX-=4/9
            app.displayY-=1/3
        velocityAngle(app)
    
    if  key=='down':
        if app.deltaAngle<=0:
            app.deltaAngle=0
            app.displayY=390
            app.displayX=320
        else:
            app.deltaAngle-=math.pi/180
            app.displayX+=4/9
            app.displayY+=1/3
        velocityAngle(app)
        
def onKeyHold(app,key):
    if 'up' in key :
        if app.deltaAngle>=math.pi/2:
            app.deltaAngle=math.pi/2
            app.displayY=360
            app.displayX=280
        else:
            app.deltaAngle+=math.pi/180
            app.displayX-=4/9
            app.displayY-=1/3
        velocityAngle(app)
    
    if  'down'in key:
        if app.deltaAngle<=0:
            app.deltaAngle=0
            app.displayY=390
            app.displayX=320
        else:
            app.deltaAngle-=math.pi/180
            app.displayX+=4/9
            app.displayY+=1/3
        velocityAngle(app)
        
def powerControl(app):
         #app.inputPowerPercentage=.7447916666666666
         app.velocityX=app.velocityX/1.05*app.inputPowerPercentage
         app.velocityY=app.velocityY/1.05*app.inputPowerPercentage
         
def velocityAngle(app):
    app.velocityX=3.725*math.cos(app.deltaAngle)
    app.velocityY=3.725*math.sin(app.deltaAngle)

def amountOfStars(app):
    
    if app.distance<70:
        app.star1='gold'
        if app.starsOpacity!=100:
            app.starsOpacity+=1
    else:
        app.star1='grey'
    
    if app.distance<50:
        app.star2='gold'
    else:
        app.star2='grey' 
    
    if app.distance<10:
        app.star3='gold'
    else:
        app.star3='grey'
    
    if app.ballY-5>400 and app.starsOpacity!=100:
        app.starsOpacity+=2

        
def horizantalMovement(app):

    if app.hitObstacleX==True:
            app.ballX=app.ballX-app.velocityX*app.time
    else:
        app.ballX=app.ballX+app.velocityX*app.time
def verticalMovement(app):
    if app.hitObstacleY==True:
        app.ballY=app.ballY+app.velocityY*app.time-1/2*app.accerlation*app.time**2
    else:
        app.ballY=app.ballY-app.velocityY*app.time+1/2*app.accerlation*app.time**2

def distance(app):
    app.distance=((app.ballX-app.targetCX)**2+(app.ballY-350)**2)
    app.distance=app.distance**(1/2)
    
    

def onStep(app):
    distance(app)
    amountOfStars(app)
    if app.distance<=37.5 and 312.5<app.ballY<387.5:
        app.launch=False
        if app.launch==False:
            app.lastTime=True
            if app.lastTime==True and app.count!=1:
                app.time+=1/8
                horizantalMovement(app)
                verticalMovement(app)
                app.count+=1
    
    if app.launch==True:
        app.time+=1/16
        horizantalMovement(app)
        verticalMovement(app)
        
    if app.obstacleRX+app.obstacleWidth>app.ballX+5>=app.obstacleRX:
        if app.obstacleRY<app.ballY<app.obstacleRY+app.obstacleHeight:
            app.hitObstacleX=True
        
    
        
    if app.obstacleRY<app.ballY+5<app.obstacleRY+app.obstacleHeight:
        if app.obstacleRX<app.ballX<app.obstacleRX+app.obstacleWidth:
            if app.countHit!=1:
                app.hitObstacleY=True
                app.oldTime=app.time
                app.velocity=-app.accerlation*app.time
                app.time=1/8
                app.countHit=1
                app.accerlation+=2
            else:
                app.hitObstacleY=False
                
    if 500<=app.ballX+5<=525:
        # WHATS UP
        #if app.ballY+5==-1*(app.ballX+5)+app.b:
            #app.velocityY=app.velocityX
            #app.velocityX=0
            #app.time=1/16
        if app.ballY<250 and app.ballY<-app.ballX+750 and app.ballY>app.ballX-300:
            if app.countHit!=1: 
                app.b=app.velocityX
                app.velocityX=-app.velocityX
                app.velocityY=app.oldVelocityY
                app.accerlation+=2
                app.time=0
                app.countHit=1
     
            
        
        print(app.velocityY)  
        
    
    #check the b values
    #review object orientation 
    
        

    
    
        
def main():
    runApp()

main()


cmu_graphics.runApp()