# ELIMINANDO SPAMS DO EMAIL:
from selenium.webdriver.common.by import By
from modules.starting_driver import *
from modules.actions import *
from genericpath import getsize


user_data = 'assets\\user_data.txt'
# 1 VERIFICAR SE O ARQUIVO "user_data.txt" ESTÁ VAZIO. SE SIM, OBTER CREDENCIAIS DE ACESSO DO USUÁRIO 
if getsize(user_data) == 0:
    #  SE SIM, OBTER CREDENCIAIS DE ACESSO DO USUÁRIO E SALVÁ-LAS NO "user_data.txt"
    get_user_information(user_data)

# 2 PERGUNTE SE O USUÁRIO QUER TROCAR DE CONTA.
new_user = input('Would you like to sign in with another account? Yes [y] - No [n]: ').lower().strip()
if new_user in ('yes', 'y'):
    # SE SIM, OBTER AS NOVAS CREDENCIAIS DE ACESSO E SALVÁ-LAS NO "user_data.txt"
    get_user_information(user_data)

# 3 LER OS DADOS DE ACESSO DO USUÁRIO
email, password = read_data(user_data)
# 4: ABRIR O NAVEGADOR
driver = start_driver()
wait_a_little()
try:
    # 5: ACESSAR O SITE 'https://poczta.wp.pl/login/login.html'
    driver.get('https://poczta.wp.pl/login/login.html')
    wait_a_little()
    # 6: CASO O BOTÃO DE NOTIFICAÇÕES APAREÇA, CLICAR NELE. DO CONTRÁRIO, IGNORE-O.
    try:
        notifications = driver.find_element(By.XPATH, '//button[text()="AKCEPTUJĘ I PRZECHODZĘ DO SERWISU"]')
        wait_a_little()
        # ACEITAR NOTIFICAÇÃO
        notifications.click()
        wait_a_little()
    except:
        pass
    finally:
        # 7: LOCALIZAR CAMPO DE EMAIL
        email_bar = driver.find_element(By.ID,'login')
        wait_a_little()
        # 8: CLICAR NO CAMPO EMAIL
        email_bar.click()
        wait_a_little()
        # 9: DIGITAR EMAIL NO CAMPO DE EMAIL
        type_naturally(email, email_bar)
        wait_a_little()
        # 10: LOCALIZAR O CAMPO DE SENHA
        password_bar = driver.find_element(By.ID,'password')
        wait_a_little()
        # 11: CLICAR NO CAMPO SENHA
        password_bar.click()
        wait_a_little()
        # 12: DIGITAR SENHA
        type_naturally(password, password_bar)
        wait_a_little()
        # 13: LOCALIZAR CAMPO DE LOGIN
        button_logIn = driver.find_element(By.XPATH,"//button[@type='submit']")
        wait_a_little()
        # 14: CLICAR NO BOTÃO DE LOGIN
        button_logIn.click()
        wait_a_lot()
        # 15: DESCER A TELA 150px
        go_down_screen(driver, 150)
        # 16: LOCALIZAR BOTÃO DE SPAM
        spam = driver.find_elements(By.XPATH, '//div[@class="sidebar__label"]')[3]
        wait_a_little()
        # 17: CLICAR NO BOTÃO DE SPAM
        spam.click()
        wait_a_little()
        # 18: DESCER A TELA 500px
        go_down_screen(driver, 500)
        wait_a_little()
        try:
            # 19: ACHAR ÍCONE DE SELEÇÃO DE TODOS OS SPAMS
            selector = driver.find_elements(By.XPATH, '//div[@class="Checkbox"]')[0]
            wait_a_little()
            # 20: CLICAR NO ÍCONE DE SELEÇÃO DE TODOS OS SPAMS
            selector.click()
            wait_a_little()
            # 21: ENCONTRAR O BOTÃO EXCLUIR
            exclude_button = driver.find_elements(By.XPATH, '//button[@class="Button Button--secondary"]')[0]
            wait_a_little()
            # 22: CLICAR NO BOTÃO EXCLUIR
            exclude_button.click()
            wait_a_little()
            # 23: LOCALIZAR BOTÃO DE CONFIRMAÇÃO DE EXCLUSÃO
            confirmation = driver.find_element(By.XPATH, '//button[@class="Button Button--cta"]')
            wait_a_little()
            # 24: CLICAR NA CONFIRMAÇÃO DE EXCLUSÃO
            confirmation.click()
            wait_a_little()
            # 25: FECHAR JANELA DO NAVEGADOR
            driver.close()
            # 26: IMPRIMIR MENSAGEM: "Os spams foram deletados com sucesso."
            print("\nSpams has been deleted successfully.\n")
        # ?: CASO HAJA UM ERRO NESSE PROCESSO, SIGNIFICA QUE NAO HÁ SPAMS"
        except:
            # ??: NESTE CASO, IMPRIMIR MENSAGEM: "Não há spams agora. Por favor, tente mais tarde."
            print("\nThere are no spams now. Please, try it again later.\n")
# !: SE POR ACASO, OS BUTÕES NÃO FOREM LOCALIZADOS, O SITE DEVE TER SIDO ATUALIZADO.
except:
        # !: NESTE CASO, INFORMAR O USUÁRIO PARA QUE ELE NOTIFIQUE O DESENVOLVEDOR.
        print('We could not delete the spams on your account. The website is likely', end=" ")
        print(' to have been updated. Please, reach out to the developer for new updates too.\n')
        # 31: FECHAR JANELA DO NAVEGADOR
        driver.close()
