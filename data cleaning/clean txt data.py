import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

path = "D:/Jieqian Liu/Data Science and Analystics/ANLY501 Data Science & Analytics/Individual Project Profolio/data gathering/API_Python/News/"
file = " amazon-news.txt"
TXT_DF = pd.read_csv(path + file)

# description = TXT_DF["description"]
text = "".join(description for description in TXT_DF.description)
# Create and generate a word cloud image:
wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
# Save the image in the img folder:
wordcloud.to_file("wordcloud.png")

