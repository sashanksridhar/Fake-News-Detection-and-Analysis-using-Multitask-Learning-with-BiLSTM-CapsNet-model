import nltk
from collections import Counter
from string import punctuation
import pandas as pd

test = pd.read_csv("E:\\RumorDetection\\test.csv",encoding='latin1')
content_test_fake = test['text']
stopwords = set(nltk.corpus.stopwords.words('english'))

with open("Rumoroutput.txt","r") as reader:
    class_0 = 0
    class_1 = 0
    class_2 = 0
    class_3 = 0
    class_4 = 0
    class_5 = 0

    word_count0 = Counter()
    word_count1 = Counter()
    word_count2 = Counter()
    word_count3 = Counter()
    word_count4 = Counter()
    word_count5 = Counter()

    total0 = 0
    total1 = 0
    total2 = 0
    total3 = 0
    total4 = 0
    total5 = 0

    linenum = 0

    lines = reader.readlines()
    for line in lines:
        num = float(line)
        # print(num)

        # if num > 0.99:
        #     print(num)
        if num <= 0.5:
            text = content_test_fake[linenum]
            text = text.encode("ascii", "ignore").decode()
            spl = text.split()
            filtered_sentence = [w.lower().rstrip(punctuation) for w in spl if w.lower() not in stopwords]
            tagged = nltk.pos_tag([word for word in filtered_sentence if word])
            for i in tagged:
                # print(i)
                if len(i[0]) != 0 or len(i[0]) != 1 or len(i[0]) != 2:

                    if i[1] == 'IN' or i[1] == 'DT' or i[1] == 'CD' or i[1] == 'CC' or i[1] == 'EX' or i[1] == 'MD' or \
                            i[
                                1] == 'WDT' or i[1] == 'WP' or i[1] == 'UH' or i[1] == 'TO' or i[1] == 'RP' or i[
                        1] == 'PDT' or i[
                        1] == 'PRP' or i[1] == 'PRP$' or i[0] == 'co' or i[1] == 'RB' or i[1] == 'RBR' or i[
                        1] == 'JJ' or i[1] == 'RBS' or i[0] == 'said' or i[0] == 'mr' or i[0] == 'states':
                        # print(i[0])
                        continue
                    else:
                        # print(i[0])
                        # print(type(i[0]))
                        total0 += 1
                        word_count0.update([i[0]])
                        # print(word_count)
            class_0 += 1
        elif num < 0.93:
            text = content_test_fake[linenum]
            text = text.encode("ascii", "ignore").decode()
            spl = text.split()
            filtered_sentence = [w.lower().rstrip(punctuation) for w in spl if w.lower() not in stopwords]
            tagged = nltk.pos_tag([word for word in filtered_sentence if word])
            for i in tagged:
                # print(i)
                if len(i[0]) != 0 or len(i[0]) != 1 or len(i[0]) != 2:

                    if i[1] == 'IN' or i[1] == 'DT' or i[1] == 'CD' or i[1] == 'CC' or i[1] == 'EX' or i[1] == 'MD' or \
                            i[
                                1] == 'WDT' or i[1] == 'WP' or i[1] == 'UH' or i[1] == 'TO' or i[1] == 'RP' or i[
                        1] == 'PDT' or i[
                        1] == 'PRP' or i[1] == 'PRP$' or i[0] == 'co' or i[1] == 'RB' or i[1] == 'RBR' or i[
                        1] == 'JJ' or i[1] == 'RBS' or i[0] == 'said' or i[0] == 'mr' or i[0] == 'states':
                        # print(i[0])
                        continue
                    else:
                        # print(i[0])
                        # print(type(i[0]))
                        total1 += 1
                        word_count1.update([i[0]])
                        # print(word_count)
            class_1 +=1
        elif num < 0.98:
            text = content_test_fake[linenum]
            text = text.encode("ascii", "ignore").decode()
            spl = text.split()
            filtered_sentence = [w.lower().rstrip(punctuation) for w in spl if w.lower() not in stopwords]
            tagged = nltk.pos_tag([word for word in filtered_sentence if word])
            for i in tagged:
                # print(i)
                if len(i[0]) != 0 or len(i[0]) != 1 or len(i[0]) != 2:

                    if i[1] == 'IN' or i[1] == 'DT' or i[1] == 'CD' or i[1] == 'CC' or i[1] == 'EX' or i[1] == 'MD' or \
                            i[
                                1] == 'WDT' or i[1] == 'WP' or i[1] == 'UH' or i[1] == 'TO' or i[1] == 'RP' or i[
                        1] == 'PDT' or i[
                        1] == 'PRP' or i[1] == 'PRP$' or i[0] == 'co' or i[1] == 'RB' or i[1] == 'RBR' or i[
                        1] == 'JJ' or i[1] == 'RBS' or i[0] == 'said' or i[0] == 'mr' or i[0] == 'states':
                        # print(i[0])
                        continue
                    else:
                        # print(i[0])
                        # print(type(i[0]))
                        total2 += 1
                        word_count2.update([i[0]])
                        # print(word_count)
            class_2 +=1
        elif num < 0.995:
            text = content_test_fake[linenum]
            text = text.encode("ascii", "ignore").decode()
            spl = text.split()
            filtered_sentence = [w.lower().rstrip(punctuation) for w in spl if w.lower() not in stopwords]
            tagged = nltk.pos_tag([word for word in filtered_sentence if word])
            for i in tagged:
                # print(i)
                if len(i[0]) != 0 or len(i[0]) != 1 or len(i[0]) != 2:

                    if i[1] == 'IN' or i[1] == 'DT' or i[1] == 'CD' or i[1] == 'CC' or i[1] == 'EX' or i[1] == 'MD' or \
                            i[
                                1] == 'WDT' or i[1] == 'WP' or i[1] == 'UH' or i[1] == 'TO' or i[1] == 'RP' or i[
                        1] == 'PDT' or i[
                        1] == 'PRP' or i[1] == 'PRP$' or i[0] == 'co' or i[1] == 'RB' or i[1] == 'RBR' or i[
                        1] == 'JJ' or i[1] == 'RBS' or i[0] == 'said' or i[0] == 'mr' or i[0] == 'states':
                        # print(i[0])
                        continue
                    else:
                        # print(i[0])
                        # print(type(i[0]))
                        total3 += 1
                        word_count3.update([i[0]])
                        # print(word_count)
            class_3 +=1
        elif num < 0.998:
            text = content_test_fake[linenum]
            text = text.encode("ascii", "ignore").decode()
            spl = text.split()
            filtered_sentence = [w.lower().rstrip(punctuation) for w in spl if w.lower() not in stopwords]
            tagged = nltk.pos_tag([word for word in filtered_sentence if word])
            for i in tagged:
                # print(i)
                if len(i[0]) != 0 or len(i[0]) != 1 or len(i[0]) != 2:

                    if i[1] == 'IN' or i[1] == 'DT' or i[1] == 'CD' or i[1] == 'CC' or i[1] == 'EX' or i[1] == 'MD' or \
                            i[
                                1] == 'WDT' or i[1] == 'WP' or i[1] == 'UH' or i[1] == 'TO' or i[1] == 'RP' or i[
                        1] == 'PDT' or i[
                        1] == 'PRP' or i[1] == 'PRP$' or i[0] == 'co' or i[1] == 'RB' or i[1] == 'RBR' or i[
                        1] == 'JJ' or i[1] == 'RBS' or i[0] == 'said' or i[0] == 'mr' or i[0] == 'states':
                        # print(i[0])
                        continue
                    else:
                        # print(i[0])
                        # print(type(i[0]))
                        total4 += 1
                        word_count4.update([i[0]])
                        # print(word_count)
            class_4 += 1
        elif num > 0.998:
            text = content_test_fake[linenum]
            text = text.encode("ascii", "ignore").decode()
            spl = text.split()
            filtered_sentence = [w.lower().rstrip(punctuation) for w in spl if w.lower() not in stopwords]
            tagged = nltk.pos_tag([word for word in filtered_sentence if word])
            for i in tagged:
                # print(i)
                if len(i[0]) != 0 or len(i[0]) != 1 or len(i[0]) != 2:

                    if i[1] == 'IN' or i[1] == 'DT' or i[1] == 'CD' or i[1] == 'CC' or i[1] == 'EX' or i[1] == 'MD' or \
                            i[
                                1] == 'WDT' or i[1] == 'WP' or i[1] == 'UH' or i[1] == 'TO' or i[1] == 'RP' or i[
                        1] == 'PDT' or i[
                        1] == 'PRP' or i[1] == 'PRP$' or i[0] == 'co' or i[1] == 'RB' or i[1] == 'RBR' or i[
                        1] == 'JJ' or i[1] == 'RBS' or i[0] == 'said' or i[0] == 'mr' or i[0] == 'states':
                        # print(i[0])
                        continue
                    else:
                        # print(i[0])
                        # print(type(i[0]))
                        total5 += 1
                        word_count5.update([i[0]])
                        # print(word_count)
            class_5 +=1
        else:
            print("INVALID")
        linenum+=1

    print("Class 0: ", class_0)
    print("Class 1: ", class_1)
    print("Class 2: ", class_2)
    print("Class 3: ", class_3)
    print("Class 4: ", class_4)
    print("Class 5: ", class_5)
    print("Total positive: ", class_0)
    print("Total negative: ", class_1+class_2+class_3+class_4+class_5)

    print("*** class 0 ****")
    print("Total Words: ",total0)
    print(word_count0.most_common(20))
    print("*** class 1 ****")
    print("Total Words: ", total1)
    print(word_count1.most_common(20))
    print("*** class 2 ****")
    print("Total Words: ", total2)
    print(word_count2.most_common(20))
    print("*** class 3 ****")
    print("Total Words: ", total3)
    print(word_count3.most_common(20))
    print("*** class 4 ****")
    print("Total Words: ", total4)
    print(word_count4.most_common(20))
    print("*** class 5 ****")
    print("Total Words: ", total5)
    print(word_count5.most_common(20))

reader.close()
