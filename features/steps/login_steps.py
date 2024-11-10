from behave import*
from features.pages.login_page import LoginPage
loginPage = LoginPage

@given(u'que eu esteja na tela de Login')
def step_impl(context):
    loginPage.acessar_site_saucedemo(context)


@when(u'eu digitar o login e senha')
def step_impl(context):
    loginPage.preenche_login(context)


@when(u'clicar em login')
def step_impl(context):
    loginPage.clica_login(context)


@then(u'terei feito o login com sucesso')
def step_impl(context):
    loginPage.fechar_aplicacao(context)