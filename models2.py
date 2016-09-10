#Ahmed Al Obaidi #CIN:302605529


from panda3d.bullet import BulletWorld
from panda3d.core import Vec3,Texture
from panda3d.bullet import BulletPlaneShape
from panda3d.bullet import BulletRigidBodyNode
from panda3d.bullet import BulletBoxShape
from panda3d.bullet import BulletDebugNode
from direct.showbase.DirectObject import DirectObject
from panda3d.core import BitMask32
import random
from panda3d.core import Point3
from direct.interval.IntervalGlobal import *
from panda3d.bullet import BulletCylinderShape
from panda3d.bullet import ZUp
from panda3d.bullet import BulletGhostNode
from panda3d.bullet import BulletTriangleMesh
from panda3d.bullet import BulletTriangleMeshShape
from panda3d.bullet import BulletSphereShape
from math import pi, sin, cos, atan, acos


class Models2(object):


    def __init__(self):
        
        self.setup()
        
        
        self.angel = 1

               
        # Set up the environment
        #
        
        self.sky = loader.loadModel("models/solar_sky_sphere")
        self.sky.reparentTo(render)
        self.sky.setScale(10000)
        self.sky.setPos(0,0,0)
        self.sky_tex = loader.loadTexture("models/stars_1k_tex.jpg")
        self.sky.setTexture(self.sky_tex, 1)
        
    
        

        
        
    
    def setup(self):
        
        
        
        #World
        self.world = BulletWorld()
        self.world.setGravity(Vec3(0, 0, -9.81))
     
        #Ground
        shape = BulletPlaneShape(Vec3(0, 0, 1), 1)
        self.ground = BulletRigidBodyNode('Ground')
        self.ground.addShape(shape) 
        self.groundNp = render.attachNewNode(self.ground)
        self.groundNp.setPos(0, 0, 0)
        self.groundNp.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.ground)
        
        
        #build
        self.shape1 = BulletBoxShape(Vec3(8, 8, 0.75))
        self.node1 = BulletRigidBodyNode('Box1')
        self.node1.setMass(0)
        self.node1.addShape(self.shape1)
        self.np1 = render.attachNewNode(self.node1)
        self.np1.setPos(0, 0, 100)
        self.np1.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.node1) 
        self.box1= loader.loadModel("models/box/box1")
        self.box1.reparentTo(render)
        self.box1.setScale(10,10,0.2)
        self.box1.setPos(0,0,100)
        
        
        self.shape2 = BulletBoxShape(Vec3(8, 8, 0.75))
        self.node2 = BulletRigidBodyNode('Box2')
        self.node2.setMass(0)
        self.node2.addShape(self.shape2)
        self.np2 = render.attachNewNode(self.node2)
        self.np2.setPos(5, -22, 102)
        self.np2.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.node2) 
        self.box2= loader.loadModel("models/box/box1")
        self.box2.reparentTo(render)
        self.box2.setScale(10,10,0.2)
        self.box2.setPos(5, -22, 102)
        
        
        self.shape3 = BulletBoxShape(Vec3(8, 8, 0.75))
        self.node3 = BulletRigidBodyNode('Box3')
        self.node3.setMass(0)
        self.node3.addShape(self.shape3)
        self.np3 = render.attachNewNode(self.node3)
        self.np3.setPos(-5, -44, 104)
        self.np3.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.node3) 
        self.box3= loader.loadModel("models/box/box1")
        self.box3.reparentTo(render)
        self.box3.setScale(10,10,0.2)
        self.box3.setPos(-5, -44, 104)
        
        self.shape4 = BulletBoxShape(Vec3(8, 8, 0.75))
        self.node4 = BulletRigidBodyNode('Box4')
        self.node4.setMass(0)
        self.node4.addShape(self.shape4)
        self.np4 = render.attachNewNode(self.node4)
        self.np4.setPos(-27, -44, 104)
        self.np4.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.node4) 
        self.box4= loader.loadModel("models/box/box1")
        self.box4.reparentTo(render)
        self.box4.setScale(10,10,0.2)
        self.box4.setPos(-27, -44, 104)
        
        
        self.shape5 = BulletBoxShape(Vec3(8, 8, 0.75))
        self.node5 = BulletRigidBodyNode('Box5')
        self.node5.setMass(0)
        self.node5.addShape(self.shape5)
        self.np5 = render.attachNewNode(self.node5)
        self.np5.setPos(-27, -66, 104)
        self.np5.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.node5) 
        self.box5= loader.loadModel("models/box/box1")
        self.box5.reparentTo(render)
        self.box5.setScale(10,10,0.2)
        self.box5.setPos(-27, -66, 104)
        
        
        self.box6= loader.loadModel("models/box/box1")
        self.box6.reparentTo(render)
        self.box6.setScale(10,87,0.2)
        self.box6.setPos(-22,-150,106)
        self.shape6 = BulletBoxShape(Vec3(8, 70, 0.75))
        self.node6 = BulletRigidBodyNode('Box6')
        self.node6.setMass(0)
        self.node6.addShape(self.shape6)
        self.np6 = render.attachNewNode(self.node6)
        self.np6.setPos(-22, -150, 106)
        self.np6.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.node6) 
        
        
        blocks_tex6 = loader.loadTexture("models/blocks_tex6.jpg")

        self.Cylinder1= loader.loadModel("models/Cylinder/Cylinder")
        self.Cylinder1.reparentTo(render)
        self.Cylinder1.setScale(8,8,0.2)
        self.Cylinder1.setPos(-22,-230,108)
        self.Cylinder1.setTexture(blocks_tex6, 1)
        radius = 8
        height = 1
        shape16 = BulletCylinderShape(radius, height, ZUp)
        self.node16 = BulletRigidBodyNode('Cylinder1')
        self.node16.setMass(0)
        self.node16.addShape(shape16)
        self.np16 = render.attachNewNode(self.node16)
        self.np16.setPos(-22, -230, 108)
        self.np16.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.node16)
        
        
        self.Cylinder2= loader.loadModel("models/Cylinder/Cylinder")
        self.Cylinder2.reparentTo(render)
        self.Cylinder2.setScale(8,8,0.2)
        self.Cylinder2.setPos(-15,-250,110)
        self.Cylinder2.setTexture(blocks_tex6, 1)
        radius = 8
        height = 1
        shape17 = BulletCylinderShape(radius, height, ZUp)
        self.node17 = BulletRigidBodyNode('Cylinder2')
        self.node17.setMass(0)
        self.node17.addShape(shape17)
        self.np17 = render.attachNewNode(self.node17)
        self.np17.setPos(-15, -250, 110)
        self.np17.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.node17)
        
        
        
        self.Cylinder3= loader.loadModel("models/Cylinder/Cylinder")
        self.Cylinder3.reparentTo(render)
        self.Cylinder3.setScale(8,8,0.2)
        self.Cylinder3.setPos(-25,-270,112)
        self.Cylinder3.setTexture(blocks_tex6, 1)
        radius = 8
        height = 1
        shape18 = BulletCylinderShape(radius, height, ZUp)
        self.node18 = BulletRigidBodyNode('Cylinder3')
        self.node18.setMass(0)
        self.node18.addShape(shape18)
        self.np18 = render.attachNewNode(self.node18)
        self.np18.setPos(-25, -270, 112)
        self.np18.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.node18)
        
        
        self.Cylinder4= loader.loadModel("models/Cylinder/Cylinder")
        self.Cylinder4.reparentTo(render)
        self.Cylinder4.setScale(8,8,0.2)
        self.Cylinder4.setPos(-30,-290,114)
        self.Cylinder4.setTexture(blocks_tex6, 1)
        radius = 8
        height = 1
        shape19 = BulletCylinderShape(radius, height, ZUp)
        self.node19 = BulletRigidBodyNode('Cylinder4')
        self.node19.setMass(0)
        self.node19.addShape(shape19)
        self.np19 = render.attachNewNode(self.node19)
        self.np19.setPos(-30, -290, 114)
        self.np19.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.node19)
        
        
        self.fire= loader.loadModel("models/stop_sign/stop_sign")
        self.fire.setScale(0.01)
        self.fire.reparentTo(render)
        self.fire.setPos(-30,-290,114+6)
        
        
        
        self.shape7 = BulletBoxShape(Vec3(8, 8, 0.75))
        self.node7= BulletRigidBodyNode('Box7')
        self.node7.setMass(0)
        self.node7.addShape(self.shape7)
        self.np7 = render.attachNewNode(self.node7)
        self.np7.setPos(0, 0, 200)
        self.np7.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.node7) 
        self.box7= loader.loadModel("models/box/box1")
        self.box7.reparentTo(render)
        self.box7.setScale(10,10,0.2)
        self.box7.setPos(0, 0, 200)
        
        

        
        #setup the items to be collected 
        self.setupItems()   
        self.setupEndPoint()
        
    
        
 
        

        

    
    def setupEndPoint(self):
        
        blocks_tex8 = loader.loadTexture("models/blocks_tex8.jpg")

        self.endpoint= loader.loadModel("models/Sphere_HighPoly/Sphere_HighPoly")
        self.endpoint.reparentTo(render)
        self.endpoint.setScale(.5)
        self.endpoint.setPos(0,0,202)
        self.endpoint.setTexture(blocks_tex8, 1)
        radius = 2.65
        self.shapeEnd = BulletSphereShape(radius)
        self.nodeEnd = BulletGhostNode('EndPoint')
        self.nodeEnd.addShape(self.shapeEnd)
        self.npEnd = render.attachNewNode(self.nodeEnd)
        self.npEnd.setPos(0, 5, 202)
        self.npEnd.setCollideMask(BitMask32.allOn())
        self.world.attachGhost(self.nodeEnd)
        
        
    def setupItems(self):
        
        #############Items########################################
        
        self.iteamsModelsList = [0] * 50
        self.iteamsNodesList = [0] * 50
        self.iteamsNpsList = [0] * 50


        self.index = 0        
            
        for i in range(5):
            x = 4 + i 
            y = -20 + i
            t1= loader.loadModel("models/Torus/Torus")
            t1.reparentTo(render)
            t1.setScale(.6)
            t1.setPos(x,y,104)
            t1.setHpr(0,90,0)
            radius = .8
            height = .5
            shape19 = BulletCylinderShape(radius, height, ZUp)
            nodet1 = BulletGhostNode('t1')
            nodet1.addShape(shape19)
            npt1 = render.attachNewNode(nodet1)
            npt1.setPos(x, y, 104)
            npt1.setHpr(0,90,0)
            npt1.setCollideMask(BitMask32.allOn())
            self.world.attachGhost(nodet1)
            
            self.iteamsModelsList[self.index] = t1
            self.iteamsNodesList[self.index] = nodet1
            self.iteamsNpsList[self.index] = npt1            
            
            self.index += 1
            
            
        for i in range(5):
            x = -4 + i 
            y = -42 + i
            t1= loader.loadModel("models/Torus/Torus")
            t1.reparentTo(render)
            t1.setScale(.6)
            t1.setPos(x,y,106)
            t1.setHpr(0,90,0)
            radius = .8
            height = .5
            shape19 = BulletCylinderShape(radius, height, ZUp)
            nodet1 = BulletGhostNode('t1')
            nodet1.addShape(shape19)
            npt1 = render.attachNewNode(nodet1)
            npt1.setPos(x, y, 106)
            npt1.setHpr(0,90,0)
            npt1.setCollideMask(BitMask32.allOn())
            self.world.attachGhost(nodet1)
            
            self.iteamsModelsList[self.index] = t1
            self.iteamsNodesList[self.index] = nodet1
            self.iteamsNpsList[self.index] = npt1            
            
            self.index += 1
            
        for i in range(5):
            x = -25 + i 
            y = -42 + i
            t1= loader.loadModel("models/Torus/Torus")
            t1.reparentTo(render)
            t1.setScale(.6)
            t1.setPos(x,y,106)
            t1.setHpr(0,90,0)
            radius = .8
            height = .5
            shape19 = BulletCylinderShape(radius, height, ZUp)
            nodet1 = BulletGhostNode('t1')
            nodet1.addShape(shape19)
            npt1 = render.attachNewNode(nodet1)
            npt1.setPos(x, y, 106)
            npt1.setHpr(0,90,0)
            npt1.setCollideMask(BitMask32.allOn())
            self.world.attachGhost(nodet1)
            
            self.iteamsModelsList[self.index] = t1
            self.iteamsNodesList[self.index] = nodet1
            self.iteamsNpsList[self.index] = npt1            
            
            self.index += 1
            
        for i in range(5):
            x = -25 + i 
            y = -64 + i
            t1= loader.loadModel("models/Torus/Torus")
            t1.reparentTo(render)
            t1.setScale(.6)
            t1.setPos(x,y,106)
            t1.setHpr(0,90,0)
            radius = .8
            height = .5
            shape19 = BulletCylinderShape(radius, height, ZUp)
            nodet1 = BulletGhostNode('t1')
            nodet1.addShape(shape19)
            npt1 = render.attachNewNode(nodet1)
            npt1.setPos(x, y, 106)
            npt1.setHpr(0,90,0)
            npt1.setCollideMask(BitMask32.allOn())
            self.world.attachGhost(nodet1)
            
            self.iteamsModelsList[self.index] = t1
            self.iteamsNodesList[self.index] = nodet1
            self.iteamsNpsList[self.index] = npt1            
            
            self.index += 1
            
        for i in range(5):
            x = -22
            y = -120 - (i*10)
            t1= loader.loadModel("models/Torus/Torus")
            t1.reparentTo(render)
            t1.setScale(.6)
            t1.setPos(x,y,108)
            t1.setHpr(0,90,0)
            radius = .8
            height = .5
            shape19 = BulletCylinderShape(radius, height, ZUp)
            nodet1 = BulletGhostNode('t1')
            nodet1.addShape(shape19)
            npt1 = render.attachNewNode(nodet1)
            npt1.setPos(x, y, 108)
            npt1.setHpr(0,90,0)
            npt1.setCollideMask(BitMask32.allOn())
            self.world.attachGhost(nodet1)
            
            self.iteamsModelsList[self.index] = t1
            self.iteamsNodesList[self.index] = nodet1
            self.iteamsNpsList[self.index] = npt1            
            
            self.index += 1
            
            
        t1= loader.loadModel("models/Torus/Torus")
        t1.reparentTo(render)
        t1.setScale(.6)
        t1.setPos(self.Cylinder1.getX(),self.Cylinder1.getY(),self.Cylinder1.getZ()+2)
        t1.setHpr(0,90,0)
        radius = .8
        height = .5
        shape19 = BulletCylinderShape(radius, height, ZUp)
        nodet1 = BulletGhostNode('t1')
        nodet1.addShape(shape19)
        npt1 = render.attachNewNode(nodet1)
        npt1.setPos(self.Cylinder1.getX(),self.Cylinder1.getY(),self.Cylinder1.getZ()+2)
        npt1.setHpr(0,90,0)
        npt1.setCollideMask(BitMask32.allOn())
        self.world.attachGhost(nodet1)
            
        self.iteamsModelsList[self.index] = t1
        self.iteamsNodesList[self.index] = nodet1
        self.iteamsNpsList[self.index] = npt1            
            
        self.index += 1
            
        t1= loader.loadModel("models/Torus/Torus")
        t1.reparentTo(render)
        t1.setScale(.6)
        t1.setPos(self.Cylinder2.getX(),self.Cylinder2.getY(),self.Cylinder2.getZ()+2)
        t1.setHpr(0,90,0)
        radius = .8
        height = .5
        shape19 = BulletCylinderShape(radius, height, ZUp)
        nodet1 = BulletGhostNode('t1')
        nodet1.addShape(shape19)
        npt1 = render.attachNewNode(nodet1)
        npt1.setPos(self.Cylinder2.getX(),self.Cylinder2.getY(),self.Cylinder2.getZ()+2)
        npt1.setHpr(0,90,0)
        npt1.setCollideMask(BitMask32.allOn())
        self.world.attachGhost(nodet1)
            
        self.iteamsModelsList[self.index] = t1
        self.iteamsNodesList[self.index] = nodet1
        self.iteamsNpsList[self.index] = npt1            
            
        self.index += 1
            
            
        t1= loader.loadModel("models/Torus/Torus")
        t1.reparentTo(render)
        t1.setScale(.6)
        t1.setPos(self.Cylinder3.getX(),self.Cylinder3.getY(),self.Cylinder3.getZ()+2)
        t1.setHpr(0,90,0)
        radius = .8
        height = .5
        shape19 = BulletCylinderShape(radius, height, ZUp)
        nodet1 = BulletGhostNode('t1')
        nodet1.addShape(shape19)
        npt1 = render.attachNewNode(nodet1)
        npt1.setPos(self.Cylinder3.getX(),self.Cylinder3.getY(),self.Cylinder3.getZ()+2)
        npt1.setHpr(0,90,0)
        npt1.setCollideMask(BitMask32.allOn())
        self.world.attachGhost(nodet1)
            
        self.iteamsModelsList[self.index] = t1
        self.iteamsNodesList[self.index] = nodet1
        self.iteamsNpsList[self.index] = npt1            
            
        self.index += 1
        
        
        

            
            

            
            
            




        
 

            
            
        