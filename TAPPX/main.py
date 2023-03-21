# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/21 15:00:20 by dacortes          #+#    #+#              #
#    Updated: 2023/03/21 15:29:13 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from termcolor import colored
import pandas as pd
import json
import numpy as np
from sentence_transformers import SentenceTransformer

'''................................ Funtions ................................'''

def read_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return  (data)

def extract_info(df, index, search):
    return (df.loc[index, search])

def analyze_key(df, article):
    scores = []
    for i in range(len(df)):
        video = ' '.join(df['keywords'][i])
        m_video = model.encode(video)
        m_article = model.encode(article)
        res = np.dot(m_article, m_video)/(np.linalg.norm(m_article)*np.linalg.norm(m_video))
        scores.append((res, i, df_video.index[i]))
    scores.sort(reverse=True)
    return (scores)

def analyze_score(socore, type):

    if socore < 0.27 and type == 'keywords':
        print("False")
        return (False)
    elif socore < 1.2 and type == 'title':
        print("False")
        return (False)
    else :
        print("True")
        return (True)

def score_key(df, article):
    scores = []
    i = 0
    while i < len(in_video):
        video = ' '.join(df['keywords'][i])
        m_video = model.encode(video)
        m_article = model.encode(article)
        res = np.dot(m_article, m_video)/(np.linalg.norm(m_article)*np.linalg.norm(m_video))
        scores.append((res, i, df_video.index[i]))
        i += 1
    scores.sort(reverse=True)
    return (scores)

def analyze_keywords(df_video):
    i = 0
    while i < len(in_article):
        article = df_article['keywords'][in_article[i]]
        article = ' '.join(df_article['keywords'][i])
        scores = score_key(df_video, article)
        print(f"El articulo #:\n{i}\nid:\n{in_article[i]}\nscores:\n{scores}")
        i += 1

def analyze_title(df_video):
    i = 0
    while i < len(in_article):
        article = df_article['title'][in_article[i]]
        scores = score_key(df_video, article)
        print(f"El articulo #:\n{i}\nid:\n{in_article[i]}\nscores:\n{scores}")
        i += 1
    
'''.................................. Vars ..................................'''

model = SentenceTransformer('sentence-transformers/distiluse-base-multilingual-cased-v1')

'''.................................. Main ..................................'''

if __name__ == "__main__":
###............................... Read.json ................................###
    df_video = read_json('videos.json')
    df_article = read_json('articles.json')
    df_video = pd.DataFrame.from_dict(df_video, orient='index')
    df_article = pd.DataFrame.from_dict(df_article, orient='index')
###............................... Index.json ...............................###
    in_video = df_video.index
    in_article = df_article.index
    print(colored(f"la cantidad de articulos para analizar es:", "blue") +
          f" {df_article.shape[0]}")
    print(colored(f"videos con los que se pueden relacionar:", "blue") +
          f" {df_video.shape[0]}")
###............................... Score ....................................###
    #analyze_keywords(df_video)