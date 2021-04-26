#code écrit par Timeo Bossuet
# tuto sur https://timeo.ml

#on commence par importer sleep et selenium
from time import sleep
from selenium import webdriver

#chemin d'accès au driver de chrome
browser = webdriver.Chrome(r'C:\Users\timeo\Desktop\instabot\chromedriver.exe')
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

#on accepte les cookies
cookieform = browser.find_element_by_xpath("//button[text()='Accepter tout']")
cookieform.click()

sleep(2)

#on cherche la case pour le mot de passe et l'identifiant
username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

#une fois cette case trouvée on entre nos donées
username_input.send_keys("mettre-ici-votre-nom-dutilisateur")
password_input.send_keys("mettre-ici-votre-mot-de-passe")

#on se connecte en cliquant sur le bouton 'submit'
login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()


#en toute fin on attends 10 seconde et on ferme le navigateur.
sleep(10)
browser.close()