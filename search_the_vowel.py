word = input().lower()
dic = {
    "a" : 0,
    "e" : 0,
    "i" : 0,
    "o" : 0,
    "u" : 0,
}

for w in word:
    if w in 'aeiou':
        dic[w] += 1
        
print(dic)