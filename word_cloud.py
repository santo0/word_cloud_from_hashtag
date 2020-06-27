from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import sys
from dec_timer import timer
text_eng = "This would obviously depend on the time period and the military force. I am assuming you are talking about times before modern warfare as modern warfare treats rank and positions quite differently then before. Field promotions are usually conducted by any superior officer as positions needs to be filled. But they are usually just temporary promotions for the campaign until a better replacement can be found. So it does not come with any additional pay or rights. Military units usually keeps a log over everything that happens including field promotions. The officer would often send letters to his superiors recommending people for permanent promotions. If this is granted the promotion becomes permanent and would come with a pay raise. An officer might have a quota for how many people of different rank he would be allowed to promote. It might also have been up to the military education facilities to decide who would be promoted but the recommendations would help a lot, especially if exams did not go well."
text_esp = "Crónicas kafkianas, capítulo MMCXVII. La curva de legislación chapucera en España se dispara a un ritmo exponencial que la pandemia jamás logró alcanzar. Ya saben, por ejemplo, que los turistas llegan por miles de Alemania pero ir a Logroño a ver a tus padres era, hasta hace unos días, algo peligroso. Desplazarse en el metro o el autobús a currar no presenta riesgos por aproximación de aliento y sobaco pero en los teatros hay que dejar dos metros de perímetro seguro. En un avión, viajeros-ganado; en una oficina de banco, peligrosos focos de contagio. Y así, «ad náuseam».Ahora les llega el turno a las discotecas. En Cataluña, por ejemplo, acaban de autorizar el baile, pero debes hacerlo con tu tribu. Nada de mezclarse con los no convivientes. La distancia no está regulada, es decir, se permiten tanto chotis como sardanas y el perreo o el «brikindans», pero la mezcla está prohibida. Las discotecas obligarán a los intrépidos danzarines a inscribirse y a bailar solo con personas con las que mantengan un «contacto muy habitual» para que, en caso de fiebre del sábado noche, todo quede en familia: bienvenidos al «apartheid» de la fiesta, a los clanes de Capuletos y Montescos."
#text_cat = "I ara vostè em preguntarà: Per què sorpresa i per què agradable? Primer pel contingut. Estradé planteja una crítica urbi et orbe, global. No només als “altres”, com és habitual, sinó també als “uns”. És una esmena a la totalitat, cosa que cada cop costa més veure. I llegir. I després perquè planteja una reflexió autocrítica, una cosa més difícil que veure jugar Démbélé. Efectivament, al final tot això del suplicatori a Laura Borràs ha anat de tot menys de Laura Borràs. JuntsxCat/PDeCAT, Esquerra i la CUP l'han usat per desgastar-se a base de retrets de vol gal·linaci i deixant de banda que estàvem parlant d'un sistema de contractes que absolutament totes (TO-TES) les administracions usen. Serà més o menys lleig però si ens toquen la manera de fer contractes d'una, cal tocar la manera de fer els contractes de totes. Perquè si no és així, la cosa fa pudor a deloscobisme."


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
    # return filter(lambda w: w.lower() not in stop_words, words)
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
    wordcloud.to_file('static/temporary_files/fig.png')


if __name__ == '__main__':
    filtered_text = get_filtered_text(text_esp, 'spanish')
    draw_word_cloud(filtered_text)