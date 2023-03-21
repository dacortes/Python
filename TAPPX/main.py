# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/21 15:00:20 by dacortes          #+#    #+#              #
#    Updated: 2023/03/21 15:04:33 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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

    if socore < 0.25 and type == 'keywords':
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

def analyze_everything(df_video):
    i = 0
    while i < len(in_article):
        article = df_article['keywords'][in_article[i]]
        scores = score_key(df_video, article)
        print(f"El articulo #:\n{i}\nid:\n{in_article[i]}\nscores:\n")
        print(scores)
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
    print(f"las row :{df_article.shape[0]}")
    print(range(len(df_video)))
    print(len(in_article))
    #analyze_everything(df_video)
###............................... Score ....................................###
    i = 0
'''    while i < 12 :
        article = df_article['keywords'][in_article[i]]
        article = ' '.join(df_article['keywords'][i])
        scores = analyze_key(df_video, article)
        sc1 = scores[0][0]
        sc2 = scores[1][0]
        id1 = scores[0][1]
        id2 = scores[1][1]
        id3 = scores[2][1]
        print("Analicis")
        print("videos que dieron resultado true :",in_video[id1], in_video[id2], in_video[id3])
        print("articulo analizado :",in_article[i])
        print(scores)
        i += 1'''