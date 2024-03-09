# Link of the question if u r interesting: https://zerojudge.tw/ShowProblem?problemid=c292
# getting inputs
n = int(input())
position =int(input())
p = int(position)
l = []
for i in range(n):
  l.append([int(i) for i in input().split(' ')])

# some thing for me to be lazy while testing
# l = [[3, 4, 2, 1, 4], [4, 2, 3, 8, 9], [2, 1, 9, 5, 6], [4, 2, 3, 7, 8], [1, 2, 6, 4, 3]] 

move = [[0, -1], [-1, 0], [0, 1], [1, 0]] #yes, position:)

lastmove = [[[n-1 for i in range(n-1)], [n-i-2 for i in range(n-1)]], 
            [[n-i-2 for i in range(n-1)], [0 for i in range(n-1)]], 
            [[0 for i in range(n-1)], [i+1 for i in range(n-1)]],
            [[i+1 for i in range(n-1)], [n-1 for i in range(n-1)]]] #x and y for last row of output, u definitely can understand:))))

x, y = n//2, n//2 # start from the middle
out = [] # list that save the answer
out.append(l[x][y])

# walk through list l according to the rule except the last row and append it to list out
for i in range(1, n):
  for j in range(i):
    x += move[position%4][0]
    y += move[position%4][1]
    out.append(l[x][y])
  position += 1
  for j in range(i):
    x += move[position%4][0]
    y += move[position%4][1]
    out.append(l[x][y])
  position += 1

# add the last row to the list out
lastmove = lastmove[p]
x = lastmove[0]
y = lastmove[1]
for i in range(n-1):
  out.append(l[x[i]][y[i]])

# print the answer shee shee
for i in out:
  print(i, end = '')
 
# Yeah I so happy because Replit finally unbanned my account:)))))
