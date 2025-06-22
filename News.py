import random
first = ["Sharukh Khan","Virat Kohli","Salman Khan","A group of moneys","Rohit Sharma","Narendra Modi","M S Dhoni","Rahul Gandhi","An Auto Rickshaw Driver"]
middle = ["eat Vadapav","is dancing","crying for toy","declares war","fight with villen","sit","is playing cricket","watch news","read newspaper","win IPL"]
last = ["at Mumbai Street.","at Pakistan.","at Surat.","on Cricket Ground.","on Tree.","in local Train.","in his house.","at Tajmahal.","after 18 year."]
while True:
   firstchoice = random.choice(first)
   middlechoice = random.choice(middle)
   lastchoice = random.choice(last)
   print(f"BREAKING NEWS : {firstchoice} {middlechoice} {lastchoice} \n")
   x = input("Do you want to genrate headline again..? (Y/n) : ").upper()
   if x == "Y" or x == "":
      continue
   elif x == "N":
      break
   else:
      print("Invalid Choice..!")
      break
print ("\nThank You for using Fake News Headline Generator. Have a Fun Day.")
   