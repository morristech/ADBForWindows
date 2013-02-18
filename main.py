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

	def initUI(self):
		self.resize(300, 500)
		self.center()
		self.setFixedSize(800, 500)
		
		self.setWindowTitle("ADB For Windows (dev)")
		
		self.show()

def main():
	app = QtGui.QApplication(sys.argv)
	w = Window()
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	main()
