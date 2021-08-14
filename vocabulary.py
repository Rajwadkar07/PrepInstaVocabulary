import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
url = "https://prepinsta.com/most-important-words-for-synonyms-and-antonyms/"
res = requests.get(url)
soup = bs(res.text, "html.parser")
soup = soup.findAll("h4", {"class":"elementor-heading-title"})
words = []
for i in soup:
    if i.text == " " or i.text == "\n" or i.text == "Vocabulary":
        pass
    else:
        words.append(i.text.strip().split(":"))
df = pd.DataFrame(words, columns = ['Words','Meanings', 'None'], index = range(1,len(words)+1))
del(df['None'])
df.to_csv("Vocabulary.csv", index_label = "Sr. No.")
print(df)
