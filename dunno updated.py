from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore

import sys


# create a Window class
class Window(QMainWindow):
    # constructor
    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Tic Square Kelompok 2 IS-03-03")

        # setting geometry
        self.setGeometry(100, 100,
                         550, 650)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(300, 300, 201, 325))
        self.frame.setStyleSheet("background-color:rgb(170, 170, 127)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(10, 110, 181, 201))
        self.textEdit.setStyleSheet("background-color:rgb(170, 170, 127)")
        self.textEdit.insertPlainText("1. Klik New Game. \n2. Pemain Pertama bermain terlebih dahulu, dengan input (X atau O). \n3. Selanjutnya, giliran pemain kedua bermain, dengan input (X atau O). \n4. Ketika salah satu pemain memenangkan game, maka akan keluar score dari pemain tersebut. \n5. Klik Reset untuk babak ke-dua setelah salah satu pemain memenangkan babak pertamanya. \n6. Ketika ingin memulai permainan baru, dan menyudahi permainan sebelumnya, maka kedua pemain bisa    meng-klik tombol New Game.")
        self.textEdit.setReadOnly(True)

        self.label6 = QLabel(self.frame)
        self.label6.setGeometry(40, 30, 150, 60)
        self.label6.setText("Cara Bermain \n  Tic Square")
        self.label6.setFont(QFont('Times', 12))

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for components
    def UiComponents(self):

        self.my_x = 0
        self.my_y = 0
        # turn
        self.turn = 0

        # times
        self.times = 0

        # creating a push button list
        self.push_list = []

        # creating 2d list
        for _ in range(3):
            temp = []
            for _ in range(3):
                temp.append((QPushButton(self)))
            # adding 3 push button in single row
            self.push_list.append(temp)

        # x and y co-ordinate
        x = 90
        y = 90

        # traversing through push button list
        for i in range(3):
            for j in range(3):
                # setting geometry to the button
                self.push_list[i][j].setGeometry(x * i + 20,
                                                 y * j + 120,
                                                 80, 80)

                # setting font to the button
                self.push_list[i][j].setFont(QFont(QFont('Times', 17)))

                # adding action
                self.push_list[i][j].clicked.connect(self.action_called)

        # creating label to tel the score
        self.label = QLabel(self)

        # setting geometry to the label
        self.label.setGeometry(20, 400, 260, 60)

        # setting style sheet to the label
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 3px solid black;"
                                 "background : white;"
                                 "}")

        # setting label alignment


        # setting font to the label
        self.label.setFont(QFont('Times', 15))

        self.label1 = QLabel(self)
        self.label1.setGeometry(400, 120, 60, 60)
        self.label1.setStyleSheet("QLabel"
                                 "{"
                                 "border : 3px solid black;"
                                 "background : white;"
                                 "}")
        self.label1.setFont(QFont('Times', 15))

        self.label2 = QLabel(self)
        self.label2.setGeometry(400, 200, 60, 60)
        self.label2.setStyleSheet("QLabel"
                                  "{"
                                  "border : 3px solid black;"
                                  "background : white;"
                                  "}")
        self.label2.setFont(QFont('Times', 15))

        self.label3 = QLabel(self)
        self.label3.setGeometry(300, 120, 100, 60)
        self.label3.setText("Skor O :")
        self.label3.setFont(QFont('Times', 12))

        self.label4 = QLabel(self)
        self.label4.setGeometry(300, 200, 100, 60)
        self.label4.setText("Skor X :")
        self.label4.setFont(QFont('Times', 12))

        self.label5 = QLabel(self)
        self.label5.setGeometry(150, 20, 450, 70)
        self.label5.setText(" TIC SQUARE GAME \nKelompok 2 IS-03-03")
        self.label5.setFont(QFont('Times', 15))

        # creating push button to restart the score
        reset_game = QPushButton("Reset", self)
        new_game = QPushButton("New Game", self)
        # setting geometry
        reset_game.setGeometry(50, 480, 200, 50)
        new_game.setGeometry(50, 540, 200, 50)

        # adding action action to the reset push button
        reset_game.clicked.connect(self.reset_game_action)
        new_game.clicked.connect(self.new_game_action)

    # method called by reset button
    def new_game_action(self):

        # resetting values
        self.turn = 0
        self.times = 0
        self.my_x = 0
        self.my_y = 0
        # making label text empty:
        self.label.setText("")
        self.label1.setText(str(self.my_x))
        self.label2.setText(str(self.my_y))
        # traversing push list
        for buttons in self.push_list:
            for button in buttons:
                # making all the button enabled
                button.setEnabled(True)
                # removing text of all the buttons
                button.setText("")

    def reset_game_action(self):

        # resetting values
        self.turn = 0
        self.times = 0

        # making label text empty:
        self.label.setText("")

        # traversing push list
        for buttons in self.push_list:
            for button in buttons:
                # making all the button enabled
                button.setEnabled(True)
                # removing text of all the buttons
                button.setText("")

    # action called by the push buttons
    def action_called(self):

        self.times += 1

        # getting button which called the action
        button = self.sender()

        # making button disabled
        button.setEnabled(False)

        # checking the turn
        if self.turn == 0:
            button.setText("X")
            self.turn = 1
        else:
            button.setText("O")
            self.turn = 0

        # call the winner checker method
        win = self.who_wins()

        # text
        text = ""

        # if winner is decided
        if win == True:
            # if current chance is 0
            if self.turn == 0:
                # O has won
                text = "O Won"
                self.my_x += 1
            # X has won
            else:
                text = "X Won"
                self.my_y += 1

            # disabling all the buttons
            for buttons in self.push_list:
                for push in buttons:
                    push.setEnabled(False)

        # if winner is not decided
        # and total times is 9
        elif self.times == 9:
            text = "Match is Draw"

        # setting text to the label
        self.label.setText(text)
        self.label1.setText(str(self.my_x))
        self.label2.setText(str(self.my_y))
    # method to check who wins
    def who_wins(self):

        # checking if any row crossed
        for i in range(3):
            if self.push_list[0][i].text() == self.push_list[1][i].text() \
                    and self.push_list[0][i].text() == self.push_list[2][i].text() \
                    and self.push_list[0][i].text() != "":
                return True

        # checking if any column crossed
        for i in range(3):
            if self.push_list[i][0].text() == self.push_list[i][1].text() \
                    and self.push_list[i][0].text() == self.push_list[i][2].text() \
                    and self.push_list[i][0].text() != "":
                return True

        # checking if diagonal crossed
        if self.push_list[0][0].text() == self.push_list[1][1].text() \
                and self.push_list[0][0].text() == self.push_list[2][2].text() \
                and self.push_list[0][0].text() != "":
            return True

        # if other diagonal is crossed
        if self.push_list[0][2].text() == self.push_list[1][1].text() \
                and self.push_list[1][1].text() == self.push_list[2][0].text() \
                and self.push_list[0][2].text() != "":
            return True

        # if nothing is crossed
        return False


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())
