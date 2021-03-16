import pandas as pd

train = pd.read_csv("E:\\RumorDetection\\train.csv",encoding='latin1')

# print(train.shape)
# print(train[train["label"]==1].shape)
# print(train[train["label"]==0].shape)

count = 0
length = 0
for line in train["title"]:
    length+=len(line)
    count+=1

print(length/count)

test = pd.read_csv("E:\\RumorDetection\\test.csv",encoding='latin1')

# print(test.shape)
# print(test[test["label"]==1].shape)
# print(test[test["label"]==0].shape)

count = 0
length = 0
for line in test["title"]:
    length+=len(line)
    count+=1

print(length/count)