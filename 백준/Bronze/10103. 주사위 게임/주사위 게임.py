N=int(input())
score0=100
score1=100
for i in range(N):
  a=input().split()
  player0_score = int(a[0])
  player1_score = int(a[1])

  if player0_score > player1_score:
    score1 -= player0_score
  elif player0_score < player1_score:
    score0 -= player1_score

print(score0, score1)