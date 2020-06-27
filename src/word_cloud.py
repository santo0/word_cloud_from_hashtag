import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords


text = "This would obviously depend on the time period and the military force. I am assuming you are talking about times before modern warfare as modern warfare treats rank and positions quite differently then before. Field promotions are usually conducted by any superior officer as positions needs to be filled. But they are usually just temporary promotions for the campaign until a better replacement can be found. So it does not come with any additional pay or rights. Military units usually keeps a log over everything that happens including field promotions. The officer would often send letters to his superiors recommending people for permanent promotions. If this is granted the promotion becomes permanent and would come with a pay raise. An officer might have a quota for how many people of different rank he would be allowed to promote. It might also have been up to the military education facilities to decide who would be promoted but the recommendations would help a lot, especially if exams did not go well."

stop_words = set(stopwords.words('english'))
words = word_tokenize(text)
words_filtered = []
for w in words:
    if w.lower() not in stop_words:
        words_filtered.append(w)

#for w, v in zip(text.split(' '), words_filtered):
#   print(w,v)

#print(STOPWORDS)
wordcloud = WordCloud(width=2560, height=1440).generate(' '.join(words_filtered))

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
#plt.show()
#plt.savefig('../fig.png')
wordcloud.to_file('../fig.png')