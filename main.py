#Ahmed Al Obaidi #CIN:302605529

from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Vec3,Vec4,BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.showbase.ShowBase import ShowBase
import random, sys, os, math
from character import *
from character2 import *

from direct.gui.OnscreenImage import OnscreenImage




# Function to put instructions on the screen.
def addInstructions(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(1,1,1,1),
                        pos=(-1.3, pos), align=TextNode.ALeft, scale = .05)

# Function to put title on the screen.
def addTitle(text):
    return OnscreenText(text=text, style=1, fg=(1,1,1,1),
                        pos=(1.3,-0.95), align=TextNode.ARight, scale = .07)
    


class World(ShowBase):

    def __init__(self):
        

        base.win.setClearColor(Vec4(0,0,0,1))
        
        # Game state variables
        self.showHelp = False
        self.showMenu = True
        self.isLevel1 = False
        self.isLevel2 = False
        self.characterClass = 0

        
        
        
        self.inst1 = addInstructions(0.95, "[ESC]: Quit")
        self.inst2 = addInstructions(0.90, "[Left Arrow]: Rotate Left")
        self.inst3 = addInstructions(0.85, "[Right Arrow]: Rotate Right")
        self.inst4 = addInstructions(0.80, "[Up Arrow]: Run Forward")
        self.inst5 = addInstructions(0.75, "[Down Arrow]: Run Backward")
        self.inst6 = addInstructions(0.70, "[Shift + Up Arrow]: Speed up Running Forward")
        self.inst7 = addInstructions(0.65, "[Shift + Down Arrow]: Speed up Running Backward")
        self.inst8 = addInstructions(0.60, "[CTRL]: Hit the Enemy")
        self.inst9 = addInstructions(0.55, "[Space]: Jump")
        self.inst10 = addInstructions(0.50, "[D]: Show / Hide Debug")
        self.inst11 = addInstructions(0.45, "[A]: Rotate Camera Left")
        self.inst12 = addInstructions(0.40, "[S]: Rotate Camera Right")
        self.inst13 = addInstructions(0.35, "[H]: Show/ Hide Help")
        self.inst14 = addInstructions(0.30, "[Enter]: Show/ Hide Menu")


        inputState.watchWithModifiers('forward', 'arrow_up')
        inputState.watchWithModifiers('reverse', 'arrow_down')
        inputState.watchWithModifiers('turnLeft', 'arrow_left')
        inputState.watchWithModifiers('turnRight', 'arrow_right')
        inputState.watchWithModifiers('rotateCamLeft', 'a')
        inputState.watchWithModifiers('rotateCamRight', 's')
        inputState.watchWithModifiers('jump', 'space')
        inputState.watchWithModifiers('speedUp', 'shift')
        inputState.watchWithModifiers('hit', 'control')
        inputState.watchWithModifiers('debug', 'd')
        inputState.watchWithModifiers('help', 'h')
        inputState.watchWithModifiers('menu', 'enter')

        self.accept("escape", sys.exit)
 
        
        #Background music
        self.mySound = base.loader.loadSfx("sound/Ancient Egyptian Music - Dark Pyramid.mp3")             

        #Menu
        self.imageObject = OnscreenImage(image = 'models/menu.jpg', pos = (0, 0, 0))
        self.imageObject.setScale(2,1,1)
        self.b1 = DirectButton(text = "Play Level 1", scale=.07, command=self.setLevel1, pos=(0,0,0.2),text_shadow =(0,0,0,0.9), text_bg=(0, 0, 0, 1),text_fg = (1,1,1,1))
        self.b2 = DirectButton(text = "Play Level 2", scale=.07, command=self.setLevel2, pos=(0.0,0,0),text_shadow =(0,0,0,0.9), text_bg=(0, 0, 0, 1),text_fg = (1,1,1,1))
        self.b3 = DirectButton(text = "Exit", scale=.07, command=sys.exit, pos=(0,0,-0.2),text_shadow =(0,0,0,0.9),text_bg=(0, 0, 0, 1),text_fg = (1,1,1,1))
                    


        
        taskMgr.add(self.update, 'updateMain')


        base.disableMouse()


        # Create some lighting
        ambientLight = AmbientLight("ambientLight")
        ambientLight.setColor(Vec4(.3, .3, .3, 1))
        directionalLight = DirectionalLight("directionalLight")
        directionalLight.setDirection(Vec3(-5, -5, -5))
        directionalLight.setColor(Vec4(1, 1, 1, 1))
        directionalLight.setSpecularColor(Vec4(1, 1, 1, 1))
        render.setLight(render.attachNewNode(ambientLight))
        render.setLight(render.attachNewNode(directionalLight))
        
        
        

    def setLevel1(self):
        if self.isLevel1 == True or self.isLevel2 == True:
            self.characterClass.removeAll()

          
        self.showMenu = False     
        self.characterClass = Character()   
        base.camera.setPos(self.characterClass.characterNP.getX(),self.characterClass.characterNP.getY()+15,5)
        base.camera.setHpr(self.characterClass.characterNP.getHpr())
        base.camera.lookAt(self.characterClass.characterNP)
        self.isLevel1 = True
        self.isLevel2 = False



        
        
    def setLevel2(self):
        if self.isLevel1 == True or self.isLevel2 == True:
            self.characterClass.removeAll()
            
        self.showMenu = False     
        self.characterClass = Character2()   
        base.camera.setPos(self.characterClass.characterNP.getX(),self.characterClass.characterNP.getY()+15,5)
        base.camera.setHpr(self.characterClass.characterNP.getHpr())
        base.camera.lookAt(self.characterClass.characterNP)
        self.isLevel2 = True
        self.isLevel1 = False

        
    def update(self, task):
        
        if self.isLevel1 == True and self.characterClass != 0:
            if self.characterClass.nextLevel == True:
                self.setLevel2()
                
                
        if self.isLevel2 == True and self.characterClass != 0:
            if self.characterClass.nextLevel == True:
                self.setLevel1()
             
        
        
        
        if inputState.isSet('help'):
            if self.showHelp == True:
                self.showHelp = False
            else:
                self.showHelp = True
                
        if inputState.isSet('menu'):
            if self.showMenu == True:
                self.showMenu = False
            else:
                self.showMenu = True
                
        
        if self.showHelp == True:      
            self.inst1.show()
            self.inst2.show()
            self.inst3.show()
            self.inst4.show()
            self.inst5.show()
            self.inst6.show()
            self.inst7.show()
            self.inst8.show()
            self.inst9.show()
            self.inst10.show()
            self.inst11.show()
            self.inst12.show()
            self.inst13.show()
            self.inst14.show()

        else:
            self.inst1.hide()
            self.inst2.hide()
            self.inst3.hide()
            self.inst4.hide()
            self.inst5.hide()
            self.inst6.hide()
            self.inst7.hide()
            self.inst8.hide()
            self.inst9.hide()
            self.inst10.hide()
            self.inst11.hide()
            self.inst12.hide()
            self.inst13.hide()
            self.inst14.hide()
            
        
        if self.showMenu == True:
            self.imageObject.show()
            self.b1.show()
            self.b2.show()
            self.b3.show()
            if self.characterClass != 0:
                self.characterClass.bar.setPos(2,2,2)
                self.characterClass.frame.setPos(2,2,2)
                self.characterClass.item.setPos(2,2,2)
        else:
            self.imageObject.hide()
            self.b1.hide()
            self.b2.hide()
            self.b3.hide()
            if self.characterClass != 0:
                self.characterClass.bar.setPos(0.8,0.5,0.9)
                self.characterClass.frame.setPos(0.7,0.5,0.8)
                self.characterClass.item.setPos(0.9,0.5,0.8)



            
            
        if self.mySound.status() == self.mySound.READY:
            self.mySound.play()
            self.mySound.setVolume(0.9)
            
            
            


        if self.isLevel1 == True or self.isLevel2 == True:

            dt = globalClock.getDt()
            self.characterClass.processInput(dt)
            self.characterClass.models.world.doPhysics(dt, 100, 1./180.)
        
        
            # Create a floater object.  We use the "floater" as a temporary
            # variable in a variety of calculations.
            self.characterClass.floater = NodePath(PandaNode("floater"))
            self.characterClass.floater.reparentTo(render)
        
        


        
            if self.characterClass.characterNP.getZ() != 0:
                base.camera.setZ(self.characterClass.characterNP.getZ()+3)
            

            # If the camera is too far from ralph, move it closer.
            # If the camera is too close to ralph, move it farther.
            camvec = self.characterClass.characterNP.getPos() - base.camera.getPos()
            camvec.setZ(0)
            camdist = camvec.length()
            camvec.normalize()
            if (camdist > 15.0):
                base.camera.setPos(base.camera.getPos() + camvec*(camdist-15))
                camdist = 15.0
            if (camdist < 5.0):
                base.camera.setPos(base.camera.getPos() - camvec*(5-camdist))
                camdist = 5.0

            self.characterClass.floater.setPos(self.characterClass.characterNP.getPos())
            self.characterClass.floater.setZ(self.characterClass.characterNP.getZ() + 2.0)
            base.camera.lookAt(self.characterClass.floater)

        return task.cont
    
    
        

    





w = World()
base.run()
