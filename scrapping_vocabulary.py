VOCAB_PATH = 'vocab_info.txt'
import os
import tqdm
def collecter_vocab():

    import requests
    from bs4 import BeautifulSoup
    import re
    # %%
    vocabulaire = []
    url = 'https://fr.wiktionary.org/wiki/Cat%C3%A9gorie:fran%C3%A7ais'
    npages = 0
    with tqdm.tqdm() as pbar:
        while True:
            pbar.set_description('Sending request')
            r = requests.get(url)
            # if r.status_code == 200:
            #     print('OK')
            pbar.set_description('Parsing request')
            soup = BeautifulSoup(r.content, 'lxml') #Parsing
            vocabulaire += [w.text for w in soup.select('.mw-category-group>ul>li')]
            # print(soup.prettify()) #Rend le code plus lisible
            npages += 1
            next_page_a = soup.find('a', string='page suivante')
            if next_page_a is None:
                break
            url = 'https://fr.wiktionary.org' + next_page_a.get('href')
            pbar.update(1)
    print (f'{npages} ont été collectées')
    # %%
    len(vocabulaire)

    with open(VOCAB_PATH, 'w') as f :

    # %%

        for w in vocabulaire:
            if re.search('^[A-Za-z]+$', w) is not None:
            # print(w)

                f.write(w)
        # %%



if not os.path.isfile(VOCAB_PATH):
    collecter_vocab()