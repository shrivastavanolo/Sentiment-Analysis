import pandas as pd
from newspaper import Article
import re
import numpy as np

df=pd.read_excel("C:/Users/shrey/Dropbox/PC/Downloads/Input.xlsx")

df["POSITIVE SCORE"]=np.nan
df["NEGATIVE SCORE"]=np.nan
df["POLARITY SCORE"]=np.nan
df["SUBJECTIVITY SCORE"]=np.nan
df["AVERAGE SENTENCE LENGTH"]=np.nan
df["PERCENTAGE OF COMPLEX WORDS"]=np.nan
df["FOG INDEX"]=np.nan
df["AVG NUMBER OF WORDS PER SENTENCE"]=np.nan
df["COMPLEX WORD COUNT"]=np.nan
df["SYLLABLE PER WORD"]=np.nan
df["AVG WORD LENGTH"]=np.nan

with open("stopwords.txt","r+") as file2:
    lines=file2.readlines()
    stopwords = [word.strip() for word in lines]

    with open("positive-words.txt","r+") as pw:
        file4=pw.readlines()
        pword = [word.strip() for word in file4 if not word in stopwords]

    with open("negative-words.txt","r+") as nw:
        file5=nw.readlines()
        nword = [word.strip() for word in file5 if not word in stopwords]

for ind in df.index:
    txtname=str(df['URL_ID'][ind])

    with open(txtname,"w+",encoding="utf-8") as file1:
        url=str(df["URL"][ind])
        try:
            article=Article(url,language="en")
            article.download()
            article.parse()
            file1.writelines(article.title)
            file1.write("\n")
            file1.writelines(article.text)
        except:
            print(url)
        else:
            pass

for ind in df.index:
    txtname=str(df['URL_ID'][ind])

    with open(txtname,"r+",encoding="utf-8") as file1:        
        sentences=file1.readlines()
        file33=" ".join(sentences)
        review = re.sub('[^a-zA-Z0-9]',' ',file33)
        review = review.lower()   
        review = review.split()
        review = [word.strip() for word in review if not word in stopwords]
        wordslen=len(review)
        sentenceslen=len(sentences)
        neg=0
        pos=0
        complexc=0
        pronoun=0
        syll=0
        lenofin=0
        for word in review:
            syllable=0
            if word.strip() in ["i","we","my","ours","us"]:
                pronoun+=1            
            if word in nword:
                neg+=1
            if word in pword:
                pos+=1
            for i in word:
                lenofin+=1
                if i in "aeiou":
                    syllable+=1
            if syllable>2:
                complexc+=1
            syll+=syllable
        polscore=(pos-neg)/((pos+neg) + 0.000001)
        subscore=(pos+ neg)/ ((len(review)) + 0.000001)
        try:
            df.loc[ind,'POSITIVE SCORE']=pos
            df.loc[ind,"NEGATIVE SCORE"]=neg
            df.loc[ind,"POLARITY SCORE"]=polscore
            df.loc[ind,"SUBJECTIVITY SCORE"]=subscore
            df.loc[ind,"AVERAGE SENTENCE LENGTH"]=wordslen/sentenceslen
            df.loc[ind,"PERCENTAGE OF COMPLEX WORDS"]=complexc/wordslen
            df.loc[ind,"FOG INDEX"]=0.4*(wordslen/sentenceslen)+(complexc/wordslen)
            df.loc[ind,"AVG NUMBER OF WORDS PER SENTENCE"]=wordslen/sentenceslen
            df.loc[ind,"COMPLEX WORD COUNT"]=complexc
            df.loc[ind,"WORD COUNT"]=wordslen
            df.loc[ind,"SYLLABLE PER WORD"]=syll/wordslen
            df.loc[ind,"PERSONAL PRONOUNS"]=pronoun
            df.loc[ind,"AVG WORD LENGTH"]=lenofin/wordslen
        except:
            print("error",ind,wordslen,sentenceslen)
        else:
            pass

#Checking df
df.head()

#Converting df to excel sheet
df.to_excel("output.xlsx")