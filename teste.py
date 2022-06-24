# ARQUIV PARA TESTES DE LOGICA
import os


env_secret_key = os.getenv('DWD_SECRET_KEY')
if env_secret_key:
    print("Nice and Ezy :)")
    print(env_secret_key)
