# Password Generator
#================================
from random import *
#================================
while True:
  Eingabe = input("Wieviele Stellen soll das Passwort haben: ")
  try:
      int_Eingabe = int(Eingabe)
      if int_Eingabe < 12 or int_Eingabe > 32:
          print('Alter! Nur Zahlen zwischen 12 und 32! OK?!')
          continue
      break
  except ValueError:
      print("Haha, witzig, das ist keine Zahl!")
  else:
    print("Höma, red ich chinesisch? 你这笨蛋！Eine Zahl zwischen 12 und 32, verdammt! Los, nochma!")

tmp_passwd = []
i = 0

for i in range(0, int_Eingabe):
  element = choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-_.:,;#+*!\§$%&/()=?~ßöäüÖÄÜ')
  tmp_passwd.append(element)
  password = "".join(tmp_passwd)  
  i = i + 1  
print("\n", password, "\n")
