import time
import winsound
s=12
for i in range(s):
    if s - i == 1:
        print(str(s - i) + " second remain")
        winsound.PlaySound("beep",winsound.SND_FILENAME)
    else:
        print(str(s - i) + " seconds remain")
        winsound.PlaySound("beep",winsound.SND_FILENAME)
print("Timer is up")
winsound.PlaySound("alarm",winsound.SND_FILENAME)