import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from time import sleep
from pyEMS import openEMSstim
from pyEMS.EMSCommand import ems_command
from pyEMS import openEMSstim
from random import randint 
import predict

from predict import predict
from predict import getAnswer
# sys.path.append("../Leapmotion-GesturePredicted")
# import Sample
# from Sample import predict
# from Sample import getAnswer


my_ems_board = openEMSstim.openEMSstim("/dev/tty.usbserial-A9WRN9D1",19200)

class GifImage(QLabel):
    def __init__(self, *args): #gifname time life
        super(GifImage, self).__init__()
        self.movie = QMovie(args[1])
        self.setMovie(self.movie)
        self.movie.start()
        self.movie.stop()    
        self.timedelay = int(args[2])
        self.life = args[3]

  
    def start(self):
        self.movie.start() 
        QSound.play("music/middle_kick.mp3")
    def playAN(self,nowlife):
        self.life = nowlife
        self.timer = QTimer()
        self.timer.singleShot(self.timedelay,self.start)
        self.timer.singleShot(self.timedelay+1200,self.cc)

    def cc(self):
        if self.life == 2:
            self.movie.setFileName("photo/full_1.gif")
            
        elif self.life == 1:
            self.movie.setFileName("photo/full_2.gif")
            #QSound.play("music/middle_kick.mp3")
        self.setMovie(self.movie)
        self.movie.start()
        self.movie.stop()
    def reset(self):
        self.movie.setFileName("photo/full.gif")
        self.setMovie(self.movie)
        self.movie.start()
        self.movie.stop()


    

class HoverButton(QPushButton):

    def __init__(self,  *args):
        super(HoverButton, self).__init__()
        self.setMouseTracking(True)
        self.setFlat(True)
        self.ph1 = args[1]
        self.ph2 = args[2]
        self.setIcon(QIcon(args[1]))
        

     

    
    def enterEvent(self,event):
        #print("Enter")
        self.setIcon(QIcon(self.ph2))

        
    def leaveEvent(self,event):
        #print("Leave")
        self.setIcon(QIcon(self.ph1))

class HoverButton1(QPushButton):

    def __init__(self,  *args):
        super(HoverButton1, self).__init__()
        self.setMouseTracking(True)
        self.setText(args[1])
        self.ph1 = args[2]+";width:202px;height:46px; border-radius: 15px;margin-right:60p;"
        self.ph2 = args[3]+";width:202px;height:46px; border-radius: 15px;margin-right:60p;"
        self.setStyleSheet(self.ph1)
    
    def enterEvent(self,event):
        #print("Enter")
        self.setStyleSheet(self.ph2)
    def leaveEvent(self,event):
        #print("Leave")
        self.setStyleSheet(self.ph1)




class MainWindow(QStackedWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(0,0,1440,1080)
        #self.setStyleSheet("background-color:white")
        self.setWindowTitle("Rock Paper Scissors")
        global pic
        global idensity1
        self.idensity1 = 10
        global idensity2
        self.idensity2 = 10

        predict()

        pic = QLabel(self)
        pic.setScaledContents(True)
        pic.setGeometry(0,0,1440,1000)
        pic.setPixmap(QPixmap("photo/title4.jpg")) 
        window = QWidget()

        go = HoverButton1(window,"EASY","font-size:20px;background-color:#5F5C5C;\
                          color:#E4E4E4","font-size:25px;background-color:#3c393a;color:#ffffff")

        hard = HoverButton1(window,"HARD","font-size:20px;background-color:#5F5C5C;\
                          color:#E4E4E4","font-size:25px;background-color:#3c393a;color:#ffffff")
        
        

        seting = HoverButton(window,"photo/settings.png","photo/settings1.png")
        seting.setIconSize(QSize(33,33))
        

        h1 = QHBoxLayout()
        #h1.addStretch(1)
        h1.addWidget(go,0,Qt.AlignCenter)
        h2 = QHBoxLayout()
        h2.addWidget(hard,0,Qt.AlignCenter)

        h3 = QHBoxLayout()
        h3.addStretch(1)
        h3.addWidget(seting)

        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addLayout(h1)
        layout.addLayout(h2)
        layout.addLayout(h3)

        go.clicked.connect(lambda: self.ReadyStart(1))
        hard.clicked.connect(lambda: self.ReadyStart(2))
        seting.clicked.connect(self.setpage)
       
        window.setLayout(layout)
        self.addWidget(window)
        self.setCurrentWidget(window)
        

    def ReadyStart(self, mode):

        print "Mode:",
        print mode
        print self.idensity1
        print self.idensity2
        pic.hide()
        global window2
        window2 = QWidget()
        window2.setStyleSheet("background-color:white")


        global leftlife
        leftlife = 3
        global rightlife
        rightlife = 3

        global roundlabel
        roundlabel = QLabel("")
        roundlabel.setFont(QFont("SWLINK",90,QFont.Bold))
        til = QHBoxLayout()
        til.addWidget(roundlabel, 0, Qt.AlignCenter)

        global pp
        pp = QLabel()
        global movie 
        movie = QMovie("photo/newR1.gif")
        pp.setMovie(movie)
        movie.start()

        global bloodleft
        global bloodright
        bloodleft = GifImage(window2, "photo/full.gif",1600,2)
        bloodright = GifImage(window2, "photo/full.gif",1600,3)
       
        

        ho = QHBoxLayout()
        ho.addWidget(bloodleft, 0, Qt.AlignCenter)
        ho.addWidget(bloodright, 0, Qt.AlignCenter)  

        global leftplayer_Ges
        global rightplayer_Ges
        leftplayer_Ges = QLabel("")
        rightplayer_Ges = QLabel("")
        leftplayer_Ges.setFont(QFont("SWLINK",30,QFont.Bold))
        rightplayer_Ges.setFont(QFont("SWLINK",30,QFont.Bold))
        h1 = QHBoxLayout()
        h1.addWidget(leftplayer_Ges, 0, Qt.AlignCenter)
        h1.addWidget(rightplayer_Ges, 0, Qt.AlignCenter)

        QSound.play("music/st.mp3")


        layout = QVBoxLayout()
        layout.addStretch()
        layout.addLayout(til)
        layout.addStretch()
        layout.addLayout(ho)
        layout.addLayout(h1)
        layout.addWidget(pp, 0, Qt.AlignCenter)
        layout.addStretch()
        window2.setLayout(layout)
        
        self.addWidget(window2)
        self.setCurrentWidget(window2)
        self.timer = QTimer()
        self.timer.singleShot(3100, lambda: self.Roundnumber("ROUND1",1))     
        self.timer.singleShot(4700, lambda: self.EMS(self.idensity1 , self.idensity2, mode))
        self.timer.singleShot(5000, lambda: self.Result())
        # self.timer.singleShot(7000, lambda: self.changebloodGif(leftmovie,"photo/full_1.gif")) 

          
        self.timer.singleShot(8000, lambda: self.changeGif(movie,"photo/newR2.gif")) 
        self.timer.singleShot(8000, lambda: self.Roundnumber("",0))  
        self.timer.singleShot(11100, lambda: self.Roundnumber("ROUND2",1))   
        self.timer.singleShot(12700, lambda: self.EMS(self.idensity1 , self.idensity2, mode))
        self.timer.singleShot(13000, lambda: self.Result())

        #self.timer.singleShot(19000, lambda: self.changeGif("photo/R3.gif")) 
        #self.timer.singleShot(24000, lambda: self.EMS(self.idensity1 , self.idensity2, mode))
        
          
        self.timer.singleShot(16000, lambda: self.changeGif(movie,"photo/newR3.gif")) 
        self.timer.singleShot(16000, lambda: self.Roundnumber("",0))  
        self.timer.singleShot(19100, lambda: self.Roundnumber("ROUND3",1))   
        self.timer.singleShot(20700, lambda: self.EMS(self.idensity1 , self.idensity2, mode))
        self.timer.singleShot(21000, lambda: self.Result())

        #self.timer.singleShot(30000, lambda: self.Result())
        self.timer.singleShot(26000, lambda: self.finishPage(mode))

    def Roundnumber(self, te ,play):
        roundlabel.setText(te)
        leftplayer_Ges.setText("")
        rightplayer_Ges.setText("")
        if play==0:
            QSound.play("music/st.mp3")        
        if play==1:
            QSound.play("music/select01.mp3")
            self.timer = QTimer()
            self.timer.singleShot(666, lambda: self.playcountSound(1))
            self.timer.singleShot(1332, lambda: self.playcountSound(2))
        
    def playcountSound(self,music):
        if music==1:
            QSound.play("music/select01.mp3")      
        elif music==2:
            QSound.play("music/select02.mp3")
      



    def changeGif(self, mov, gifname):
        mov.stop()
        mov = QMovie(gifname)
        pp.setMovie(mov)
        mov.start()
 
    def EMS(self, i1, i2, mode):
        print mode
        print "ems",
        print i1, i2
        global righthand_number
        righthand_number = randint(1, 3)
        # lefthand_number = randint(1, 3)
        # try:
        #     lefthand_number = int(getAnswer())  
        # except ValueError:
        #     print "gggggggggg"
        #   
        lefthand_number = int(getAnswer())
        if lefthand_number == 0:
            print "no hand!"
        if mode == 1: #easy mode
            if righthand_number == 1:
                print "scissor",
                #print i1
                self.ScissorTest(5)
            elif righthand_number ==2:
                print "rock",
                #print i2
                self.RockTest(5)
                
            else:
                pass 
        elif mode == 2: #pi camera  hard mode
            if lefthand_number==3:#left is paper=>ems:scissor
                righthand_number=1
                #my_ems_board.send(ems_command(2,i2,1000))
                # ScissorTest(self)
                self.ScissorTest(5)
            else:#o.w
                righthand_number=lefthand_number+1
                if righthand_number==2:#ems:rock
                    #my_ems_board.send(ems_command(1,i1,1000))
                    #my_ems_board.send(ems_command(2,i1,1000))
                    self.RockTest(5)
                    

        print righthand_number,lefthand_number
        # timer = QTimer()
        # timer.singleShot(100, lambda: self.Result(righthand_number))
        
    #show result        
    def Result(self):
        ge = ["Scissors", "Rock", "Paper"]
        #left = int(getAnswer())
        # try:
        #     left = int(getAnswer())
        # except ValueError:
        #     self.changeGif(movie,"photo/stand.gif")
        left = int(getAnswer())
        print "tttttttttttt"
        print left
        print "tttttttttttt"
        if left == 0:
            self.changeGif(movie, "photo/stand.gif")

        else: 
            right = righthand_number
            #print right,left
            leftplayer_Ges.setText(ge[left-1])
            rightplayer_Ges.setText(ge[right-1])
            #left read by leamotion
            result=right-left
            #print 'fuckkkkkkk' + str(result)
            if result==0:#peace
                self.changeGif(movie,"photo/peace.gif")
                global rightlife
                bloodright.playAN(rightlife-1)  
                rightlife -=1 
                global leftlife
                bloodleft.playAN(leftlife-1) 
                leftlife -=1
            elif result==1 or result==-2:#ems win
                self.changeGif(movie,"photo/rightattack.gif")
                # global leftlife
                bloodleft.playAN(leftlife-1) 
                leftlife -=1
            else:
                self.changeGif(movie,"photo/leftattack.gif") 
                # global rightlife
                bloodright.playAN(rightlife-1)  
                rightlife -=1        


    def finishPage(self, mode):
        self.removeWidget(window2)
        global window3
        window3 = QWidget()
        window3.setStyleSheet("background-color:#fdfbed")
        pic1 = QLabel()
        pic1.setPixmap(QPixmap("photo/finishpage.jpg"))
        over = QLabel("GAME OVER")
        over.setFont(QFont("SWLINK",30,QFont.Bold))


        layout = QVBoxLayout()

        finish = HoverButton1(window3,"FINISH","font-size:20px;background-color:#5F5C5C;\
                          color:#E4E4E4","font-size:25px;background-color:#3c393a;color:#ffffff")
        finish.clicked.connect(self.gotohome)
        tryagain = HoverButton1(window3,"TRY AGAIN","font-size:20px;background-color:#5F5C5C;\
                          color:#E4E4E4","font-size:25px;background-color:#3c393a;color:#ffffff")
        tryagain.clicked.connect(lambda: self.restart(mode))
        
        h1 = QHBoxLayout()
        h1.addWidget(tryagain,0,Qt.AlignCenter)
        h2 = QHBoxLayout()
        h2.addWidget(finish,0,Qt.AlignCenter)


        
        layout.addWidget(pic1, 0, Qt.AlignHCenter)
        layout.addWidget(over, 0, Qt.AlignCenter)
        layout.addStretch()
        layout.addLayout(h1)
        layout.addLayout(h2)
        layout.addStretch()
        window3.setLayout(layout)
        self.addWidget(window3)
        self.setCurrentWidget(window3)



    def restart(self, mode):
        self.removeWidget(window3)
        self.addWidget(window2)
        self.setCurrentWidget(window2)

        leftplayer_Ges.setText("")
        rightplayer_Ges.setText("")

        global movie
        movie.stop()
        movie = QMovie("photo/newR1.gif")
        pp.setMovie(movie)
        movie.start()

        global leftlife
        global rightlife

        print "restart:", leftlife, rightlife


        leftlife = 3
        rightlife = 3

        print "restart:~~~", leftlife, rightlife


        bloodleft.reset()
        bloodright.reset()
        QSound.play("music/st.mp3")



        self.timer = QTimer()
        roundlabel.setText("")      
        self.timer.singleShot(3100, lambda: self.Roundnumber("ROUND1",1))     
        self.timer.singleShot(4700, lambda: self.EMS(self.idensity1 , self.idensity2, mode))
        self.timer.singleShot(5000, lambda: self.Result())
        # self.timer.singleShot(7000, lambda: self.changebloodGif(leftmovie,"photo/full_1.gif")) 

          
        self.timer.singleShot(8000, lambda: self.changeGif(movie,"photo/newR2.gif")) 
        self.timer.singleShot(8000, lambda: self.Roundnumber("",0))  
        self.timer.singleShot(11100, lambda: self.Roundnumber("ROUND2",1))   
        self.timer.singleShot(12700, lambda: self.EMS(self.idensity1 , self.idensity2, mode))
        self.timer.singleShot(13000, lambda: self.Result())

        #self.timer.singleShot(19000, lambda: self.changeGif("photo/R3.gif")) 
        #self.timer.singleShot(24000, lambda: self.EMS(self.idensity1 , self.idensity2, mode))
        
          
        self.timer.singleShot(16000, lambda: self.changeGif(movie,"photo/newR3.gif")) 
        self.timer.singleShot(16000, lambda: self.Roundnumber("",0))  
        self.timer.singleShot(19100, lambda: self.Roundnumber("ROUND3",1))   
        self.timer.singleShot(20700, lambda: self.EMS(self.idensity1 , self.idensity2, mode))
        self.timer.singleShot(21000, lambda: self.Result())

        #self.timer.singleShot(30000, lambda: self.Result())
        self.timer.singleShot(26000, lambda: self.finishPage(mode))

        
        

    def gotohome(self):
        #self.idensity1 = 10
        #self.idensity2 = 10
        self.removeWidget(window3)
        pic.show()




    def setpage(self):
        pic.hide()   
        global window1   
        window1 = QWidget()
        window1.setStyleSheet("background-color:#fdfbed")
        pic1 = QLabel()
        pic1.setPixmap(QPixmap("photo/set2.jpg")) 
        

        

        global Slabel
        Slabel=QLabel("Idensity:10")
        Slabel.setStyleSheet('font-size: 18pt;')
        global Rlabel
        Rlabel=QLabel("Idensity:10")
        Rlabel.setStyleSheet('font-size: 18pt;')
        

        layout = QVBoxLayout()
        

        global Sslider
        Sslider=QSlider(Qt.Horizontal)
        Sslider.setStyleSheet("QSlider::handle:horizontal {background-color:#3c393a;};")
        Sslider.setMinimum(10)
        Sslider.setMaximum(100)
        Sslider.setTickPosition(QSlider.TicksBelow)
        Sslider.setTickInterval(10)
        Sslider.valueChanged.connect(self.change_level1)

        global Rslider
        Rslider=QSlider(Qt.Horizontal)
        Rslider.setStyleSheet("QSlider::handle:horizontal {background-color:#3c393a;}")
        Rslider.setMinimum(10)
        Rslider.setMaximum(100)
        Rslider.setTickPosition(QSlider.TicksBelow)
        Rslider.setTickInterval(10)
        Rslider.valueChanged.connect(self.change_level2)        
 
        returnButton = HoverButton(window1,"photo/back.png","photo/back2.png")
        returnButton.clicked.connect(self.back)
       
        Sbottun = HoverButton(window1,"photo/bolt.png","photo/bolt1.png")
        Sbottun.clicked.connect(lambda: self.RockTest(0))
        Sbottun.setIconSize(QSize(40,40))


        Rbottun = HoverButton(window1,"photo/bolt.png","photo/bolt1.png")
        Rbottun.clicked.connect(lambda: self.ScissorTest(0))
        Rbottun.setIconSize(QSize(40,40))

        h1 = QHBoxLayout()
        #h1.addStretch()
        h1.addWidget(Sslider)
        #h1.addStretch()
        h1.addWidget(Rslider)
        #h1.addStretch()

        h2 = QHBoxLayout()
        h2.addWidget(Slabel,0,Qt.AlignCenter)
        h2.addWidget(Rlabel,0,Qt.AlignCenter)
        
        
        h3 = QHBoxLayout()
        h3.addWidget(Sbottun,0,Qt.AlignCenter)
        h3.addWidget(Rbottun,0,Qt.AlignCenter)

        h4 = QHBoxLayout()
        h4.addWidget(returnButton,0,Qt.AlignRight)



        layout.addWidget(pic1)
        layout.addLayout(h1)        
        layout.addLayout(h2)        
        layout.addLayout(h3)
        layout.addLayout(h4)



        window1.setLayout(layout)        
        self.addWidget(window1)
        self.setCurrentWidget(window1)


    def back(self):
        pic.show()
        self.removeWidget(window1)
    def change_level1(self,i):
        self.idensity1 = i
        number=str(i)
        text="Idensity:"+number
        Slabel.setText(text)
    def change_level2(self,i):
        self.idensity2 = i
        number=str(i)
        text="Idensity:"+number
        Rlabel.setText(text)

    def RockTest(self, u):
    	print "ems------------",
        print self.idensity1+u
        my_ems_board.send(ems_command(1,self.idensity1+u,500))
        self.timer = QTimer()
        self.timer.singleShot(100, lambda: self.ScissorTest(u))  
        #my_ems_board.send(ems_command(2,self.idensity1,500))


    def ScissorTest(self, u):
    	print "ems------------",
        print self.idensity2+u
        my_ems_board.send(ems_command(2,self.idensity2+u,500))

    



if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()




