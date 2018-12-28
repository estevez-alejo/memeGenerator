from nider.core import Font
from nider.core import Outline

from nider.models import Content
from nider.models import Linkback
from nider.models import Paragraph
from nider.models import Image

from PIL import ImageEnhance
from PIL import ImageFilter

from google_images_download import google_images_download

from random import randint
import sys
import pdb
import wikiquote
import uuid

# TODO: change this fontpath to the fontpath on your machine
roboto_font_folder = '/home/alejo/.local/share/fonts/roboto/'

text_outline = Outline(1, '#121212')

autores = ['Julio Iglesias', 'Diego Armando Maradona', 'Carlos Menem', 'Carlos Salvador Bilardo', 'Adolf Hitler', 'Susana Gimenez', 
           'Hector Veira', 'Juan Domingo Perón', 'Woody Allen', 'Groucho Marx',
            'Nicolas Maduro']

for a in autores:

    response = google_images_download.googleimagesdownload()
    arguments = {"keywords":a,"limit":25,"print_urls":True,"size":"medium"}
    #print(a)
    paths = response.download(arguments)
    i=0
    for q in wikiquote.quotes(a, lang='es', max_quotes=25):

        if len(q) <= 256:

            para = Paragraph(text='"'+q+'"',
                             font=Font(roboto_font_folder + 'Roboto-Medium.ttf', 25),
                             text_width=35,
                             align='center',
                             color='#ffff00',
                             outline=text_outline
                             )

            linkback = Linkback(text='@quienlodice',
                                font=Font(roboto_font_folder + 'Roboto-Bold.ttf', 20),
                                color='#efefef',
                                outline=text_outline
                                )

            content = Content(paragraph=para, linkback=linkback)

            img = Image(content,
                        fullpath=a+'-'+str(uuid.uuid4())+'.png',
                        width=640,
                        height=480
                        )

            # TODO: change this texture path to the texture path on your machine
            img.draw_on_texture(paths[a][i])
            i = i + 1
