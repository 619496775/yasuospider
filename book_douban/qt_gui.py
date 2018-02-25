import sys
from book_douban import  mysql
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MyGui(QWidget):
    def __init__(self,parent = None):
        QWidget.__init__(self)
        # 数据库操作器
        self.mysql = mysql.MySQL()
        
        # 函数
        self._init_gui()
        self._init_signal_slot()
        #self._display_bookshelf()
        
        # 变量
        # self.searchDoc,搜索栏cursor 用来获得python执行Mysql命令的方法，操作游标
        # self.bookshelfDoc,书架栏cursor
        # self.bookshelfDoc2,推荐栏cursor
        
    def _init_gui(self):
        self.setWindowTitle("YasuoBooks")
        #搜索栏布局
        self.searchLabel = QLabel(u'书名')
        self.searchEdit = QLineEdit()
        self.searchButton = QPushButton(u'搜索')
        self.searchTable = QTableWidget(0,2)
        self.searchTable.setEditTriggers(QAbstractItemView.NoEditTriggers)#禁止编辑
        self.searchTable.setHorizontalHeaderLabels([u'书名',u'评分'])
        self.searchTable.setSelectionBehavior(QAbstractItemView.SelectRows)#整行选中的方式
        self.searchTable.setColumnWidth(0,220)
        self.searchTable.setColumnWidth(1,30)
        
        searchLayout = QGridLayout()
        searchLayout.addWidget(self.searchLabel,0,0)
        searchLayout.addWidget(self.searchEdit,0,1)
        searchLayout.addWidget(self.searchButton,0,2)
        searchLayout.addWidget(self.searchTable,1,0,1,3)
        
        
        

        #主布局
        mainLayout = QGridLayout(self)
        mainLayout.setSpacing(10)
        mainLayout.addLayout(searchLayout, 0, 0)
    
    # 信号    
    def _init_signal_slot(self):
        # PyQt5
        # combo = QtWidgets.QComboBox(self)
        # combo.activated.connect(self.onActivated)
        # PyQt4
        # combo = QtWidgets.QComboBox(self)
        # self.connect(combo, QtCore.pyqtSignal('activated(QString)'), self.onActivated)
        # self.connect(self.searchButton, SIGNAL('clicked()'), self.slot_search_keyword)
        self.searchButton.clicked.connect(self.slot_search_keyword)
    
    # 槽函数
    def slot_search_keyword(self):  
        try:
            keyword = self.searchEdit.text()
            if keyword is None:
                return
            id = self.mysql.search_book_id(keyword)
            id = str(id)
            #self.searchDoc = doc.clone() #保留光标
            
            # 显示查询结果
            self.searchTable.clearContents()
            self.searchTable.setRowCount(0)
        
            
            self.searchTable.insertRow(0)
            self.searchTable.setItem(0,0,QTableWidgetItem(id))  
        except:
            id = ''
            self.searchTable.clearContents()
            '''
            self.searchTable.setRowCount(0)
            self.searchTable.insertRow(0)
            id = self.mysql.search_book_id("XL")
            id = str(id)
            self.searchTable.setItem(0,0,QTableWidgetItem(id))        
            self.searchTable.setItem(0,1,QTableWidgetItem("yasuo"))
            '''
        
app = QApplication(sys.argv)
gui = MyGui()
gui.show()
app.exec_()