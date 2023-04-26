import requests
from bs4 import BeautifulSoup
import time

while True:
    # URL der Webseite
    url = "https://www.onlinetitans.org/store/p4/Live-Podcast_%22Nicht_mehr_ganz_Twitter%22_mit_iBlali_%26_Zeo_in_M%C3%BCnchen.html#/"

    # Hole den HTML-Code der Webseite
    html = requests.get(url).text

    # Wandle den HTML-Code in ein BeautifulSoup-Objekt um
    soup = BeautifulSoup(html, "html.parser")

    # Finde das Input-Tag mit der ID "wsite-com-product-quantity-input"
    input_tag = soup.find("input", {"id": "wsite-com-product-quantity-input"})

    # Hole den Wert des "max"-Attributs
    max_value = input_tag.get("max")
    max_value = max_value + " Tickets"

    # Erstelle die Datei "data.txt" im Verzeichnis "/var/www/html/livepodcast/" und schreibe den Wert von "max_value" hinein
    with open("/var/www/html/livepodcast/data.txt", "w") as f:
        f.write(max_value)

    print(max_value)

    # Warte 120 Sekunden, bevor die Schleife erneut ausgeführt wird
    time.sleep(120)
