from newspaper import Article
import nltk
from gtts import gTTS
import os

#Get the article
article = Article('https://www.nu.or.id/esai/di-balik-muktamar-nu-yang-teduh-SgPyT')
article.download()
article.parse()
nltk.download('punkt')
article.nlp()
#Get the articles text
mytext = article.text
language = 'id'
myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("read_article.mp3")
os.system("start read_article.mp3")