N = int(input())
card = [i for i in range(1, N+1)]
discarded_card = []

while len(card) != 1:
    discarded_card.append(card.pop(0)) #버리기
    card.append(card.pop(0)) #뒤로 옮기기

for i in discarded_card:
    print(i, end = ' ')
print(card[0])