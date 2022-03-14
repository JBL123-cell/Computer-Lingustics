import wikipediaapi as wikiapi
import json
wiki = wikiapi.Wikipedia('ru')
page = wiki.page('Галактика')

links = page.links
data = {}
js = []
for title in sorted(links.keys()):
    if any(ch.isdigit() for ch in title):
        continue
    else:
        page_1 = wiki.page(title)
        if page_1.exists():
            js.append(page_1.summary)

for i in range(len(js)):
    data[i] = {'text': js[i]}
with open('galax.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)







