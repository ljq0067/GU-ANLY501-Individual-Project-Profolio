import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

path = "D:/Jieqian Liu/Data Science and Analystics/ANLY501 Data Science & Analytics/Individual Project Profolio/data gathering/API_R/News/"
file = "online-shopping.csv"
CSV_DF = pd.read_csv(path + file)

print(CSV_DF.head())
# iterating the columns
for col in CSV_DF.columns:
    print(col)

# REMOVE any rows with NaN in them
CSV_DF = CSV_DF.dropna()
# Create the list of description
DescriptionLIST = []
for next1 in CSV_DF["description"]:
    DescriptionLIST.append(next1)

print("The description list is")
print(DescriptionLIST)

# Vectorized
MyCountV = CountVectorizer(
    input="content",
    lowercase=True,
    stop_words="english"
)

MyDTM = MyCountV.fit_transform(DescriptionLIST)  # create a sparse matrix
print(type(MyDTM))
# vocab is a vocabulary list
vocab = MyCountV.get_feature_names()  # change to a list
print(list(vocab)[10:20])

MyDTM = MyDTM.toarray()  # convert to a regular array
print(type(MyDTM))

ColumnNames = MyCountV.get_feature_names()
MyDTM_DF = pd.DataFrame(MyDTM, columns=ColumnNames)
print(MyDTM_DF)

num_topics = 5

lda_model_DH = LatentDirichletAllocation(n_components=num_topics,
                                         max_iter=100, learning_method='online')
LDA_DH_Model = lda_model_DH.fit_transform(MyDTM_DF)

print("SIZE: ", LDA_DH_Model.shape)  # (NO_DOCUMENTS, NO_TOPICS)

# Let's see how the first document in the corpus looks like in
## different topic spaces
print("First description...")
print(LDA_DH_Model[0])
print("Sixth description...")
print(LDA_DH_Model[5])

## implement a print function
def print_topics(model, vectorizer, top_n=10):
    for idx, topic in enumerate(model.components_):
        print("Topic:  ", idx)

        print([(vectorizer.get_feature_names()[i], topic[i])
               for i in topic.argsort()[:-top_n - 1:-1]])
        ## gets top n elements in decreasing order

# call the function above with our model and CountV
print_topics(lda_model_DH, MyCountV)

word_topic = np.array(lda_model_DH.components_)
# print(word_topic)
word_topic = word_topic.transpose()

num_top_words = 15
vocab_array = np.asarray(vocab)

# fontsize_base = 70 / np.max(word_topic)  # font size for word with largest share in corpus
fontsize_base = 15

for t in range(num_topics):
    plt.subplot(1, num_topics, t + 1)  # plot numbering starts with 1
    plt.ylim(0, num_top_words + 0.5)  # stretch the y-axis to accommodate the words
    plt.xticks([])  # remove x-axis markings ('ticks')
    plt.yticks([])  # remove y-axis markings ('ticks')
    plt.title('Topic #{}'.format(t))
    top_words_idx = np.argsort(word_topic[:, t])[::-1]  # descending order
    top_words_idx = top_words_idx[:num_top_words]
    top_words = vocab_array[top_words_idx]
    top_words_shares = word_topic[top_words_idx, t]
    for i, (word, share) in enumerate(zip(top_words, top_words_shares)):
        plt.text(0.3, num_top_words - i - 0.5, word, fontsize=fontsize_base)
        ##fontsize_base*share)

plt.tight_layout()
plt.show()
