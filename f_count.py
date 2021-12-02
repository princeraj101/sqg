import os

f = open("hypothesis_t5-base-qg-hl.txt","r")
f1 = open("out_file.txt","w")
count = 0
spl_word = "<sep>"
for line in f:
    if spl_word in line:
        res = line.partition(spl_word)[0]
        f1.write(res + os.linesep)
        print(res)
        count += 1
print(count)
