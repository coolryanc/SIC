import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from time import sleep
from pyEMS import openEMSstim
from pyEMS.EMSCommand import ems_command
from pyEMS import openEMSstim
from random import randint 



my_ems_board = openEMSstim.openEMSstim("/dev/tty.usbserial-A9WRN9D1",19200)
"""
class GifImage(QLabel):
    def __init__(self, *args):
        super(GifImage, self).__init__()
        print args[1]
        global movie 
        self.movie = QMovie(args[1])
        self.setMovie(self.movie)
        self.movie.start()
        #self.movie.stop()
        #self.setVisible(False)
        self.timer = QTimer()
        self.timer.singleShot(int(args[2]),self.clockdown)

    
    def clockdown(self):
        self.movie.stop()
        self.movie = QMovie("photo/leftattack.gif")
        self.setMovie(self.movie)
        self.movie.start()
 """       

class HoverButton(QPushButton):

    def __init__(self,  *args):
        super(HoverButton, self).__init__()
        self.setMouseTracking(True)
        self.setFlat(True)
        self.ph1 = args[1]
        self.ph2 = args[2]
        self.setIcon(QIcon(args[1]))
    
    def enterEvent(self,event):
        print("Enter")
        self.setIcon(QIcon(self.ph2))
    def leaveEvent(self,event):
        print("Leave")
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
        print("Enter")
        self.setStyleSheet(self.ph2)
    def leaveEvent(self,event):
        print("Leave")
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

  
        global pp
        #pp = GifImage(window2, "photo/stand.gif", 6000 ,"HI")
        pp = QLabel()
        global movie 
        movie = QMovie("photo/321.gif")
        pp.setMovie(movie)
        movie.start()


        layout = QVBoxLayout()
        layout.addWidget(pp)
        window2.setLayout(layout)
        
        self.addWidget(window2)
        self.setCurrentWidget(window2)

        self.timer = QTimer()
        self.timer.singleShot(3000, lambda: self.changeGif("photo/stand.gif"))      
        self.timer.singleShot(6000, lambda: self.EMS(self.idensity1 , self.idensity2, mode))

        self.timer.singleShot(9000, lambda: self.changeGif("photo/321.gif")) 
        self.timer.singleShot(12000, lambda: self.changeGif("photo/stand.gif")) 
        self.timer.singleShot(15000, lambda: self.EMS(self.idensity1 , self.idensity2, mode))

        self.timer.singleShot(18000, lambda: self.changeGif("photo/321.gif")) 
        self.timer.singleShot(21000, lambda: self.changeGif("photo/stand.gif")) 
        self.timer.singleShot(24000, lambda: self.EMS(self.idensity1 , self.idensity2, mode))


        self.timer.singleShot(30000, lambda: self.finishPage(mode))


    def EMS(self, i1, i2, mode):
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
            else:
                pass 
            # player hand?
                #if player win:
                    #self.changeGif()
                #elif player lose:
                    #self.changeGif()
                #else:
                    #self.changeGif()
                       
        elif mode == 2: #pi camera
            pass
            # player hand?
                #if player win:
                    #self.changeGif()
                #elif player lose:
                    #self.changeGif()
                #else:
                    #self.changeGif()
        
        and_number = randint(1, 3)
        if and_number == 1:
            self.changeGif("photo/leftattack.gif")
        elif and_number == 2:
            self.changeGif("photo/rightattack.gif")
        else:
            self.changeGif("photo/peace.gif")

        
    def changeGif(self, gifname):
        global movie
        movie.stop()
        movie = QMovie(gifname)
        pp.setMovie(movie)
        movie.start()
        
        


    def finishPage(self, mode):
        self.removeWidget(window2)
        global window3
        window3 = QWidget()
        layout = QVBoxLayout()
        finish = QPushButton("Finish")
        finish.clicked.connect(self.gotohome)
        tryagain = QPushButton("tryagain")
        tryagain.clicked.connect(lambda: self.restart(mode))

        layout.addWidget(tryagain)
        layout.addWidget(finish)
        window3.setLayout(layout)
        self.addWidget(window3)
        self.setCurrentWidget(window3)

    def restart(self, mode):
        self.removeWidget(window3)
        self.addWidget(window2)
        self.setCurrentWidget(window2)

        global movie
        movie.stop()
        movie = QMovie("photo/321.gif")
        pp.setMovie(movie)
        movie.start()

        self.timer = QTimer()
        self.timer.singleShot(3000, lambda: self.changeGif("photo/stand.gif"))      
        self.timer.singleShot(6000, lambda: self.EMS(self.idensity1 , self.idensity2, mode))

        self.timer.singleShot(9000, lambda: self.changeGif("photo/321.gif")) 
        self.timer.singleShot(12000, lambda: self.changeGif("photo/stand.gif")) 
        self.timer.singleShot(15000, lambda: self.EMS(self.idensity1 , self.idensity2, mode))

        self.timer.singleShot(18000, lambda: self.changeGif("photo/321.gif")) 
        self.timer.singleShot(21000, lambda: self.changeGif("photo/stand.gif")) 
        self.timer.singleShot(24000, lambda: self.EMS(self.idensity1 , self.idensity2, mode))

        self.timer.singleShot(30000, lambda: self.finishPage(mode))

        
        

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
        my_ems_board.send(ems_command(1,self.idensity1,1000))
        my_ems_board.send(ems_command(2,self.idensity1,1000))

    def ScissorTest(self):
        print self.idensity2
        my_ems_board.send(ems_command(1,self.idensity2,1000))

    


 
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()




