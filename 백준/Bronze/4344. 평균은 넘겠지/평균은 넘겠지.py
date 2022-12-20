c=int(input())
for i in range(c): #(1)
    score=list(map(int,input().split()))
    student=0
    for j in score[1:]: #(2)
        avg=sum(score[1:])/score[0]
        if j>avg:
            student+=1
    rate=student/score[0]*100
    print('{0:0.3f}%'.format(rate))