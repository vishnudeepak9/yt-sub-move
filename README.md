# YouTube Subscribed Channel to the new account with Python

I have used an old youtube account for a few years and collected a lot of informative channels and subscribed to them, all my fav channels & youtube creators, and a lot of useful Channels in my old account. Recently, I Urge to create a new account for a fresh start & I wanted to have my years of collection (subscribed channels). But there is no perfect way to import Channels to the new account.

So, I thought why don't make our hands dirty? So I discussed this with my senior who is very good at Python Programming, as we have different ways to implement the same thing. So we thought to put something simpler and minimalistic, a program that will be useful to someone trying to do the same thing. So we give it a shot.

## Step-1
Download your old account youtude data by, logging into old account and go to <a href="https://takeout.google.com/takeout/custom/youtube?hl=en&continue=https://myaccount.google.com/dashboard" target="_blank">here</a> and download your data.

Extract your TAKEOUT zip file 
Open Terminal or any IDE
Next.
```
git clone https://github.com/vishnudeepak9/yt-sub-move
mv yt-sub-move
```
Now Move or Copy your ```Takeout/YouTube and YouTube Music/subscriptions/subscriptions.csv``` to ```yt-sub-move```

## Step-2
Log out of your YouTube old account.
Login to New youtube (Preferred Chrome).
Open a single tab with a new youtube account
Now run the ```youtube.py```
```
python3 youtube.py
```

