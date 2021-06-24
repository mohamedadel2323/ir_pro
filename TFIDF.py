import pandas as pd
import math


document1 = 'Helwan University is a public university based in Helwan , Egypt , which is part of Greater Cairo . It comprises 21 faculties as well as 50 research centers and productive units which connect the university with the problems of the Egyptian society .'
document2 = 'It is generally known for its engineering and business study courses . Especially notable are its Faculties of Engineering , the Faculty of Commerce and Business Administration , with specialized departments dealing with foreign trade , international relations , and business information systems ; the Faculty of Computers & Information ; and the Faculty of Science .'
document3 = 'Faculty of Medicine is the newest faculty of them all , the university hospital is at Badr City . Helwan university also has a Faculty of Nursing , and its Faculty of Pharmacy is known to be the first clinical pharmacy in Egypt .'
document4 = 'Helwan University is a member of the Egyptian Supreme Council of Universities . It was established on July 26 , 1975 by Act No. 70 of 1975 over 350 acres of land . It is the youngest of 3 major governmental universities in Cairo .'
document5 = 'However , it goes back to the 19th century during the reign of Muhammad Ali of Egypt who established “ The Operations School ” . The fields of that school were the basis of many institutes that formed Helwan University later .'
document6 = 'The university possesses all the factors of distinction and diversity . It is considered to be a unique model among Egyptian Universities as it encompasses Arts , Fine arts , Applied arts , Art education , Music education and Physical Education Faculties . Being within the heart of an industrial community , Helwan University is considered a unique model among Egyptian universities in general .'
document7 = 'Although Helwan University is the most recent of 3 major governmental universities in Cairo , it encompasses some of the oldest most faculties in Egypt and Middle East . The Faculty of Applied Arts for example , was established in 1839 , while the Faculty of Fine Arts and Art Education were established in 1908 and 1936 respectively .'
document8 = 'Helwan University also have a number of faculties with special innovative nature , Such as Faculty of Music Education , Faculty of Physical education .'
document9 = 'This campus also hosts a joint Masters Program between Germany and Egypt , named INEMA ( International Education Management ) . The Masters program consists of six attendance phases , three are held at Zamalek Campus in Cairo , three take place at the Pädagogische Hochschule in Ludwigsburg , Germany . The shared Masters program was first established in 2010 .'
document10 = 'According to Webometrics Ranking of World Universities , Helwan University is ranked 2300th in the world and 11th in Egypt .In QS ranking 2018 Helwan University was rated 51-60 in The Arab Region .'




stopWords = ['the', 'a', 'an', 'in','of','that','then','is','are','was','were','out']
bagOfWords1 = document1.split(' ')
bagOfWords2 = document2.split(' ')
bagOfWords3 = document3.split(' ')
bagOfWords4 = document4.split(' ')
bagOfWords5 = document5.split(' ')
bagOfWords6 = document6.split(' ')
bagOfWords7 = document7.split(' ')
bagOfWords8 = document8.split(' ')
bagOfWords9 = document9.split(' ')
bagOfWords10 = document10.split(' ')

bagOfWords1WithoutSW = [word.lower() for word in bagOfWords1 if not word in stopWords]
bagOfWords2WithoutSW = [word.lower() for word in bagOfWords2 if not word in stopWords]
bagOfWords3WithoutSW = [word.lower() for word in bagOfWords3 if not word in stopWords]
bagOfWords4WithoutSW = [word.lower() for word in bagOfWords4 if not word in stopWords]
bagOfWords5WithoutSW = [word.lower() for word in bagOfWords5 if not word in stopWords]
bagOfWords6WithoutSW = [word.lower() for word in bagOfWords6 if not word in stopWords]
bagOfWords7WithoutSW = [word.lower() for word in bagOfWords7 if not word in stopWords]
bagOfWords8WithoutSW = [word.lower() for word in bagOfWords8 if not word in stopWords]
bagOfWords9WithoutSW = [word.lower() for word in bagOfWords9 if not word in stopWords]
bagOfWords10WithoutSW = [word.lower() for word in bagOfWords10 if not word in stopWords]



uniqueWords = set(bagOfWords1WithoutSW).union(set(bagOfWords2WithoutSW)).union(set(bagOfWords3WithoutSW)).union(set(bagOfWords4WithoutSW)).union(set(bagOfWords5WithoutSW)).union(set(bagOfWords6WithoutSW)).union(set(bagOfWords7WithoutSW)).union(set(bagOfWords8WithoutSW)).union(set(bagOfWords9WithoutSW)).union(set(bagOfWords10WithoutSW))


numOfWords1 = dict.fromkeys(uniqueWords, 0)
for word in bagOfWords1WithoutSW:
    numOfWords1[word] += 1

numOfWords2 = dict.fromkeys(uniqueWords, 0)
for word in bagOfWords2WithoutSW:
    numOfWords2[word] += 1

numOfWords3 = dict.fromkeys(uniqueWords, 0)
for word in bagOfWords3WithoutSW:
    numOfWords3[word] += 1

numOfWords4 = dict.fromkeys(uniqueWords, 0)
for word in bagOfWords4WithoutSW:
    numOfWords4[word] += 1

numOfWords5 = dict.fromkeys(uniqueWords, 0)
for word in bagOfWords5WithoutSW:
    numOfWords5[word] += 1

numOfWords6 = dict.fromkeys(uniqueWords, 0)
for word in bagOfWords6WithoutSW:
    numOfWords6[word] += 1

numOfWords7 = dict.fromkeys(uniqueWords, 0)
for word in bagOfWords7WithoutSW:
    numOfWords7[word] += 1

numOfWords8 = dict.fromkeys(uniqueWords, 0)
for word in bagOfWords8WithoutSW:
    numOfWords8[word] += 1

numOfWords9 = dict.fromkeys(uniqueWords, 0)
for word in bagOfWords9WithoutSW:
    numOfWords9[word] += 1

numOfWords10 = dict.fromkeys(uniqueWords, 0)
for word in bagOfWords10WithoutSW:
    numOfWords10[word] += 1

def computeTF(wordDict, bagOfWords):
    tfDict = dict()
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items():
        tfDict[word] = round(math.log10( 1 + (count / float(bagOfWordsCount))),10)
    return tfDict

tf1 = computeTF(numOfWords1, bagOfWords1WithoutSW)
tf2 = computeTF(numOfWords2, bagOfWords2WithoutSW)
tf3 = computeTF(numOfWords3, bagOfWords3WithoutSW)
tf4 = computeTF(numOfWords4, bagOfWords4WithoutSW)
tf5 = computeTF(numOfWords5, bagOfWords5WithoutSW)
tf6 = computeTF(numOfWords6, bagOfWords6WithoutSW)
tf7 = computeTF(numOfWords7, bagOfWords7WithoutSW)
tf8 = computeTF(numOfWords8, bagOfWords8WithoutSW)
tf9 = computeTF(numOfWords9, bagOfWords9WithoutSW)
tf10 = computeTF(numOfWords10, bagOfWords10WithoutSW)

print('\n')
print('Term Frequancy for 10 documents: ')
print('\n')
print(tf1)
print('\n')
print(tf2)
print('\n')
print(tf3)
print('\n')
print('\n')
print(tf4)
print('\n')
print(tf5)
print('\n')
print(tf6)
print('\n')
print('\n')
print(tf7)
print('\n')
print(tf8)
print('\n')
print(tf9)
print('\n')
print(tf10)
print('\n')


def computeIDF(documents):
    N = len(documents)
    
    idfDict = dict.fromkeys(documents[0].keys(), 0)
    for document in documents:
        for word, val in document.items():
            if val > 0:
                idfDict[word] += 1
    
    for word, val in idfDict.items():
        idfDict[word] = round(math.log10(N / float(val)),2)
    return idfDict

idfs = computeIDF([numOfWords1, numOfWords2, numOfWords3,numOfWords4,numOfWords5,numOfWords6,numOfWords7,numOfWords8,numOfWords9,numOfWords10])

print('Inverted Document Frequancy for 10 documents: ')
print('\n')
print(idfs)
print('\n')


def computeTFIDF(tfBagOfWords, idfs):
    tfidf = dict()
    for word, val in tfBagOfWords.items():
        tfidf[word] = round(val * idfs[word],10)
    return tfidf

tfidf1 = computeTFIDF(tf1, idfs)
tfidf2 = computeTFIDF(tf2, idfs)
tfidf3 = computeTFIDF(tf3, idfs)
tfidf4 = computeTFIDF(tf4, idfs)
tfidf5 = computeTFIDF(tf5, idfs)
tfidf6 = computeTFIDF(tf6, idfs)
tfidf7 = computeTFIDF(tf7, idfs)
tfidf8 = computeTFIDF(tf8, idfs)
tfidf9 = computeTFIDF(tf9, idfs)
tfidf10 = computeTFIDF(tf10, idfs)


df = pd.DataFrame([tfidf1, tfidf2, tfidf3,tfidf4,tfidf5,tfidf6,tfidf7,tfidf8,tfidf9,tfidf10])

print('TFIDF for 10 documents: ')
print('\n')
print(df)












