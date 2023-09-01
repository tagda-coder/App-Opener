#!/usr/bin/env python 
import os 
os.system("clear")
""" 
Hey Guys Welcome Back to Tagda Coder Script. 
Here We have create Very Amazing Script which will help you to open Your Desire Apps in single click...
           Requirements For This Tool 
           -------------------------
           1.Python Programming | Channel Par Basic Upload hai 
           2.And Practice 
           -------------------------

If You also Want to Learn Coding And Making Script like me .

Then Go and  Must Visit our Channel {TAGDA CODER}
On YouTube.

This Tool Is Created By Me :- Mandeep Malakar
"""

#=====================  ================
# Code Start From Here | Don't Be Copy Paster
#=====================  ================

# Be a Unique 
# Banner And Interface Of Tool .
print("""\033[1m\033[41m         \033[42m        \033[42m           \033[45m      \033[46m           \033[0m""")
print("""\033[32m\033[1m  
        ╲    ╱    \033[35m  \033[31mYouTube   :\033[37m Tagda Coder
        ╱▔▔▔▔╲    \033[33m╿ \033[31mTool Name : \033[37mApp-Opener
       \033[32m┃ \033[31m▇  \033[31m▇ \033[32m┃   \033[31m│ Country   : \033[37mIndia 
     ╭╮┣━━━━━━┫╭╮ \033[35m╽ \033[31mVersion   : \033[37m1.0         
     ┃┃┃\033[33mCoders┃┃┃   \033[31mAuthor    : \033[37mMandeep
     ╰╯┃\033[31mLegion┃╰╯\033[32m
       ╰┓┏━━┓┏╯    \033[33m〄 \033[32mSecurity Purpose \033[33m〄
        ╰╯  ╰╯        

\033[1m\033[41m         \033[42m        \033[42m           \033[45m      \033[46m            \033[0m            
""")


# Apps thats  are to be Open 
# Option of Apps '''

print("\033[1m\033[36m{\033[31m01\033[36m}\033[33m────\033[37m[ \033[32mWhatsApp ")
os.system("sleep 1")
print("\033[36m{\033[31m02\033[36m}\033[33m────\033[37m[ \033[34mFacebook")
os.system("sleep 1")
print("\033[36m{\033[31m03\033[36m}\033[33m────\033[37m[ \033[38;5;209mInstaGram")
os.system("sleep 1")
print("\033[36m{\033[31m04\033[36m}\033[33m────\033[37m[ \033[31mYouTube")
os.system("sleep 1")
print("\033[36m{\033[31m05\033[36m}\033[33m────\033[37m[ \033[32mGOOGLE")
os.system("sleep 1")
print("\033[36m{\033[31m06\033[36m}\033[33m────\033[37m[ \033[33m\033[31mCHR\033[31mOME")
os.system("sleep 1")
print("\033[36m{\033[31m07\033[36m}\033[33m────\033[37m[ \033[33m\033[36mContact Me")
os.system("sleep 1")
print("\033[36m{\033[31m08\033[36m}\033[33m────\033[37m[ \033[33m\033[31mSUBSCRIBE⭕")
os.system("sleep 1")
print("\033[36m{\033[31m09\033[36m}\033[33m────\033[37m[ \033[33m\033[33mPlayStore")
print()
choice = input("\033[1m\033[37m }---\033[33mSelect Any One\n         \033[36mThat You Want to Open : \033[36m\033[4m")

print("\033[0m")


# Condition Of the User 
# Whatsapp

if "1" in choice or "01" in choice or "WhatsApp" in choice or "whatsapp" in choice :

    os.system("am start --user 0 -n com.whatsapp/.HomeActivity")
    os.system("python App-Opener.py")

#FaceBook
elif "2" in choice or "02" in choice or "FaceBook" in choice or "facebook" in choice :
    os.system("am start --user 0 -n com.facebook.katana/.activity.FbMainTabActivity")
    os.system("python App-Opener.py")

#InstaGram
elif "3" in choice or "03" in choice or "Instagram" in choice or "InstaGram" in choice :

    os.system("am start --user 0 -n com.instagram.android/com.instagram.mainactivity.MainActivity")
    os.system("python App-Opener.py")

#YouTube

elif "4" in choice or "04" in choice or "YouTube" in choice or "Youtube" in choice or "youtube" in choice :
    os.system("am start --user 0 -n com.google.android.youtube/com.google.android.apps.youtube.app.watchwhile.WatchWhileActivity")
    os.system("python App-Opener.py")

#Google 

elif "5" in choice or "05" in choice or "Google" in choice or "google" in choice :
    os.system("termux-open-url https://www.google.com")
    os.system("python App-Opener.py")
#Chrome 
elif "6" in choice or "06" in choice or "Chrome" in choice or "chrome" in choice :
    os.system("termux-open-url https://www.google.com/search?q=tagda+coder&oq=tagda+coder+&aqs=chrome..69i57j69i61l3.3569j0j7&client=ms-android-oppo-rvo3&sourceid=chrome-mobile&ie=UTF-8")
    os.system("python App-Opener.py")
#Contacts

elif "07" in choice or "7" in choice or "contact" in choice or "Contacts" in choice or "contacts" in choice :
    print("\033[1m\033[31mAlert ! ")
    print("\033[33mIf you are not able to call Must install Termux-Api From Playstore ")
    os.system("sleep 3")
    os.system("termux-telephony-call +919939411504")
    os.system("python App-Opener.py")
elif "08" in choice or "8" in choice or "Subscribe" in choice or "subscribe" in choice or "Channel" in choice :
    os.system("termux-open-url https://youtube.com/channel/UCGouo2InkKtaIiZMrPTykgA")
    os.system("sleep 100")
    os.system("termux-open-url https://youtube.com/channel/UCNzoTEPI72NAsm9xpDxce5Q")
    os.system("python App-Opener.py")
elif "09" in choice or "9" in choice or "playstore" in choice or "Playstore" in choice :
    os.system("termux-open-url https://play.google.com/store/apps/details?id=com.termux.api")
    os.system("python App-Opener.py")

else :
    print("\033[31m\033[1mInvalid \033[33mCommand ")
    os.system("python App-Opener.py")


# You Can Use this Code to your script or you want to Enhance The Features of This Tool ..
# But Don't Forget to Give Credits .
# Thank You



