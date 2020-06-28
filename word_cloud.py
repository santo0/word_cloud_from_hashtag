from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import sys
import os
from dec_timer import timer


def get_stop_words_by_language(lang):
    if lang == 'english':
        # this can be reduced, but it's done this way for clarity in further implementations
        return stopwords.words('english')
    elif lang == 'spanish':
        return stopwords.words('spanish')
    else:
        sys.exit(1)

def get_filtered_text(text, lang):
    stop_words = set(get_stop_words_by_language(lang))
    words = word_tokenize(text, language=lang)
    words_filtered = []
    for w in words:
        w_lowered = w.lower()
        if w_lowered not in stop_words:
            words_filtered.append(w_lowered)
    return ' '.join(words_filtered)

@timer
def draw_word_cloud(filtered_text):
    wordcloud = WordCloud(width=2560, height=1440).generate(filtered_text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    try:
        os.remove('static/temporary_files/fig100.png')
    except FileNotFoundError:
        pass
    wordcloud.to_file('static/temporary_files/fig100.png')

