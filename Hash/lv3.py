from collections import defaultdict

genres = ['classic', 'pop', 'classic', 'classic', 'pop','jazz']
plays = [5000, 600, 150, 800, 2500, 50000]

answer =[]
dicGenres = defaultdict(list)
total = defaultdict(lambda : 0)

for g, p in zip(genres, plays):
    total[g] += p
print(total)

sortedTotal = sorted(total.items(), key=lambda x: x[1], reverse=True)
print(sortedTotal)

for i in range(len(genres)):
    dicGenres[hash(genres[i])].append(plays[i])
print(dicGenres)

for k in dicGenres:
    dicGenres[k].sort(reverse=True)
print(dicGenres)

print(len(dicGenres[hash(sortedTotal[1][0])]))

for m in range(len(sortedTotal)):
    idx = plays.index(dicGenres[hash(sortedTotal[m][0])][0])
    answer.append(idx)
    plays[idx] = -1
    if len(dicGenres[hash(sortedTotal[m][0])]) > 1:
        answer.append(plays.index(dicGenres[hash(sortedTotal[m][0])][1]))

print(answer)

