import sys
import os
from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):
	def __init__(self):
		super(Window, self).__init__()
		self.initUI()

	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def exit_enter(self, event):
		self.exit.setPixmap(QtGui.QPixmap('img/exit_down.png'))
	def exit_leave(self, event):
		self.exit.setPixmap(QtGui.QPixmap('img/exit_up.png'))

	def minimize_enter(self, event):
		self.minimize.setPixmap(QtGui.QPixmap('img/minimize_down.png'))
	def minimize_leave(self, event):
		self.minimize.setPixmap(QtGui.QPixmap('img/minimize_up.png'))

	def pushBulletHover_enter(self, event):
		self.pushBulletHover.setPixmap(QtGui.QPixmap('img/pushBulletHover.png'))
	def pushBulletHover_leave(self, event):
		self.pushBulletHover.setPixmap(QtGui.QPixmap('img/pushBulletHoverOff.png'))

	def exitButton(self, event):
		exit(0)

	def minimizeButton(self, event):
		self.showNormal()
		self.showMinimized()

	def initUI(self):
		self.resize(800, 500)
		self.center()
		self.setFixedSize(800, 500)

		self.background = QtGui.QLabel(self)
		self.background.setPixmap(QtGui.QPixmap('interface.png'))
		self.background.setGeometry(0, 0, 800, 500)

		self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
		
		self.setWindowTitle("ADB For Windows (dev)")

		self.exit = QtGui.QLabel(self)
		self.exit.setPixmap(QtGui.QPixmap('img/exit_up.png'))
		self.exit.setGeometry(766, 1, 33, 29)
		self.exit.enterEvent = self.exit_enter
		self.exit.leaveEvent = self.exit_leave
		self.exit.mouseReleaseEvent = self.exitButton

		self.minimize = QtGui.QLabel(self)
		self.minimize.setPixmap(QtGui.QPixmap('img/minimize_up.png'))
		self.minimize.setGeometry(700, 1, 32, 29)
		self.minimize.enterEvent = self.minimize_enter
		self.minimize.leaveEvent = self.minimize_leave
		self.minimize.mouseReleaseEvent = self.minimizeButton

		self.loggedIn = QtGui.QLabel(self)
		self.loggedIn.setPixmap(QtGui.QPixmap('img/logIn.png'))
		self.loggedIn.setGeometry(575, 23, 44, 8)
		#self.loggedIn.enterEvent = self.minimize_enter
		#self.loggedIn.leaveEvent = self.minimize_leave
		#self.loggedIn.mouseReleaseEvent = self.minimizeButton

		self.pushBulletHover = QtGui.QLabel(self)
		self.pushBulletHover.setPixmap(QtGui.QPixmap('img/pushBulletHoverOff.png'))
		self.pushBulletHover.setGeometry(561, 1, 107, 36)
		self.pushBulletHover.enterEvent = self.pushBulletHover_enter
		self.pushBulletHover.leaveEvent = self.pushBulletHover_leave
		self.pushBulletHover.mouseReleaseEvent = self.pushBulletHover

		self.show()

	def mouseMoveEvent(self, event):
		super(Window, self).mouseMoveEvent(event)
		if self.leftClick == True: self.moveWindow(event.globalPos())

	def mousePressEvent(self, event):
		super(Window, self).mousePressEvent(event)
		if event.button() == QtCore.Qt.LeftButton:
			self.leftClick = True

	def mouseReleaseEvent(self, event):
		super(Window, self).mouseReleaseEvent(event)
		self.leftClick = False

def main():
	app = QtGui.QApplication(sys.argv)
	w = Window()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	main()
