import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from time import sleep
from pyEMS import openEMSstim
from pyEMS.EMSCommand import ems_command
from pyEMS import openEMSstim
from random import randint 
from host import Host


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
    def playAN(self,nowlife):
        self.life = nowlife
        self.timer = QTimer()
        self.timer.singleShot(self.timedelay,self.start)
        self.timer.singleShot(self.timedelay+1000,self.cc)

    def cc(self):
        if self.life == 2:
            self.movie.setFileName("photo/full_1.gif")
        elif self.life == 1:
            self.movie.setFileName("photo/full_2.gif")
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
        pic = QLabel(self)
        self.timer = QTimer()
        pic.setScaledContents(True)
        pic.setGeometry(0,0,1440,1000)
        pic.setPixmap(QPixmap("photo/title4.jpg")) 
        window = QWidget()

        host.register(self.receive)

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
    def changeGif(self, gifname):
        global movie
        movie.stop()
        movie = QMovie(gifname)
        #print "fuckkkkkk"
        pp.setMovie(movie)
        movie.start()


    #def set_left(self):
        #self.timer.singleShot(1000, lambda: self.changeGif("photo/R2.gif")) 
        #self.changeGif("photo/leftattack.gif")
    #def set_right(self):
        #self.changeGif("photo/rightattack.gif")
    #def set_peace(self):
        #self.changeGif("photo/peace.gif")
    def ReadyStart(self, mode):
        global count
        count=1
        global oppp
        oppp=mode
        print "Mode:"
        print mode
        print self.idensity1
        print self.idensity2

        global roundlabel
        roundlabel = QLabel("")
        roundlabel.setFont(QFont("SWLINK",90,QFont.Bold))
        til = QHBoxLayout()
        til.addWidget(roundlabel, 0, Qt.AlignCenter)
        msgtopi="1 "+str(self.idensity1)+" "+str(self.idensity2)+" "+str(mode)
        host.sendMessages(msgtopi)
        pic.hide()
        global window2
        window2 = QWidget()
        window2.setStyleSheet("background-color:white")
        global leftlife
        leftlife = 3
        global rightlife
        rightlife = 3
        global pp
        pp = QLabel()
        global movie 
        movie = QMovie("photo/R1.gif")
        pp.setMovie(movie)
        movie.start()
        global bloodleft
        global bloodright
        bloodleft = GifImage(window2, "photo/full.gif",1600,2)
        bloodright = GifImage(window2, "photo/full.gif",1600,3)
        #self.timer.singleShot(3000, lambda: self.changeGif("stand.gif"))
        self.timer.singleShot(7500,self.pleasesend)
        ho = QHBoxLayout()
        ho.addWidget(bloodleft, 0, Qt.AlignCenter)
        ho.addWidget(bloodright, 0, Qt.AlignCenter)  
        layout = QVBoxLayout()
        layout.addStretch()
        layout.addLayout(til)
        layout.addStretch()
        layout.addLayout(ho)
        layout.addWidget(pp, 0, Qt.AlignCenter)
        layout.addStretch()
        window2.setLayout(layout)
        self.addWidget(window2)
        self.setCurrentWidget(window2)
    def Roundnumber(self, te):
        roundlabel.setText(te)    
    def pleasesend(self):
        host.sendMessages("2 start")          
    def receive(self,data):
        choice=int(data)
        global count
        global oppp
        if choice == 1:
            self.changeGif("photo/leftattack.gif")
            global rightlife
            bloodright.playAN(rightlife-1)  
            rightlife -=1 
            count+=1  
            print count     
            ss=str(count)
            self.timer.singleShot(3000, lambda: self.changeGif("photo/R"+ss+".gif"))
            if count!=4:
                self.timer.singleShot(10000,self.pleasesend)
        elif choice == 2:
            self.changeGif("photo/rightattack.gif")
            global leftlife
            bloodleft.playAN(leftlife-1) 
            leftlife -=1
            count+=1
            print count
            ss=str(count)
            self.timer.singleShot(3000, lambda: self.changeGif("photo/R"+ss+".gif"))
            if count!=4:
                self.timer.singleShot(10000,self.pleasesend)
        elif choice == 3:
            self.changeGif("photo/peace.gif")
            global rightlife
            bloodright.playAN(rightlife-1)  
            rightlife -=1 
            global leftlife
            bloodleft.playAN(leftlife-1) 
            leftlife -=1
            count+=1
            print count
            ss=str(count)
            self.timer.singleShot(3000, lambda: self.changeGif("photo/R"+ss+".gif"))
            if count!=4:
                self.timer.singleShot(10000,self.pleasesend)
        if count==4:
            self.timer.singleShot(3000, lambda: self.finishPage(oppp))
              
        #self.timer.singleShot(6000, lambda: self.EMS(self.idensity1 , self.idensity2, mode))


        #self.timer.singleShot(10000, lambda: self.changeGif("photo/R2.gif")) 
        #self.timer.singleShot(15000, lambda: self.EMS(self.idensity1 , self.idensity2, mode))

        #self.timer.singleShot(19000, lambda: self.changeGif("photo/R3.gif")) 
        #self.timer.singleShot(24000, lambda: self.EMS(self.idensity1 , self.idensity2, mode))


        #self.timer.singleShot(30000, lambda: self.finishPage(mode))


    def EMS(self, i1, i2, mode):
        #countcount=1
        print mode
        print "ems",
        print i1, i2
        if mode == 1: #easy mode
            rand_number = randint(1, 3)
            if rand_number == 1:
                print "scissor",
                print i1
                my_ems_board.send(ems_command(1,i2,1000))
            elif rand_number ==2:
                print "rock",
                print i2
                my_ems_board.send(ems_command(1,i1,1000))
                my_ems_board.send(ems_command(2,i1,1000))   
        

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
        global count
        count=1
        self.removeWidget(window3)
        self.addWidget(window2)
        self.setCurrentWidget(window2)

        global movie
        movie.stop()
        movie = QMovie("photo/R1.gif")
        pp.setMovie(movie)
        movie.start()

        global leftlife
        global rightlife


        leftlife = 3
        rightlife = 3



        bloodleft.reset()
        bloodright.reset()
        self.timer = QTimer()
        print "restart:", leftlife, rightlife
        self.timer.singleShot(7500, self.pleasesend)  
        print "restart:~~~", leftlife, rightlife    
        """
        self.timer = QTimer()
              
        self.timer.singleShot(6000, lambda: self.EMS(self.idensity1 , self.idensity2, mode))

        self.timer.singleShot(10000, lambda: self.changeGif("photo/R2.gif")) 
        self.timer.singleShot(15000, lambda: self.EMS(self.idensity1 , self.idensity2, mode))

        self.timer.singleShot(19000, lambda: self.changeGif("photo/R3.gif")) 
        self.timer.singleShot(24000, lambda: self.EMS(self.idensity1 , self.idensity2, mode))


        self.timer.singleShot(30000, lambda: self.finishPage(mode))
        
        """
    

    def gotohome(self):
        self.idensity1 = 10
        self.idensity2 = 10
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
        #Sslider.setStyleSheet(" border: 2px solid grey; background: #32CC99;height: 15px;margin: 0px 20px 0 20px;")
        Sslider.setMinimum(10)
        Sslider.setMaximum(100)
        Sslider.setTickPosition(QSlider.TicksBelow)
        Sslider.setTickInterval(10)
        Sslider.valueChanged.connect(self.change_level1)

        global Rslider
        Rslider=QSlider(Qt.Horizontal)
        Rslider.setMinimum(10)
        Rslider.setMaximum(100)
        Rslider.setTickPosition(QSlider.TicksBelow)
        Rslider.setTickInterval(10)
        Rslider.valueChanged.connect(self.change_level2)        
 
        returnButton = HoverButton(window1,"photo/back.png","photo/back2.png")
        returnButton.clicked.connect(self.back)
       
        Sbottun = HoverButton(window1,"photo/bolt.png","photo/bolt1.png")
        Sbottun.clicked.connect(self.RockTest)
        Sbottun.setIconSize(QSize(40,40))


        Rbottun = HoverButton(window1,"photo/bolt.png","photo/bolt1.png")
        Rbottun.clicked.connect(self.ScissorTest)
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

    def RockTest(self):
        print self.idensity1
        msgtopi="3 "+str(self.idensity1)+" "+str(self.idensity2)+" 1"
        self.timer = QTimer()
        self.timer.singleShot(100, lambda: self.ScissorTest())
        host.sendMessages(msgtopi)


    def ScissorTest(self):
        print self.idensity2
        msgtopi="3 "+str(self.idensity1)+" "+str(self.idensity2)+" 2"
        host.sendMessages(msgtopi)

    


 
if __name__ == '__main__':
    
    global host
    host = Host()
    app = QApplication([])
    window = MainWindow()

    host.start()
    window.show()
    app.exec_()




