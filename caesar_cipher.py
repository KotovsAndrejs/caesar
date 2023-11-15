a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def e(text, rotation): #Функция отвечает за  режим шифрования
  text = text.upper()
  newtext = ""
  for c in text: #Цикл перебирает значения в исходном тексте
    if (a.find(c) == -1): #Цикл находит
      newtext += c
    else:
      newtext += (a[(a.find(c) + rotation) % len(a)])
  return newtext

def d(text, rotation): #Функция отвечает за  режим дешифрования
  text = text.upper()
  newtext= ""
  for c in text: #Цикл перебирает значения в исходном тексте
    if (a.find(c) == -1):
      newtext += c
    else:
      newtext += (a[(a.find(c) - rotation) % len(a)])
  return newtext

w = """
1. Encrypt text
2. Decrypt text
3. Bruteforce all rotations
Choose mode: """
mode = int(input(w))

if mode == 1: #При выборе, код запросит текст, ротацию и выведет зашифрованный текст
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Encrypted: " + e(text, rotation))
elif mode == 2: #При выборе, код запросит текст, ротацию и выведет дешифрованный текст
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Decrypted: " + d(text, rotation))
elif mode == 3: #шутка
  print("Bruteforcing...")
  print("But I don't know how to do it, sorry ¯\_(ツ)_/¯")
