sentence=("Sahad is a handsome boy")
word=sentence.split()
count={}
for i in word:
    count[i] = count.get(i, 0) + 1
print(count)