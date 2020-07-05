n = int(input())

k = n % 10

if k == 2 or k == 4 or k == 5 or k == 7 or k == 9:
  print("hon")
elif k == 0 or k == 1 or k == 6 or k == 8:
  print("pon")
else:
  print("bon")

