def multiplication_table(n):
  for i in range(1, 11):
    print(n, "x", i, "=", n*i)

num = input("Van welk getal wilt u de tafel zien? ")
multiplication_table(int(num))
