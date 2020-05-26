import nltk
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import wordnet

filename = ''

def isEnglish(word):
    list=word.split()

    if(len(list) == 3):
        if (wordnet.synsets(list[0]) and wordnet.synsets(list[1])):
            return True
    
    return False

def readFile():
    fileRead= open('Corpus/'+filename,'r')
    lines= fileRead.readlines()

    fileWrite= open('English/'+filename+'.eng','w')        
    for l in lines:
        if (isEnglish(l)):
            fileWrite.writelines(l.lower())
        
    fileWrite.close()
    fileRead.close()

def fileLemmatization():
    lemma=WordNetLemmatizer()

    fileRead= open('English/'+filename+'.eng','r')
    lines= fileRead.readlines()

    fileWrite= open('Lemmatization/'+filename+'.lem','w')        
    for l in lines:
        list=l.split()
        var1=lemma.lemmatize(list[0],'n')
        if var1==list[0]:
            var1=lemma.lemmatize(list[0],'v')
        if var1==list[0]:
            var1=lemma.lemmatize(list[0],'a')
        
        var2=lemma.lemmatize(list[1],'n')
        if var2==list[1]:
            var2=lemma.lemmatize(list[1],'v')
        if var2==list[1]:
            var2=lemma.lemmatize(list[1],'a')

        line=var1+' '+var2+'\t'+list[2]+'\n'    
        fileWrite.writelines(line)

    fileWrite.close()
    fileRead.close()

    
def fileFactorize():
    fileRead= open('Lemmatization/'+filename+'.lem','r')
    lines= fileRead.readlines()

    fileWrite= open('Factorization/'+filename+'.fac','w')
    
    vector = {}
    for l in lines:
        list=l.split()

        tup = (list[0], list[1])
        if(tup not in vector):
            vector[tup] = int(list[2])
        else:
            vector[tup] = vector[tup] + int(list[2])

    for i in vector:
        fileWrite.write(i[0] + ' ' + i[1] + ' ' + str(vector[i]) + '\n')

    fileWrite.close()
    fileRead.close()
    
    vector.clear()


filenames = ['2gm-0000','2gm-0001','2gm-0002','2gm-0003','2gm-0004','2gm-0005','2gm-0006','2gm-0007','2gm-0008','2gm-0009',
            '2gm-0010','2gm-0011','2gm-0012','2gm-0013','2gm-0014','2gm-0015','2gm-0016','2gm-0017','2gm-0018','2gm-0019',
            '2gm-0020','2gm-0021','2gm-0022','2gm-0023','2gm-0024','2gm-0025','2gm-0026','2gm-0027','2gm-0028','2gm-0029',
            '2gm-0030','2gm-0031']

for filen in filenames:
    filename = filen
    
    print('Init ' + filename)
    readFile()
    print("End English")
    fileLemmatization()
    print("End Lemmatization")
    fileFactorize()
    print("End Factorization\n")
