import wikipediaapi as wikiapi

wiki = wikiapi.Wikipedia('ru')
page = wiki.page('Галактика')

links = page.links
doc = []
for title in sorted(links.keys()):
    page_1 = wiki.page(title)
    if page_1.exists():
        doc.append((page_1.summary))
with open('doc.json', 'w', encoding='utf-8') as file:
    for item in doc:
        file.write("{}\n".format(item))





