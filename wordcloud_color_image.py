
#color image
from wordcloud import WordCloud,STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt 
import matplotlib 
from matplotlib import rc
import nltk 
from nltk.corpus import stopwords
import numpy as np
import pandas as pd
import csv
from importlib import reload
import ast
import requests
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import os

#rc('font', family='NanumBarunGothic')


from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

rc('font', family='NanumBarunGothic')

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
#d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()


# Read the whole text.
text = open(r'txt파일 주소.txt').read()

# read the mask / color image taken from
# http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010
alice_coloring = np.array(Image.open(( r"C:\Users\HaEunMok\Desktop\career.png")))
stopwords = set(STOPWORDS)
stopwords.add("said")

font_path = r'폰트위치'
wc = WordCloud(background_color="white", font_path = font_path,
               max_words=2000, mask=alice_coloring,
               stopwords=stopwords, max_font_size=40, random_state=42)
# generate word cloud
wc.generate(text)

# create coloring from image
image_colors = ImageColorGenerator(alice_coloring)


plt.figure(figsize=(10, 10))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")


# show
#fig, axes = plt.subplots(1, 3)
#axes[0].imshow(wc, interpolation="bilinear")
# recolor wordcloud and show
# we could also give color_func=image_colors directly in the constructor
#axes[1].imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
#axes[2].imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
#for ax in axes:
#    ax.set_axis_off()

#plt.show()
plt.savefig("저장할 png파일명", format="png")
plt.show()
