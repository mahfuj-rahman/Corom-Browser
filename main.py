# ----------In the name of ALLAH, The Rohim, The Rahman-----------

# Project name: Corom Browser
# by Team PENTAGON
# --------Member's Information--------

# Md. Mahfujur Rahman | ID: 192-15-13207
# Samiul Arafah Dhrubo | ID: 192-15-13051
# Lamia Binta Progga | ID: 192-15-13222
# Saima Binta Younus | ID: 192-15-13137
# Abdullah Al Ryan | ID: 192-15-13088

# --------Project starts from here--------


# To create an Environment to run the browser

# contributed by Mahfuj
import sys

# Responsible for main window
from PyQt5.QtWidgets import *

# Responsible for WebEngine
from PyQt5.QtWebEngineWidgets import *

# To Set and Access a URL
from PyQt5.QtCore import *


# Basic Code to for the corom browser
# contributed by Mahfuj
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://duckduckgo.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navigator
        navigator = QToolBar()
        self.addToolBar(navigator)

        # contributed by Samiul
        # back to previous browsing page
        back_btn = QAction('←‌', self)
        back_btn.triggered.connect(self.browser.back)
        navigator.addAction(back_btn)

        # contributed by Samiul
        # move to next browsing page
        forward_btn = QAction(' →', self)
        forward_btn.triggered.connect(self.browser.forward)
        navigator.addAction(forward_btn)

        # contributed by Samiul
        # reload tab
        reload_btn = QAction('∞', self)
        reload_btn.triggered.connect(self.browser.reload)
        navigator.addAction(reload_btn)

        # contributed by Progga
        # home_btn to escape to initial state
        home_btn = QAction('🏛️', self)
        home_btn.triggered.connect(self.navigate_home)
        navigator.addAction(home_btn)

        # contributed by Progga
        # Stop button
        stop_btn = QAction("❌", self)
        stop_btn.triggered.connect(self.browser.stop)
        navigator.addAction(stop_btn)

        # contributed by Progga
        # Open DIU student portal
        stu_portal = QAction("DIU Student Portal👨‍🎓", self)
        stu_portal.triggered.connect(self.diu_stu_portal)
        navigator.addAction(stu_portal)

        # contributed by Progga
        # Open BLC
        blc_diu = QAction("DIU BLC🎓", self)
        blc_diu.triggered.connect(self.load_blc)
        navigator.addAction(blc_diu)

        # contributed by Progga
        # Open DIU Website
        web_diu = QAction("DIU Website💡", self)
        web_diu.triggered.connect(self.diu_website)
        navigator.addAction(web_diu)

        # contributed by Progga
        # Corona Update
        corona = QAction("Corona Update💉", self)
        corona.triggered.connect(self.corona_web)
        navigator.addAction(corona)

        # contributed by Mahfuj
        # BlockChain
        b_chain = QAction("BlockChain Update🔗", self)
        b_chain.triggered.connect(self.block_chain)
        navigator.addAction(b_chain)

        # contributed by Mahfuj
        # Cryptocurrency
        c_currency = QAction("Cryptocurrency live💲", self)
        c_currency.triggered.connect(self.crypto)
        navigator.addAction(c_currency)

        # contributed by Mahfuj
        # Pipilica Search Engine
        pipilica = QAction("Pipilica🔍", self)
        pipilica.triggered.connect(self.pipilica_search_engine)
        navigator.addAction(pipilica)

        # contributed by Mahfuj
        # Mail
        mail = QAction("Mail Box📬", self)
        mail.triggered.connect(self.mail_box)
        navigator.addAction(mail)

        # contributed by Mahfuj
        # Alvi Ma'am github
        git_hub_syada_madam = QAction("Git Hub", self)
        git_hub_syada_madam.triggered.connect(self.syada_madam)
        navigator.addAction(git_hub_syada_madam)

        # contributed by Mahfuj
        # Youtube
        you = QAction("Youtube", self)
        you.triggered.connect(self.you_tube)
        navigator.addAction(you)

        # contributed by Mahfuj
        # Facebook
        f_book = QAction("Facebook", self)
        f_book.triggered.connect(self.facebook)
        navigator.addAction(f_book)

        # contributed by Mahfuj
        # Linkedin
        link = QAction("LinkedIn", self)
        link.triggered.connect(self.linkedin)
        navigator.addAction(link)

        # contributed by Progga
        # start game
        start_game = QAction('Game', self)
        start_game.triggered.connect(self.play_game)
        navigator.addAction(start_game)

        # URL Bar //contributed by Saima
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navigator.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    # contributed by Progga
    # Calling from the home_btn
    def navigate_home(self):
        self.browser.setUrl(QUrl('https://google.com'))

    # contributed by Progga
    def load_blc(self):
        self.browser.setUrl(QUrl('https://elearn.daffodilvarsity.edu.bd/'))

    # contributed by Progga
    def diu_website(self):
        self.browser.setUrl(QUrl('https://daffodilvarsity.edu.bd/'))

    # contributed by Progga
    def corona_web(self):
        self.browser.setUrl(QUrl('https://corona.gov.bd/'))

    # contributed by Progga
    def diu_stu_portal(self):
        self.browser.setUrl(QUrl('http://gateway.diu.edu.bd:8888/'))

    # contributed by Mahfuj
    def block_chain(self):
        self.browser.setUrl(QUrl('https://www.blockchain.com/'))

    # contributed by Mahfuj
    def crypto(self):
        self.browser.setUrl(QUrl('https://www.cryptocompare.com/'))

    # contributed by Mahfuj
    def pipilica_search_engine(self):
        self.browser.setUrl(QUrl('https://www.pipilika.com/'))

    # contributed by Mahfuj
    def mail_box(self):
        self.browser.setUrl(QUrl('https://mail.google.com/'))

    # contributed by Mahfuj
    def syada_madam(self):
        self.browser.setUrl(QUrl('https://github.com/onikajnu'))

    # contributed by Mahfuj
    def you_tube(self):
        self.browser.setUrl(QUrl('https://www.youtube.com/'))

    # contributed by Mahfuj
    def facebook(self):
        self.browser.setUrl(QUrl('https://www.facebook.com/'))

    # contributed by Mahfuj
    def linkedin(self):
        self.browser.setUrl(QUrl('https://www.linkedin.com/'))

    # contributed by Progga
    def play_game(self):
        self.browser.setUrl(QUrl('https://play.famobi.com/smarty-bubbles'))

    # calling from the url bar //contributed by Saima
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    # calling from update url //contributed by Saima
    def update_url(self, q):
        self.url_bar.setText(q.toString())


# Executing app //contributed by Ryan
app = QApplication(sys.argv)
QApplication.setApplicationName('Corom Browser')
window = MainWindow()
app.exec()
