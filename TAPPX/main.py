# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dacortes <dacortes@student.42barcelona.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/03/21 15:00:20 by dacortes          #+#    #+#              #
#    Updated: 2023/03/22 15:55:21 by dacortes         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

'''.................................. libraries .............................'''

from termcolor import colored
from tqdm import tqdm
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

def analyze_score(socore, video):
    if socore < 0.27:
        #print( f"id: {in_video[video]} status:" + colored(" False", "red")
        #      + colored("\nvalue:","blue") + f" {socore}")
        return (False)
    else :
        #print( f"id: {in_video[video]} status:" + colored(" True", "green")
        #     + colored("\nvalue:","blue") + f"{socore}")
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

def push_dic_dic(dic, id_article, id_video, score):
    if id_article not in dic:
        dic[id_article] = {}
    if id_video not in dic[id_article]:
        dic[id_article][id_video] = {}
    dic[id_article][id_video]['score'] = score  

def push_dic(dic, id_article):
    dic[id_article] = {}


def analyze_keywords(df_video):
    i = 0
    num = 1
    tittle = colored("Analisis por keywords", attrs=["bold"])
    print("............ "+ colored(tittle, "blue") + " ............")
    pbar = tqdm(total=len(in_article))
    while i < len(in_article):
        article = df_article['keywords'][in_article[i]]
        article = ' '.join(df_article['keywords'][i])
        scores = score_key(df_video, article)
        #print(colored("Numero de articulo:","blue") + f" {num}\nid: {in_article[i]}")
        v1 = round((scores[0][0] * 10), 1)
        id1 = scores[0][1]
        v2 = round((scores[1][0] * 10), 1)
        id2 = scores[1][1]
        tittle = colored("Analisis del score", attrs=["bold"])
        #print("=====>"+ colored(tittle, "blue"))
        analyze_score(v1, id1)
        analyze_score(v2, id2)
        push_dic(dic_outut, in_article[i])
        push_dic_dic(dic_outut, in_article[i], in_video[id1], str(v1))
        push_dic_dic(dic_outut, in_article[i], in_video[id2], str(v2))
        i += 1
        num += 1
        pbar.update(1)
    pbar.close()

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
    dic_outut = {}
    in_video = df_video.index
    in_article = df_article.index
    print(colored(f"la cantidad de articulos para analizar es:", "blue") +
          f" {df_article.shape[0]}")
    print(colored(f"videos con los que se pueden relacionar:", "blue") +
          f" {df_video.shape[0]}")
###............................... Score ....................................###
    analyze_keywords(df_video)
    with open('data.json', 'w') as file:
        json.dump(dic_outut, file, indent=2)