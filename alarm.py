import time
import webbrowser

total_break = 3
count = 0
while count < total_break:
    what = input("should i?")
    print("the program started "+ time.ctime())
    time.sleep(10)
    webbrowser.open("https://web.facebook.com")
    count +=1
