#Ahmed Al Obaidi #CIN:302605529

import direct.directbase.DirectStart
from panda3d.core import Filename,AmbientLight,DirectionalLight
from panda3d.core import PandaNode,NodePath,Camera,TextNode
from panda3d.core import Vec3,Vec4,BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
import random, sys, os, math
from panda3d.bullet import BulletCapsuleShape
from panda3d.bullet import ZUp
from direct.showbase.InputStateGlobal import inputState
from panda3d.bullet import BulletCharacterControllerNode
import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText 
from direct.gui.DirectGui import *
from models import *
from direct.gui.DirectGui import *





class Character(object):


    def __init__(self):
        
        self.models = Models()
        self.health = 100.0
        self.lost = 0
        self.won = 0
        self.debug = False
        self.ev = False
        self.re = False
        self.isMoving = False
        self.nextLevel = False
        self.b3 = 0



        
        self.setUp()
        taskMgr.add(self.update, 'update')
        taskMgr.add(self.updateItems, 'updateItems')
        taskMgr.add(self.updateEnemies, 'updateEnemies')
        taskMgr.add(self.updateEndPoint, 'updateEndPoint')



        
        
        self.mySoundRing = base.loader.loadSfx("sound/ring.mp3")
        self.mySoundPunch = base.loader.loadSfx("sound/punch_or_whack.mp3")
        self.mySoundEvil = base.loader.loadSfx("sound/Evil_Laugh_Male.mp3")
        self.mySoundEndFx = base.loader.loadSfx("sound/End_Fx.mp3")
        self.mySoundEnd = base.loader.loadSfx("sound/Fireworks.mp3")
        self.mySoundRunning = base.loader.loadSfx("sound/running.mp3")
        self.mySoundJump = base.loader.loadSfx("sound/jump.mp3")






        
        
        
    def setUp(self):
        self.itemNumber = 0
        self.incBar()
        
        # Character
        h = 1.75
        w = 0.4
        shape = BulletCapsuleShape(w, h - 2 * w, ZUp)

        self.character = BulletCharacterControllerNode(shape, 0.4, 'Player')
        self.characterNP = render.attachNewNode(self.character)
        self.characterNP.setPos(-325, 950, 60)
        self.characterNP.setH(180)
        self.characterNP.setCollideMask(BitMask32.allOn())
        self.models.world.attachCharacter(self.character)

        self.actorNP = Actor('models/Bricker/Bricker3.egg', {
                         'run' : 'models/Bricker/Bricker-run.egg',
                         'walk' : 'models/Bricker/Bricker-walk.egg',
                         'jump' : 'models/Bricker/Bricker-jump.egg',
                         'fallbackGetup' : 'models/Bricker/FallbackGetup.egg',
                         'fallforwardGetup' : 'models/Bricker/Bricker-FallforwardGetup.egg',
                         'fireball' : 'models/Bricker/Bricker-fireball.egg',
                         'punching' : 'models/Bricker/Bricker-punching.egg',
                         'superpunch' : 'models/Bricker/Bricker-superpunch.egg'})

        self.actorNP.reparentTo(self.characterNP)
        self.actorNP.setScale(0.3)
        self.actorNP.setH(180)
        self.actorNP.setPos(0, 0, 0.2)
        
        
        #enemies
        
        self.setUpEnemies()

        #debug
        
        self.debugNode = BulletDebugNode('Debug')
        self.debugNode.showWireframe(True)
        self.debugNode.showConstraints(True)
        self.debugNode.showBoundingBoxes(False)
        self.debugNode.showNormals(False)
        self.debugNP = render.attachNewNode(self.debugNode)
        self.debugNP.hide()
        self.models.world.setDebugNode(self.debugNP.node())

        
        
        
        
        
    def setUpEnemies(self):
        h2 = 3.75
        w2 = 1.1
        shape2 = BulletCapsuleShape(w2, h2 - 2 * w2, ZUp)

        self.e1 = BulletRigidBodyNode("E1")
        self.e1.setMass(0)
        self.e1.addShape(shape2)
        self.e1NP = render.attachNewNode(self.e1)
        self.e1NP.setPos(-327, 790, self.models.n5Upstairs+3)
        self.e1NP.setCollideMask(BitMask32.allOn())
        self.models.world.attachRigidBody(self.e1)

        self.actorNPe1 = loader.loadModel('models/mummy/mummy.egg')

        self.actorNPe1.reparentTo(self.e1NP)
        self.actorNPe1.setScale(0.05)
        self.actorNPe1.setPos(0, 0, -1.0)
        self.e1Hited = 0
        
        h3 = 3.75
        w3 = 1.1
        shape3 = BulletCapsuleShape(w3, h3 - 2 * w3, ZUp)

        self.e2 = BulletRigidBodyNode("E2")
        self.e2.setMass(0)
        self.e2.addShape(shape3)
        self.e2NP = render.attachNewNode(self.e2)
        self.e2NP.setPos( self.models.Cylinder1.getX(), self.models.Cylinder1.getY(), self.models.n5Upstairs+3)
        self.e2NP.setCollideMask(BitMask32.allOn())
        self.models.world.attachRigidBody(self.e2)

        self.actorNPe2 = loader.loadModel('models/mummy/mummy.egg')

        self.actorNPe2.reparentTo(self.e2NP)
        self.actorNPe2.setScale(0.05)
        self.actorNPe2.setPos(0, 0, -1.0)
        self.e2Hited = 0
        
        h4 = 3.75
        w4 = 1.1
        shape4 = BulletCapsuleShape(w4, h4 - 2 * w4, ZUp)

        self.e3 = BulletRigidBodyNode("E3")
        self.e3.setMass(0)
        self.e3.addShape(shape4)
        self.e3NP = render.attachNewNode(self.e3)
        self.e3NP.setPos( self.models.Cylinder2.getX(), self.models.Cylinder2.getY(), self.models.n5Upstairs+3)
        self.e3NP.setCollideMask(BitMask32.allOn())
        self.models.world.attachRigidBody(self.e3)

        self.actorNPe3 = loader.loadModel('models/mummy/mummy.egg')

        self.actorNPe3.reparentTo(self.e3NP)
        self.actorNPe3.setScale(0.05)
        self.actorNPe3.setPos(0, 0, -1.0)
        self.e3Hited = 0
        
        
        h5 = 3.75
        w5 = 1.1
        shape5 = BulletCapsuleShape(w5, h5 - 2 * w5, ZUp)

        self.e4 = BulletRigidBodyNode("E4")
        self.e4.setMass(0)
        self.e4.addShape(shape5)
        self.e4NP = render.attachNewNode(self.e4)
        self.e4NP.setPos( self.models.Cylinder3.getX(), self.models.Cylinder3.getY(), self.models.n5Upstairs+3)
        self.e4NP.setCollideMask(BitMask32.allOn())
        self.models.world.attachRigidBody(self.e4)

        self.actorNPe4 = loader.loadModel('models/mummy/mummy.egg')

        self.actorNPe4.reparentTo(self.e4NP)
        self.actorNPe4.setScale(0.05)
        self.actorNPe4.setPos(0, 0, -1.0)
        self.e4Hited = 0
        
        
        
        
    def doJump(self):
        self.character.setMaxJumpHeight(15.0)
        self.character.setJumpSpeed(8.0)
        self.character.doJump()


    def processInput(self, dt):
        speed = Vec3(0, 0, 0)
        omega = 0.0
        
        if inputState.isSet('forward')  and  self.won == 0 and self.lost == 0 :
             
            if inputState.isSet('speedUp'):
                speed.setY(20.0)
            else:
                speed.setY(10.0)
         
        if inputState.isSet('reverse')  and  self.won == 0 and self.lost == 0: 
            if inputState.isSet('speedUp'):
                speed.setY(-20.0)
            else:
                speed.setY(-10.0)
                
        if inputState.isSet('turnLeft')  and  self.won == 0 and self.lost == 0:  
            omega =  60.0
            
        if inputState.isSet('turnRight')  and  self.won == 0 and self.lost == 0: 
            omega = -60.0
            
        if inputState.isSet('jump')  and  self.won == 0 and self.lost == 0:
            self.actorNP.loop("jump") 
            self.mySoundRunning.stop()         
            self.mySoundJump.play()
            self.mySoundJump.setVolume(0.6)
            self.doJump()
            
        if inputState.isSet('hit')  and  self.won == 0 and self.lost == 0:
            self.actorNP.loop("punching")
            speed.setY(30.0)
            
        if inputState.isSet('debug') and  self.won == 0 and self.lost == 0:
            if  self.debug == True:
                self.debug = False
            else:
                self.debug = True
                
                
        if inputState.isSet('forward') or inputState.isSet('reverse') or inputState.isSet('turnLeft') or inputState.isSet('turnRight'):
            if self.isMoving is False and  self.won == 0 and self.lost == 0:
                self.actorNP.loop("run")
                self.isMoving = True
                self.mySoundRunning.play()
                self.mySoundRunning.setVolume(0.4)
        else:
            if self.isMoving:
                self.actorNP.stop()
                self.actorNP.pose("walk",0)
                self.isMoving = False
                self.mySoundRunning.stop()
                
                
                
        if inputState.isSet('rotateCamLeft') and  self.won == 0 and self.lost == 0:
            base.camera.setX(base.camera, -20 * globalClock.getDt())
        if inputState.isSet('rotateCamRight') and  self.won == 0 and self.lost == 0:
            base.camera.setX(base.camera, +20 * globalClock.getDt())
            
        
            

                
                
        
                

        self.character.setAngularMovement(omega)
        self.character.setLinearMovement(speed, True)
        
        
    def update(self, task):
        
        if self.debug == True:
            self.debugNP.show()
        else:
            self.debugNP.hide()
 
        angleDegrees = task.time * 1000.0
        angleRadians = angleDegrees * (pi / 180.0)
        
        self.models.Cylinder1.setHpr(angleRadians,0,0)
        self.models.np16.setHpr(angleRadians,0,0)
            
        
        self.models.Cylinder2.setHpr(-angleRadians,0,0)
        self.models.np17.setHpr(-angleRadians,0,0)
        
     
       
        self.models.Cylinder3.setHpr(angleRadians,0,0)
        self.models.np18.setHpr(angleRadians,0,0)

     
        self.models.Cylinder4.setHpr(-angleRadians,0,0)
        self.models.np19.setHpr(-angleRadians,0,0)
        
        if self.models.np19.is_empty() == False and self.models.Cylinder4.is_empty() == False:
            
            if self.testWithSingleBody(self.models.node19)==True and  inputState.isSet('forward') == False and inputState.isSet('reverse') == False and inputState.isSet('turnLeft') == False and inputState.isSet('turnRight') == False and inputState.isSet('jump') == False:
                
                self.characterNP.setPos(0,0,0)
                self.mySoundEndFx.play()
            
        
        return task.cont
    
    def updateItems(self, task):

        
        
        angleDegrees = task.time * 1000.0
        angleRadians = angleDegrees * (pi / 180.0)

        for i in range(self.models.index):

            if self.models.iteamsNpsList[i].is_empty() == False and self.models.iteamsModelsList[i].is_empty() == False:
                self.models.iteamsModelsList[i].setHpr(angleRadians*10,90,0)
                self.models.iteamsNpsList[i].setHpr(angleRadians*10,90,0)
        
                if self.testWithSingleBody(self.models.iteamsNodesList[i])==True:
                    self.models.iteamsModelsList[i].setZ(2000)
                    self.models.iteamsNpsList[i].setZ(2000)
                    self.models.iteamsModelsList[i].remove_node()
                    self.models.iteamsNpsList[i].remove_node()
                    
                    self.mySoundRing.play()
            
                    self.itemNumber += 1
                    self.item.destroy()       
                    self.item = DirectFrame(text = str(self.itemNumber), scale = 0.07, pos=(0.9,0.5,0.8),frameColor=(0, 0, 0, 0),  text_fg = (1,1,1,1),text_shadow =(0,0,0,0.9))

        
        return task.cont
    
    
    def youLost(self):
        
        if self.health < 1 and self.lost == 0:
            taskMgr.remove('updateEnemies')

            self.lost = DirectFrame(text = "You Lost", scale = 0.2, pos=(0,0,0),
                            frameColor=(0, 0, 0, 0),  text_fg = (1,0,0,1),text_shadow =(0,0,0,0.9))
                    
            p = float(float(self.itemNumber)/float(self.models.index) *100.0)
            d = int(p)
            self.lost2 = DirectFrame(text = "You Collected "+str(d)+"% of the Items", scale = 0.1, pos=(0,0,-0.15),
                            frameColor=(0, 0, 0, 0),  text_fg = (1,1,1,1),text_shadow =(0,0,0,0.9))
                    
            self.b = DirectButton(text = "Exit", scale=.07, command=sys.exit, pos=(-0.3,0,-0.3),text_shadow =(0,0,0,0.9),
                                     text_bg=(0, 0, 0, 1),text_fg = (1,1,1,1))
                    
            self.b2 = DirectButton(text = "Restart", scale=.07, command=self.setRestart, pos=(0.3,0,-0.3),text_shadow =(0,0,0,0.9), text_bg=(0, 0, 0, 1),text_fg = (1,1,1,1))
        
        
    def updateEnemies(self, task):
        
        self.youLost()
        
        if self.testWithSingleBody(self.models.ground)==True or self.testWithSingleBody(self.models.node13)==True:
            self.ev = False
            

        if self.testWithSingleBody(self.models.node12)==True:
                
            if self.actorNPe1.is_empty() == False and self.e1NP.is_empty() == False:
                if self.ev == False:          
                    self.mySoundEvil.play() 
                    self.ev = True
                    
                vecE1 = self.characterNP.getPos() - self.e1NP.getPos()
                vecE1.setZ(0)
                vecE1.normalize()           
                self.e1NP.setPos(self.e1NP.getPos() + vecE1 * (1.0/10.0))                                 
                self.actorNPe1.setH(self.actorNPe1.getH()-1000 * globalClock.getDt())
                
            


        if self.testWithSingleBody(self.models.node16)==True:
                
            if self.actorNPe2.is_empty() == False and self.e2NP.is_empty() == False:
                
                if self.ev == False:          
                    self.mySoundEvil.play() 
                    self.ev = True
                    
                vecE2 = self.characterNP.getPos() - self.e2NP.getPos()
                vecE2.setZ(0)
                vecE2.normalize()           
                self.e2NP.setPos(self.e2NP.getPos() + vecE2 * (1.0/10.0))                  
                self.actorNPe2.setH(self.actorNPe2.getH()-1000 * globalClock.getDt())
                
                
        if self.testWithSingleBody(self.models.node17)==True:
                
            if self.actorNPe3.is_empty() == False and self.e3NP.is_empty() == False:
                
                if self.ev == False:          
                    self.mySoundEvil.play() 
                    self.ev = True
                    
                vecE3 = self.characterNP.getPos() - self.e3NP.getPos()
                vecE3.setZ(0)
                vecE3.normalize()           
                self.e3NP.setPos(self.e3NP.getPos() + vecE3 * (1.0/10.0))                  
                self.actorNPe3.setH(self.actorNPe3.getH()-1000 * globalClock.getDt())
                
                
        if self.testWithSingleBody(self.models.node18)==True:
                
            if self.actorNPe4.is_empty() == False and self.e4NP.is_empty() == False:
                
                if self.ev == False:          
                    self.mySoundEvil.play() 
                    self.ev = True
                    
                vecE4 = self.characterNP.getPos() - self.e4NP.getPos()
                vecE4.setZ(0)
                vecE4.normalize()           
                self.e4NP.setPos(self.e4NP.getPos() + vecE4 * (1.0/10.0))                  
                self.actorNPe4.setH(self.actorNPe4.getH()-1000 * globalClock.getDt())
        
        


        
        if self.testWithSingleBody(self.e1)==True:
            self.pain()       
            if inputState.isSet('hit'):            
                self.e1Hited += 1.0
                self.mySoundPunch.play()
                self.mySoundPunch.setVolume(0.5)
                if self.actorNPe1.is_empty() == False and self.e1NP.is_empty() == False and self.e1Hited > 3:
                    self.actorNPe1.setZ(2000)
                    self.e1NP.setZ(2000)
                    self.actorNPe1.remove_node()
                    self.e1NP.remove_node()
                    

                    

        if self.testWithSingleBody(self.e2)==True:
            self.pain()       
            if inputState.isSet('hit'):            
                self.e2Hited += 1.0
                self.mySoundPunch.play()
                self.mySoundPunch.setVolume(0.5)
                if self.actorNPe2.is_empty() == False and self.e2NP.is_empty() == False and self.e2Hited > 3:
                    self.actorNPe2.setZ(2000)
                    self.e2NP.setZ(2000)
                    self.actorNPe2.remove_node()
                    self.e2NP.remove_node()
                    
                    
                    
        if self.testWithSingleBody(self.e3)==True:
            self.pain()       
            if inputState.isSet('hit'):            
                self.e3Hited += 1.0
                self.mySoundPunch.play()
                self.mySoundPunch.setVolume(0.5)
                if self.actorNPe3.is_empty() == False and self.e3NP.is_empty() == False and self.e3Hited > 3:
                    self.actorNPe3.setZ(2000)
                    self.e3NP.setZ(2000)
                    self.actorNPe3.remove_node()
                    self.e3NP.remove_node()
                    

                    
        if self.testWithSingleBody(self.e4)==True:
            self.pain()       
            if inputState.isSet('hit'):            
                self.e4Hited += 1.0
                self.mySoundPunch.play()
                self.mySoundPunch.setVolume(0.5)
                if self.actorNPe4.is_empty() == False and self.e4NP.is_empty() == False and self.e4Hited > 3:
                    self.actorNPe4.setZ(2000)
                    self.e4NP.setZ(2000)
                    self.actorNPe4.remove_node()
                    self.e4NP.remove_node()
                

                
                        
        
        return task.cont

    
    
    
    
    def incBar(self): 
        # Create a frame
        # Add button
        self.bar = DirectWaitBar(text = "HEALTH", value = self.health, range=100,
                             pos = (0.8,0.5,0.9),
                             scale = 0.5, barColor = (0,0.9,0,1),
                             text_fg = (0,0.5,0,1),text_shadow =(0,0,0,0.5))
        
        self.frame = DirectFrame(text = " Items #", scale = 0.07, pos=(0.7,0.5,0.8),
                                 frameColor=(0, 0, 0, 0),  text_fg = (1,1,1,1),text_shadow =(0,0,0,0.9))
        
        self.item = DirectFrame(text = str(self.itemNumber), scale = 0.07, pos=(0.9,0.5,0.8),
                                 frameColor=(0, 0, 0, 0),  text_fg = (1,1,1,1),text_shadow =(0,0,0,0.9))
        

    def pain(self):
        self.bar.destroy()
        self.health -= 0.3
        if self.health < 101 and  self.health > 70:
            self.bar = DirectWaitBar(text = "HEALTH", value = self.health, range=100,pos = (0.8,0.5,0.9),scale = 0.5, barColor = (0,0.9,0,1),text_fg = (0,0.5,0,1),text_shadow =(0,0,0,0.5))
        elif self.health < 71 and  self.health > 40:
            self.bar = DirectWaitBar(text = "HEALTH", value = self.health, range=100,pos = (0.8,0.5,0.9),scale = 0.5, barColor = (0.9,0.9,0,1),text_fg = (0.5,0.5,0,1),text_shadow =(0,0,0,0.5))
        else :
            self.bar = DirectWaitBar(text = "HEALTH", value = self.health, range=100,pos = (0.8,0.5,0.9),scale = 0.5, barColor = (0.9,0,0,1),text_fg = (0.5,0,0,1),text_shadow =(0,0,0,0.5))
    
 
    
    def updateEndPoint(self, task):
                
        angleDegrees = task.time * 5000.0
        angleRadians = angleDegrees * (pi / 180.0)


        if self.models.npEnd.is_empty() == False and self.models.endpoint.is_empty() == False and self.won == 0:
                       
                self.models.endpoint.setHpr(angleRadians,0,0)
                self.models.npEnd.setHpr(angleRadians,0,0)

                if self.testWithSingleBody(self.models.nodeEnd)==True:
                    self.mySoundEnd.play()
                    self.models.endpoint.remove_node()
                    self.models.npEnd.remove_node()
                    self.won = DirectFrame(text = "You Won", scale = 0.2, pos=(0,0,0),
                            frameColor=(0, 0, 0, 0),  text_fg = (0.5,1,0.5,1),text_shadow =(0,0,0,0.9))
                    
                    p = float(float(self.itemNumber)/float(self.models.index) *100.0)
                    d = int(p)
                    self.won2 = DirectFrame(text = "You Collected "+str(d)+"% of the Items", scale = 0.1, pos=(0,0,-0.15),
                            frameColor=(0, 0, 0, 0),  text_fg = (1,1,1,1),text_shadow =(0,0,0,0.9))
                    
                    self.b = DirectButton(text = "Exit", scale=.07, command=sys.exit, pos=(-0.3,0,-0.3),text_shadow =(0,0,0,0.9),
                                     text_bg=(0, 0, 0, 1),text_fg = (1,1,1,1))
                    
                    self.b2 = DirectButton(text = "Restart", scale=.07, command=self.setRestart, pos=(0.3,0,-0.3),text_shadow =(0,0,0,0.9), text_bg=(0, 0, 0, 1),text_fg = (1,1,1,1))
                    self.b3 = DirectButton(text = "Go To Level 2", scale=.07, command=self.nextLevel2, pos=(0,0,-0.5),text_shadow =(0,0,0,0.9), text_bg=(0, 0, 0, 1),text_fg = (1,1,1,1))



        
        return task.cont
    
    def testWithSingleBody(self, secondNode):
        contactResult = self.models.world.contactTestPair(self.character, secondNode) # returns a BulletContactResult object
        if len(contactResult.getContacts()) > 0:
            return True
        
    def setRestart(self):
        self.re = True
        taskMgr.remove('update')
        taskMgr.remove('updateItems')
        taskMgr.remove('updateEnemies')
        taskMgr.remove('updateEndPoint')
        
        self.itemNumber = 0
        self.item.destroy()       
        self.item = DirectFrame(text = str(self.itemNumber), scale = 0.07, pos=(0.9,0.5,0.8),frameColor=(0, 0, 0, 0),  text_fg = (1,1,1,1),text_shadow =(0,0,0,0.9))
        
        
        for i in range(self.models.index):

            if self.models.iteamsNpsList[i].is_empty() == False and self.models.iteamsModelsList[i].is_empty() == False:
                self.models.iteamsModelsList[i].setZ(2000)
                self.models.iteamsNpsList[i].setZ(2000)
                self.models.iteamsModelsList[i].remove_node()
                self.models.iteamsNpsList[i].remove_node()            

        self.models.iteamsModelsList = 0
        self.models.iteamsNodesList = 0
        self.models.iteamsNpsList = 0
        
        self.models.setupItems()
        
        if(self.won != 0):
            self.won.destroy()
            self.won2.destroy()
            self.models.setupEndPoint()

        if(self.lost != 0):
            self.lost.destroy()
            self.lost2.destroy()
            
        self.b.destroy()
        self.b2.destroy()
        
        if(self.b3 != 0):
            self.b3.destroy()

        
        
        self.bar.destroy()
        self.health = 100
        self.bar = DirectWaitBar(text = "HEALTH", value = self.health, range=100,pos = (0.8,0.5,0.9),scale = 0.5, barColor = (0,0.9,0,1),text_fg = (0,0.5,0,1),text_shadow =(0,0,0,0.5))
        
        self.won = 0
        
        self.characterNP.setPos(-325, 950, 60)
        self.characterNP.setH(180)

        
        base.camera.setPos(self.characterNP.getX(),self.characterNP.getY()+10,5)
        base.camera.setHpr(self.characterNP.getHpr())
        base.camera.lookAt(self.characterNP)
        
        
        if self.actorNPe1.is_empty() == False and self.e1NP.is_empty() == False:
            self.actorNPe1.setZ(2000)
            self.e1NP.setZ(2000)
            self.actorNPe1.remove_node()
            self.e1NP.remove_node()

        if self.actorNPe2.is_empty() == False and self.e2NP.is_empty() == False:
            self.actorNPe2.setZ(2000)
            self.e2NP.setZ(2000)
            self.actorNPe2.remove_node()
            self.e2NP.remove_node()
            
        if self.actorNPe3.is_empty() == False and self.e3NP.is_empty() == False:
            self.actorNPe3.setZ(2000)
            self.e3NP.setZ(2000)
            self.actorNPe3.remove_node()
            self.e3NP.remove_node()

        if self.actorNPe4.is_empty() == False and self.e4NP.is_empty() == False:
            self.actorNPe4.setZ(2000)
            self.e4NP.setZ(2000)
            self.actorNPe4.remove_node()
            self.e4NP.remove_node()
            
        self.setUpEnemies()
        
        self.lost = 0


        
        taskMgr.add(self.update, 'update')
        taskMgr.add(self.updateItems, 'updateItems')
        taskMgr.add(self.updateEnemies, 'updateEnemies')
        taskMgr.add(self.updateEndPoint, 'updateEndPoint')


    def removeAll(self):
        self.re = True
        taskMgr.remove('update')
        taskMgr.remove('updateItems')
        taskMgr.remove('updateEnemies')
        taskMgr.remove('updateEndPoint')
        
        self.itemNumber = 0
        self.item.destroy()               
        
        for i in range(self.models.index):
            if self.models.iteamsNpsList[i].is_empty() == False and self.models.iteamsModelsList[i].is_empty() == False:
                self.models.iteamsModelsList[i].setZ(2000)
                self.models.iteamsNpsList[i].setZ(2000)
                self.models.iteamsModelsList[i].remove_node()
                self.models.iteamsNpsList[i].remove_node()            

        self.models.iteamsModelsList = 0
        self.models.iteamsNodesList = 0
        self.models.iteamsNpsList = 0
        
        
        if(self.won != 0):
            self.won.destroy()
            self.won2.destroy()
            self.b.destroy()
            self.b2.destroy()
            self.b3.destroy()

        if(self.lost != 0):
            self.lost.destroy()
            self.lost2.destroy()
            self.b.destroy()
            self.b2.destroy()
            self.b3.destroy()

            

        
        
        self.bar.destroy()
        self.health = 100
        
        self.won = 0
              
        
        if self.actorNPe1.is_empty() == False and self.e1NP.is_empty() == False:
            self.actorNPe1.setZ(2000)
            self.e1NP.setZ(2000)
            self.actorNPe1.remove_node()
            self.e1NP.remove_node()

        if self.actorNPe2.is_empty() == False and self.e2NP.is_empty() == False:
            self.actorNPe2.setZ(2000)
            self.e2NP.setZ(2000)
            self.actorNPe2.remove_node()
            self.e2NP.remove_node()
            
        if self.actorNPe3.is_empty() == False and self.e3NP.is_empty() == False:
            self.actorNPe3.setZ(2000)
            self.e3NP.setZ(2000)
            self.actorNPe3.remove_node()
            self.e3NP.remove_node()

        if self.actorNPe4.is_empty() == False and self.e4NP.is_empty() == False:
            self.actorNPe4.setZ(2000)
            self.e4NP.setZ(2000)
            self.actorNPe4.remove_node()
            self.e4NP.remove_node()
            
        
        self.lost = 0
        
        
        self.actorNP.remove_node()
        self.characterNP.remove_node()
        
        self.models.environ.remove_node()
        self.models.sky.remove_node()
        self.models.groundNp.remove_node()
        self.models.pyramid1.remove_node()
        self.models.np.remove_node()
        self.models.pyramid2.remove_node()
        self.models.np3.remove_node()
        self.models.pyramid3.remove_node()
        self.models.np4.remove_node()
        self.models.sphinx.remove_node()
        self.models.np5.remove_node()
        self.models.box1.remove_node()
        self.models.np8.remove_node()
        self.models.box2.remove_node()
        self.models.np9.remove_node()
        self.models.box3.remove_node()
        self.models.np10.remove_node()
        self.models.box4.remove_node()
        self.models.np11.remove_node()
        
        
        for i in range(10):
            self.models.stairsListNp[i].remove_node()
            self.models.stairsList[i].remove_node()
            
            
        self.models.box6.remove_node()
        self.models.np12.remove_node()
        self.models.box7.remove_node()
        self.models.np13.remove_node()
        self.models.box8.remove_node()
        self.models.np14.remove_node()
        self.models.Cylinder1.remove_node()
        self.models.np16.remove_node()
        self.models.Cylinder2.remove_node()
        self.models.np17.remove_node()
        self.models.Cylinder3.remove_node()
        self.models.np18.remove_node()
        self.models.Cylinder4.remove_node()
        self.models.np19.remove_node()
        self.models.fire.remove_node()
        self.models.endpoint.remove_node()
        self.models.npEnd.remove_node()

    def nextLevel2(self):
        self.nextLevel = True




            
        

        
        
        



        
  

        

    
        


        
        
        




   
