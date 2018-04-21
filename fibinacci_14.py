
def fabinacci(n):
   if n == 1:
      return 1
   elif n == 2:
      return 1
   return fabinacci(n -1) + fabinacci(n-2)

print fabinacci(6)
