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
        """
        if c%10==0:
            time.sleep(60)
        #this code is used to execute every 10 subscriptions at a time
        """

        #we can modify this to one subscription and wait till 10 seconds and then continue
        time.sleep(10)
        