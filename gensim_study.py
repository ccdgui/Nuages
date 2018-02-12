"""
Topic Modeling Study using Spacy and Gensim libraries.
Input: Unstructured text data from Health Forum posts (patient.info) about Migraine.
Output: Representation of 5 main topics using pyLDAvis library. 

"""


import json
import spacy 
from spacy.lang.en import English
import en_core_web_sm
nlp = en_core_web_sm.load()
from spacy.tokenizer import Tokenizer
from gensim import corpora, models, similarities
from gensim.models import Phrases
from gensim.models.phrases import Phraser
import pyLDAvis.gensim


# In[42]:

#blog posts are saved in json format  
with open('/home/StrobiHealth/Nuages/input_raw_data/raw_forum_data.json') as json_data:
    raw_data = json.load(json_data)


# In[58]:

#Tokenize document, remove space, stop words and punctuation with Spacy
def tokenize(sent):
    lda_tokens = []
    for token in list(sent):
        if token.orth_.isspace():
            continue
        elif token.is_stop:
            continue
        elif token.is_punct: 
            continue    
        elif token.lemma_ == '-PRON-':  
            continue
        elif len(token) < 4: 
            continue
        else:
            lda_tokens.append(lemmatize(token))
    return lda_tokens


# In[59]:

#Word lemmatization with Spacy  
def lemmatize(token):
    if token.lemma_ == '-PRON-':
        return token.text
    else: 
        return token.lemma_


# In[60]:

#Chunks source text into sentences and call tokenizer and lemmatizer functions 
def cleanup(bubble):        
    nlp_text = nlp(bubble)
    chunk_sents = []
    for sent in nlp_text.sents:
        token_sent = tokenize(sent)       
        chunk_sents.append(token_sent)
    return chunk_sents


# In[61]:

#Updates Gensim dictionary that assigns an integer id to all words appearing in the corpus 
def update_dict(clean_bubble): 
    dictionary.add_documents(clean_bubble)
    dictionary.save('/home/StrobiHealth/Nuages/gensim_models/gensim_json.dict')
    vector_bubble = [dictionary.doc2bow(text, allow_update=True) for text in clean_bubble]
    return vector_bubble


# In[62]:

#Iterates through the raw text, calls tokenizer function and updates Gensim LDA Function 
dictionary = corpora.Dictionary()
dictionary.save('/home/StrobiHealth/Nuages/gensim_models/gensim_json.dict')
bubble = "" 
for item in raw_data: 
    id = item['bubble_id']
    for text in item['bubble_content']: 
        bubble += text
cleanup_bubble = cleanup(bubble)
vector_bubble = update_dict(cleanup_bubble)
lda_model = models.LdaModel(vector_bubble, id2word=dictionary, num_topics=5)
show_topic = lda_model.show_topics(num_topics=5)


# In[63]:

#display topics pyLDAvis Library
pyLDAvis.enable_notebook()
pyLDAvis.gensim.prepare(lda_model, vector_bubble, dictionary)
