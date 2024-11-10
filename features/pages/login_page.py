import time
from features.support.ambiente import*
from features.support.elementos import*
from features.support.page_utils import PageUtils
page_utils = PageUtils()

class LoginPage:
    def acessar_site_saucedemo(context):
        page_utils.abrir_um_browser(URL_SAUCEDEMO)

    def clica_login(context):
        page_utils.clica_elemento_login(CLICK_LOGIN)

    def preenche_login(context):
        page_utils.inserir_login()
        page_utils.inserir_senha()
    
    def fechar_aplicacao(context):
        page_utils.fechar_browser()
