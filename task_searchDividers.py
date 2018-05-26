import sys

number = sys.argv[1]
k = []

def divide(n):
  if n in k:
    return
  for i in range(2, 20):
    if n%i == 0:
      divide(n/i)
      if i not in k:
        k.append(i)
      if (int(n/i)) not in k:
        k.append(int(n/i))
  return

divide(int(number))
k.append(int(number))

print (k)