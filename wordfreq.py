import pandas as pd
import nltk
from collections import Counter
from string import punctuation

train = pd.read_csv("E:\\RumorDetection\\train.csv",encoding='latin1')
test = pd.read_csv("E:\\RumorDetection\\test.csv",encoding='latin1')

content_train_fake = train[train['label']==1]
content_test_fake = test[test['label']==1]
content_train_nofake = train[train['label']==0]
content_test_nofake = test[test['label']==0]

content_train_fake = content_train_fake['text']
content_test_fake = content_test_fake['text']

content_train_nofake = content_train_nofake['text']
content_test_nofake = content_test_nofake['text']

stopwords = set(nltk.corpus.stopwords.words('english'))

word_count = Counter()
total = 0
for line in content_train_fake:
    line = line.encode("ascii", "ignore").decode()
    spl = line.split()
    filtered_sentence = [w.lower().rstrip(punctuation) for w in spl if w.lower() not in stopwords]
    tagged = nltk.pos_tag([word for word in filtered_sentence if word])
    for i in tagged:
        # print(i)
        if len(i[0]) != 0 or len(i[0]) != 1 or len(i[0]) != 2:

            if i[1] == 'IN' or i[1] == 'DT' or i[1] == 'CD' or i[1] == 'CC' or i[1] == 'EX' or i[1] == 'MD' or i[
                1] == 'WDT' or i[1] == 'WP' or i[1] == 'UH' or i[1] == 'TO' or i[1] == 'RP' or i[1] == 'PDT' or i[
                1] == 'PRP' or i[1] == 'PRP$' or i[0] == 'co' or i[1]=='RB' or i[1]=='RBR' or i[1] == 'JJ' or i[1]=='RBS' or i[0]=='said'or i[0]=='mr'or i[0]=='states':
                # print(i[0])
                continue
            else:
                # print(i[0])
                # print(type(i[0]))
                total+=1
                word_count.update([i[0]])
                # print(word_count)

for line in content_test_fake:
    line = line.encode("ascii", "ignore").decode()
    spl = line.split()
    filtered_sentence = [w.lower().rstrip(punctuation) for w in spl if w.lower() not in stopwords]
    tagged = nltk.pos_tag([word for word in filtered_sentence if word])
    for i in tagged:
        if len(i[0]) != 0 or len(i[0]) != 1 or len(i[0]) != 2:

            if i[1] == 'IN' or i[1] == 'DT' or i[1] == 'CD' or i[1] == 'CC' or i[1] == 'EX' or i[1] == 'MD' or i[
                1] == 'WDT' or i[1] == 'WP' or i[1] == 'UH' or i[1] == 'TO' or i[1] == 'RP' or i[1] == 'PDT' or i[
                1] == 'PRP' or i[1] == 'PRP$' or i[0] == 'co' or i[1]=='RB' or i[1]=='RBR' or i[1] == 'JJ' or i[1]=='RBS' or i[0]=='said' or i[0]=='mr'or i[0]=='states':
                # print(i[0])
                continue
            else:
                total+=1
                word_count.update([i[0]])
    # word_count.update(w.lower().rstrip(punctuation) for w in spl if w.lower() not in stopwords)

print([x for x in word_count.most_common(20)])
print(total)

word_count = Counter()
total = 0
for line in content_train_nofake:
    line = line.encode("ascii", "ignore").decode()
    spl = line.split()
    filtered_sentence = [w.lower().rstrip(punctuation) for w in spl if w.lower() not in stopwords]
    tagged = nltk.pos_tag([word for word in filtered_sentence if word])
    for i in tagged:
        # print(i)
        if len(i[0]) != 0 or len(i[0]) != 1 or len(i[0]) != 2:

            if i[1] == 'IN' or i[1] == 'DT' or i[1] == 'CD' or i[1] == 'CC' or i[1] == 'EX' or i[1] == 'MD' or i[
                1] == 'WDT' or i[1] == 'WP' or i[1] == 'UH' or i[1] == 'TO' or i[1] == 'RP' or i[1] == 'PDT' or i[
                1] == 'PRP' or i[1] == 'PRP$' or i[0] == 'co' or i[1]=='RB' or i[1]=='RBR' or i[1] == 'JJ' or i[1]=='RBS':
                # print(i[0])
                continue
            else:
                # print(i[0])
                # print(type(i[0]))
                total+=1
                word_count.update([i[0]])
                # print(word_count)

for line in content_test_nofake:
    line = line.encode("ascii", "ignore").decode()
    spl = line.split()
    filtered_sentence = [w.lower().rstrip(punctuation) for w in spl if w.lower() not in stopwords]
    tagged = nltk.pos_tag([word for word in filtered_sentence if word])
    for i in tagged:
        if len(i[0]) != 0 or len(i[0]) != 1 or len(i[0]) != 2:

            if i[1] == 'IN' or i[1] == 'DT' or i[1] == 'CD' or i[1] == 'CC' or i[1] == 'EX' or i[1] == 'MD' or i[
                1] == 'WDT' or i[1] == 'WP' or i[1] == 'UH' or i[1] == 'TO' or i[1] == 'RP' or i[1] == 'PDT' or i[
                1] == 'PRP' or i[1] == 'PRP$' or i[0] == 'co' or i[1]=='RB' or i[1]=='RBR' or i[1] == 'JJ' or i[1]=='RBS' :
                # print(i[0])
                continue
            else:
                total+=1
                word_count.update([i[0]])
    # word_count.update(w.lower().rstrip(punctuation) for w in spl if w.lower() not in stopwords)

print([x for x in word_count.most_common(20)])
print(total)