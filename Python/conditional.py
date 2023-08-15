#if (5>4):
 #   print(True)
#else:
 #   print(False)
spamwords=['buynow','subscribe','click this']
email="this is you should buynow"
if ("spamwords "in email):
    spam=True
elif("subscribe" in email):
    spam=True
else:
    spam=False
    
print("spam is",spam)