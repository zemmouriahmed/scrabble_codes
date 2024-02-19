import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
rp.set_url("https://www.motscroises.fr/dictionnaire-scrabble.fr/robots.txt")
rp.read()
# Correction de l'URL en enlevant le double slash avant "section/"
can_scrape = rp.can_fetch("*", "https://www.motscroises.fr/dictionnaire-scrabble.fr/section/")
print(can_scrape)  # Retourne True si le scraping est autorisé, False sinon
