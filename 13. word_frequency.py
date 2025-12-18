f=open("sample.txt","r")
text=f.read()
f.close()
text=text.lower()
words=text.split()
freq={}

for i in words:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1

print("Word Frequency:")
for i in freq:
    print(i, ":", freq[i])