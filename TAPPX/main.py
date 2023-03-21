# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/21 15:00:20 by dacortes          #+#    #+#              #
#    Updated: 2023/03/21 15:00:22 by dacortes         ###   ########.fr        #
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
        res = np.dot(m_video, m_article)/(np.linalg.norm(m_video)*np.linalg.norm(m_article))
        scores.append((res, i, df['categoriaIAB'][i][0]['class']))
    scores.sort(reverse=True)
    return (scores)

def analyze_score(socore):

    if socore < 0.25:
        print("False")
        return (False)
    else :
        print("True")
        return (True)
    
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
    article = df_article['text'][in_article[0]]
###............................... Score ....................................###
    scores = analyze_key(df_video, article)
    sc1 = scores[0][0]
    sc2 = scores[1][0]
    analyze_score (sc1)
    id1 = scores[0][1]
    id2 = scores[1][1]
    id3 = scores[2][1]
    print("Analicis")
    print("videos que dieron resultado true :",in_video[id1], in_video[id2], in_video[id3])
    print("articulo analizado :",in_article[0])
    print(scores)
###............................... Test .....................................###
''' out_video = extract_info(df_video, in_video[0], 'text')
    out_article = extract_info(df_article, in_article[0], 'text')
    print("id :",in_video[0], "\ncontent :\n",out_video)
    print("id :",in_article[0], "\ncontent :\n",out_article)'''