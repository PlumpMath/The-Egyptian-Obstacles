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


class Models(object):


    def __init__(self):
        
        self.setup()
        
        
        self.angel = 1

               
        # Set up the environment
        #
        self.environ = loader.loadModel("models/square")      
        self.environ.reparentTo(render)
        self.environ.setPos(0,0,0)
        self.environ.setScale(3000,3000,1)
        self.desert_tex = loader.loadTexture("models/desert.jpg")
        self.environ.setTexture(self.desert_tex, 1)
        
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
        
        
        
        #BoxPyramid1
        self.pyramid1 = loader.loadModel("models/pyramid/Pyramid")
        self.pyramid1.reparentTo(render)
        self.pyramid1.setScale(.5)
        self.pyramid1.setPos(0,-400,0)
        
        mesh = BulletTriangleMesh()
        for geomNP in self.pyramid1.findAllMatches('**/+GeomNode'):
            geomNode = geomNP.node()
            ts = geomNP.getTransform(self.pyramid1)
            for geom in geomNode.getGeoms():
                mesh.addGeom(geom, ts)
                
                
        shape2 = BulletTriangleMeshShape(mesh, dynamic=False)
        self.node = BulletRigidBodyNode('BoxPyramid1')
        self.node.setMass(0)
        self.node.addShape(shape2)
        self.np = render.attachNewNode(self.node)
        self.np.setPos(0, -400, 0)
        self.np.setScale(1.65)
        self.np.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.node)
        
        
        #BoxPyramid2
        self.pyramid2 = loader.loadModel("models/pyramid/Pyramid")
        self.pyramid2.reparentTo(render)
        self.pyramid2.setScale(.25)
        self.pyramid2.setPos(180,-400,0)
        
        mesh2 = BulletTriangleMesh()
        for geomNP in self.pyramid2.findAllMatches('**/+GeomNode'):
            geomNode = geomNP.node()
            ts = geomNP.getTransform(self.pyramid2)
            for geom in geomNode.getGeoms():
                mesh2.addGeom(geom, ts)
                
        shape3 = BulletTriangleMeshShape(mesh2, dynamic=False)
        self.node3 = BulletRigidBodyNode('BoxPyramid2')
        self.node3.setMass(0)
        self.node3.addShape(shape3)
        self.np3 = render.attachNewNode(self.node3)
        self.np3.setPos(180, -400, 0)
        self.np3.setScale(0.85)
        self.np3.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.node3)
        
        
        #BoxPyramid3
        self.pyramid3 = loader.loadModel("models/pyramid/Pyramid")
        self.pyramid3.reparentTo(render)
        self.pyramid3.setScale(.25)
        self.pyramid3.setPos(-180,-400,0)
        
        mesh3 = BulletTriangleMesh()
        for geomNP in self.pyramid3.findAllMatches('**/+GeomNode'):
            geomNode = geomNP.node()
            ts = geomNP.getTransform(self.pyramid3)
            for geom in geomNode.getGeoms():
                mesh3.addGeom(geom, ts)
                
                
        shape4 = BulletTriangleMeshShape(mesh2, dynamic=False)
        self.node4 = BulletRigidBodyNode('BoxPyramid3')
        self.node4.setMass(0)
        self.node4.addShape(shape4)
        self.np4 = render.attachNewNode(self.node4)
        self.np4.setPos(-180, -400, 0)
        self.np4.setScale(0.85)
        self.np4.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.node4)
        
        
        #BoxSphinx       
        self.sphinx = loader.loadModel("models/sphinx/Sphinx")
        self.sphinx.reparentTo(render)
        self.sphinx.setScale(.08)
        self.sphinx.setPos(100,-50,20)
        shape5 = BulletBoxShape(Vec3(18, 55, 30))
        self.node5 = BulletRigidBodyNode('BoxSphinx')
        self.node5.setMass(0)
        self.node5.addShape(shape5)
        self.np5 = render.attachNewNode(self.node5)
        self.np5.setPos(100, -50, 10)
        self.np5.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.node5)
            
    
        
        #start
        blocks_tex6 = loader.loadTexture("models/blocks_tex6.jpg")


   
        
        self.box1= loader.loadModel("models/box/box3")
        self.box1.reparentTo(render)
        self.box1.setScale(10,400,10)
        self.box1.setPos(-300,850,0)
        shape8 = BulletBoxShape(Vec3(8, 315, 13.5))
        self.node8 = BulletRigidBodyNode('Box1')
        self.node8.setMass(0)
        self.node8.addShape(shape8)
        self.np8 = render.attachNewNode(self.node8)
        self.np8.setPos(-300, 850, 10)
        self.np8.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.node8) 
        
        
        self.box2= loader.loadModel("models/box/box3")
        self.box2.reparentTo(render)
        self.box2.setScale(10,400,10)
        self.box2.setPos(-350,850,0)
        shape9 = BulletBoxShape(Vec3(8, 315, 13.5))
        self.node9 = BulletRigidBodyNode('Box2')
        self.node9.setMass(0)
        self.node9.addShape(shape9)
        self.np9 = render.attachNewNode(self.node9)
        self.np9.setPos(-350, 850, 10)
        self.np9.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.node9) 
        
        
        self.box3= loader.loadModel("models/box/box4")
        self.box3.reparentTo(render)
        self.box3.setScale(40,10,10)
        self.box3.setPos(-325,543,0)
        shape10 = BulletBoxShape(Vec3(30, 8, 13.5))
        self.node10 = BulletRigidBodyNode('Box3')
        self.node10.setMass(0)
        self.node10.addShape(shape10)
        self.np10 = render.attachNewNode(self.node10)
        self.np10.setPos(-325, 543, 10)
        self.np10.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.node10) 
        
        self.box4= loader.loadModel("models/box/box4")
        self.box4.reparentTo(render)
        self.box4.setScale(40,10,10)
        self.box4.setPos(-325,1157,0)
        shape11 = BulletBoxShape(Vec3(30, 8, 13.5))
        self.node11 = BulletRigidBodyNode('Box4')
        self.node11.setMass(0)
        self.node11.addShape(shape11)
        self.np11 = render.attachNewNode(self.node11)
        self.np11.setPos(-325, 1157, 10)
        self.np11.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.node11) 
        
        
        #Stars 1
        self.stairsList = [0] * 10
        self.stairsListNp = [0] * 10

        
        n5 = 0
        for i in range(10):
            n5 += 2
            self.stairsList[i]= loader.loadModel("models/box/box1")
            self.stairsList[i].reparentTo(render)
            self.stairsList[i].setScale(1.3)
            self.stairsList[i].setPos(-325,925-(n5*1.2),n5)
            self.stairsList[i].setHpr(0,0,90)
            shape6 = BulletBoxShape(Vec3(3.2, 1.1, 1.1))
            node6 = BulletRigidBodyNode('Box5 '+str(i))
            node6.setMass(0)
            node6.addShape(shape6)
            self.stairsListNp[i] = render.attachNewNode(node6)
            self.stairsListNp[i].setPos(-325, 925-(n5*1.2), n5)
            self.stairsListNp[i].setCollideMask(BitMask32.allOn())
            self.world.attachRigidBody(node6) 
            
        self.n5Upstairs = n5
        
        self.box6= loader.loadModel("models/box/box1")
        self.box6.reparentTo(render)
        self.box6.setScale(10,87,0.2)
        self.box6.setPos(-325,829,n5)
        self.shape12 = BulletBoxShape(Vec3(8, 70, 0.75))
        self.node12 = BulletRigidBodyNode('Box6')
        self.node12.setMass(0)
        self.node12.addShape(self.shape12)
        self.np12 = render.attachNewNode(self.node12)
        self.np12.setPos(-325, 829, n5)
        self.np12.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.node12) 
        
        
        
        self.box7= loader.loadModel("models/box/box2")
        self.box7.reparentTo(render)
        self.box7.setScale(5,12,0.25)
        self.box7.setPos(-325,749,n5)
        shape13 = BulletBoxShape(Vec3(4, 10, 0.8))
        self.node13 = BulletRigidBodyNode('Box7')
        self.node13.setMass(0)
        self.node13.addShape(shape13)
        self.np13 = render.attachNewNode(self.node13)
        self.np13.setPos(-325, 749, n5)
        self.np13.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.node13)
        
        
        box7Interval1 = self.box7.posInterval(3.3, Point3(-325, 749, n5+5),
        startPos=Point3(-325, 749, n5-5))
        np13Interval1 = self.np13.posInterval(3, Point3(-325, 749, n5+5),
        startPos=Point3(-325, 749, n5-5))
        box7Interval2 = self.box7.posInterval(3.3, Point3(-325, 749, n5-5),
        startPos=Point3(-325, 749, n5+5))
        np13Interval2 = self.np13.posInterval(3, Point3(-325, 749, n5-5),
        startPos=Point3(-325, 749, n5+5)) 
             
        self.box7Pace = Sequence(Parallel(box7Interval1,np13Interval1),
                                 Parallel(box7Interval2,np13Interval2),
                                 name="box7Pace")
        self.box7Pace.loop() 
        
        
        
        self.box8= loader.loadModel("models/box/box2")
        self.box8.reparentTo(render)
        self.box8.setScale(5,12,0.25)
        self.box8.setPos(-325,725,n5)
        shape14 = BulletBoxShape(Vec3(4, 10, 0.8))
        node14 = BulletRigidBodyNode('Box8')
        node14.setMass(0)
        node14.addShape(shape14)
        self.np14 = render.attachNewNode(node14)
        self.np14.setPos(-325, 725, n5)
        self.np14.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(node14)
        
        
        box8Interval1 = self.box8.posInterval(3.3, Point3(-325, 725, n5-5),
        startPos=Point3(-325, 725, n5+5))
        np14Interval1 = self.np14.posInterval(3, Point3(-325, 725, n5-5),
        startPos=Point3(-325, 725, n5+5))
        box8Interval2 = self.box8.posInterval(3.3, Point3(-325, 725, n5+5),
        startPos=Point3(-325, 725, n5-5))
        np14Interval2 = self.np14.posInterval(3, Point3(-325, 725, n5+5),
        startPos=Point3(-325, 725, n5-5)) 
             
        self.box8Pace = Sequence(Parallel(box8Interval1,np14Interval1),
                                 Parallel(box8Interval2,np14Interval2),
                                 name="box8Pace")
        self.box8Pace.loop() 
        

        self.Cylinder1= loader.loadModel("models/Cylinder/Cylinder")
        self.Cylinder1.reparentTo(render)
        self.Cylinder1.setScale(8,8,0.2)
        self.Cylinder1.setPos(-322,700,n5)
        self.Cylinder1.setTexture(blocks_tex6, 1)
        radius = 8
        height = 1
        shape16 = BulletCylinderShape(radius, height, ZUp)
        self.node16 = BulletRigidBodyNode('Cylinder1')
        self.node16.setMass(0)
        self.node16.addShape(shape16)
        self.np16 = render.attachNewNode(self.node16)
        self.np16.setPos(-322, 700, n5)
        self.np16.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.node16)
        
        
        self.Cylinder2= loader.loadModel("models/Cylinder/Cylinder")
        self.Cylinder2.reparentTo(render)
        self.Cylinder2.setScale(8,8,0.2)
        self.Cylinder2.setPos(-327,680,n5)
        self.Cylinder2.setTexture(blocks_tex6, 1)
        radius = 8
        height = 1
        shape17 = BulletCylinderShape(radius, height, ZUp)
        self.node17 = BulletRigidBodyNode('Cylinder2')
        self.node17.setMass(0)
        self.node17.addShape(shape17)
        self.np17 = render.attachNewNode(self.node17)
        self.np17.setPos(-327, 680, n5)
        self.np17.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.node17)
        
        
        
        self.Cylinder3= loader.loadModel("models/Cylinder/Cylinder")
        self.Cylinder3.reparentTo(render)
        self.Cylinder3.setScale(8,8,0.2)
        self.Cylinder3.setPos(-322,660,n5)
        self.Cylinder3.setTexture(blocks_tex6, 1)
        radius = 8
        height = 1
        shape18 = BulletCylinderShape(radius, height, ZUp)
        self.node18 = BulletRigidBodyNode('Cylinder3')
        self.node18.setMass(0)
        self.node18.addShape(shape18)
        self.np18 = render.attachNewNode(self.node18)
        self.np18.setPos(-322, 660, n5)
        self.np18.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.node18)
        
        
        self.Cylinder4= loader.loadModel("models/Cylinder/Cylinder")
        self.Cylinder4.reparentTo(render)
        self.Cylinder4.setScale(8,8,0.2)
        self.Cylinder4.setPos(-327,640,n5)
        self.Cylinder4.setTexture(blocks_tex6, 1)
        radius = 8
        height = 1
        shape19 = BulletCylinderShape(radius, height, ZUp)
        self.node19 = BulletRigidBodyNode('Cylinder4')
        self.node19.setMass(0)
        self.node19.addShape(shape19)
        self.np19 = render.attachNewNode(self.node19)
        self.np19.setPos(-327, 640, n5)
        self.np19.setCollideMask(BitMask32.allOn())
        self.world.attachRigidBody(self.node19)
        
        
        self.fire= loader.loadModel("models/stop_sign/stop_sign")
        self.fire.setScale(0.01)
        self.fire.reparentTo(render)
        self.fire.setPos(-327,640,n5+5)
        
        #setup the items to be collected 
        self.setupItems()
        
        self.setupEndPoint()
        
    
        
 
        #################End point###################################
        

        

    
    def setupEndPoint(self):
        
        blocks_tex8 = loader.loadTexture("models/blocks_tex8.jpg")

        self.endpoint= loader.loadModel("models/Sphere_HighPoly/Sphere_HighPoly")
        self.endpoint.reparentTo(render)
        self.endpoint.setScale(.8)
        self.endpoint.setPos(0,-200,2)
        self.endpoint.setTexture(blocks_tex8, 1)
        radius = 2.65
        self.shapeEnd = BulletSphereShape(radius)
        self.nodeEnd = BulletGhostNode('EndPoint')
        self.nodeEnd.addShape(self.shapeEnd)
        self.npEnd = render.attachNewNode(self.nodeEnd)
        self.npEnd.setPos(0, -200, 2)
        self.npEnd.setCollideMask(BitMask32.allOn())
        self.world.attachGhost(self.nodeEnd)
        
        
    def setupItems(self):
        
        #############Items########################################
        
        self.iteamsModelsList = [0] * 50
        self.iteamsNodesList = [0] * 50
        self.iteamsNpsList = [0] * 50


        self.index = 0        
            
        n6 = 0
        for i in range(10):
            
            t1= loader.loadModel("models/Torus/Torus")
            t1.reparentTo(render)
            t1.setScale(.6)
            t1.setPos(-325,925-(n6*1.2),n6+2)
            t1.setHpr(0,90,0)
            radius = .8
            height = .5
            shape19 = BulletCylinderShape(radius, height, ZUp)
            nodet1 = BulletGhostNode('t1')
            nodet1.addShape(shape19)
            npt1 = render.attachNewNode(nodet1)
            npt1.setPos(-325, 925-(n6*1.2), n6+2)
            npt1.setHpr(0,90,0)
            npt1.setCollideMask(BitMask32.allOn())
            self.world.attachGhost(nodet1)
            
            self.iteamsModelsList[self.index] = t1
            self.iteamsNodesList[self.index] = nodet1
            self.iteamsNpsList[self.index] = npt1            
            
            n6  += 2
            self.index += 1
            
            
        n7 = 20
        for i in range(5):
            
            t1= loader.loadModel("models/Torus/Torus")
            t1.reparentTo(render)
            t1.setScale(.6)
            t1.setPos(-325,880-n7,n6+2)
            t1.setHpr(0,90,0)
            radius = .8
            height = .5
            shape19 = BulletCylinderShape(radius, height, ZUp)
            nodet1 = BulletGhostNode('t1')
            nodet1.addShape(shape19)
            npt1 = render.attachNewNode(nodet1)
            npt1.setPos(-325, 880-n7, n6+2)
            npt1.setHpr(0,90,0)
            npt1.setCollideMask(BitMask32.allOn())
            self.world.attachGhost(nodet1)
            
            self.iteamsModelsList[self.index] = t1
            self.iteamsNodesList[self.index] = nodet1
            self.iteamsNpsList[self.index] = npt1            
            
            n7  += 20
            self.index += 1
            
   
        t1= loader.loadModel("models/Torus/Torus")
        t1.reparentTo(render)
        t1.setScale(.6)
        t1.setPos(self.Cylinder1.getX(),self.Cylinder1.getY(),n6+2)
        t1.setHpr(0,90,0)
        radius = .8
        height = .5
        shape19 = BulletCylinderShape(radius, height, ZUp)
        nodet1 = BulletGhostNode('t1')
        nodet1.addShape(shape19)
        npt1 = render.attachNewNode(nodet1)
        npt1.setPos(self.Cylinder1.getX(),self.Cylinder1.getY(),n6+2)
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
        t1.setPos(self.Cylinder2.getX(),self.Cylinder2.getY(),n6+2)
        t1.setHpr(0,90,0)
        radius = .8
        height = .5
        shape19 = BulletCylinderShape(radius, height, ZUp)
        nodet1 = BulletGhostNode('t1')
        nodet1.addShape(shape19)
        npt1 = render.attachNewNode(nodet1)
        npt1.setPos(self.Cylinder2.getX(),self.Cylinder2.getY(),n6+2)
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
        t1.setPos(self.Cylinder3.getX(),self.Cylinder3.getY(),n6+2)
        t1.setHpr(0,90,0)
        radius = .8
        height = .5
        shape19 = BulletCylinderShape(radius, height, ZUp)
        nodet1 = BulletGhostNode('t1')
        nodet1.addShape(shape19)
        npt1 = render.attachNewNode(nodet1)
        npt1.setPos(self.Cylinder3.getX(),self.Cylinder3.getY(),n6+2)
        npt1.setHpr(0,90,0)
        npt1.setCollideMask(BitMask32.allOn())
        self.world.attachGhost(nodet1)
            
        self.iteamsModelsList[self.index] = t1
        self.iteamsNodesList[self.index] = nodet1
        self.iteamsNpsList[self.index] = npt1            
            
        self.index += 1
        

        
            
            
        n6 = 0
        for i in range(30):
            x = random.randint(-50, 50)
            y = random.randint(-50, 50) 
            t1= loader.loadModel("models/Torus/Torus")
            t1.reparentTo(render)
            t1.setScale(.6)
            t1.setPos(x,y,2)
            t1.setHpr(0,90,0)
            radius = .8
            height = .5
            shape19 = BulletCylinderShape(radius, height, ZUp)
            nodet1 = BulletGhostNode('t1')
            nodet1.addShape(shape19)
            npt1 = render.attachNewNode(nodet1)
            npt1.setPos(x, y, 2)
            npt1.setHpr(0,90,0)
            npt1.setCollideMask(BitMask32.allOn())
            self.world.attachGhost(nodet1)
            
            self.iteamsModelsList[self.index] = t1
            self.iteamsNodesList[self.index] = nodet1
            self.iteamsNpsList[self.index] = npt1            
            
            n6  += 2
            self.index += 1
            
            
            

        
        
 

            
            
        