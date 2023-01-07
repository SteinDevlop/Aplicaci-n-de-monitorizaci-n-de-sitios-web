import requests
import time
from bs4 import BeautifulSoup
import hashlib
import os
class Command:
    site = "https://www.google.com/"
    analisis = 0
    cambios = 0
    requestPerSecond = 1
    @classmethod
    def check_website(cls):
        cls.analisis += 1
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

        # Envía una solicitud HTTP GET al sitio web que quieres monitorizar, incluyendo la cabecera User-Agent
        response = requests.get(cls.site, headers=headers)

        # Parsea el contenido de la respuesta utilizando Beautiful Soup
        soup = BeautifulSoup(response.content, 'html.parser')
        for element in soup.find_all():
            if 'timestamp' in element.attrs or 'unique_id' in element.attrs:
                element.decompose()
        # Genera un hash del contenido del sitio web
        website_hash = hashlib.sha1(str(soup).encode('utf-8')).hexdigest()

        # Abre el archivo que almacena el último hash conocido

        if os.path.isfile("last_hash.txt"):
            pass
        else:
            with open("last_hash.txt","w"):
                pass


        with open('last_hash.txt', 'r') as f:
            last_known_hash = f.read()

        # Compara el último hash conocido con el nuevo hash del sitio web
        if website_hash != last_known_hash:
            # Si son diferentes, significa que el sitio web ha cambiado
            Command.send_notification()

        # Guarda el nuevo hash en el archivo
        with open('last_hash.txt', 'w') as f:
            f.write(website_hash)
    @classmethod
    def send_notification(cls):
        cls.cambios += 1

if __name__ == "__main__":
    print("Proceso de monitoria iniciado")
    print(f"""
        ----------Update Inicial ----
        Pagina web: {Command.site}
        Cambios en la pagina detectado: {Command.cambios}
        -------------------------------
        """)
    print(f"""
        ----------Informacion relevante ----
        Si hay muchos cambios, es extremamente probable que
        la pagina cambie su codigo con cada recarga,
        aconsejamos dejar de usar la herramienta en url como ellas.
        -------------------------------
        """)
    while True:
    # Ejecutar la función
        print(f"\033[F\033[KCambios en la pagina: {Command.cambios}")
        Command.check_website()
        time.sleep(Command.requestPerSecond)

