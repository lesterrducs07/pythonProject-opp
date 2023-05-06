response = r.get(https://en.wikipedia.org/wiki/HTML)

wiki_text = response.text
soup = BeautifulSoup(wiki_text 'html.parser')

print(soup)