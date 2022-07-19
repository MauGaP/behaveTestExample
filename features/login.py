import time
from page_objects.Login_page import CAMPO_EMAIL, CAMPO_PAS, CONTRASENA, HOME_PAGE, LOGIN_BOTON, SIGNIN_BOTON, USUARIO
from page_objects.BasePage import click_elemrnt_by_css_selector, go_to_website, llenar_campo
## ir a http://automationpractice.com/index.php
go_to_website(HOME_PAGE)
## hacer click en boton Sing In (inspeccionar, buscar selector, copiar selector)
time.sleep(1)
click_elemrnt_by_css_selector(LOGIN_BOTON)
## completar campo Email address    mikmik@gmail.com  
llenar_campo(CAMPO_EMAIL,USUARIO)
## completar campo Password   MIKMIK
llenar_campo(CAMPO_PAS,CONTRASENA)
##Click en loguear
click_elemrnt_by_css_selector(SIGNIN_BOTON)
## validar elemento en lapagina sing out