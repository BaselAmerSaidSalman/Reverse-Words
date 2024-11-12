import time
sentence = input("Enter a sentence: ").split(" ")
while sentence == "":
  print("Sorry, you didn't enter anything!")
  sentence = input("Please enter a sentence: ").split(" ")
print(" ".join(sentence[-1::-1]))
time.sleep(2)
  

  
