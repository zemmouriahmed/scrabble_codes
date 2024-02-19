import urllib.robotparser

rp = urllib.robotparser.RobotFileParser()
rp.set_url("https://www.motscroises.fr/dictionnaire-scrabble.fr/robots.txt")
rp.read()
can_scrape = rp.can_fetch("*", "https://www.motscroises.fr/dictionnaire-scrabble.fr//section/")
print(can_scrape)  # Retourne True si le scraping est autorisé, False sinon
