import csv
import webbrowser
import time
with open("subscriptions.csv",'r') as file:
    csvreader=csv.reader(file)
    c=0
    for i in csvreader:
        c+=1
            #print(i[1])
        webbrowser.open_new(i[1])
        if c%10==0:
            time.sleep(60)