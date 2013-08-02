summarize.py
============

A python script for summarizing articles using nltk.

Requires:

    python2.7
    nltk
    bs4 (only for opening urls)
    requests (only for opening urls)
  
Usage:

    git clone https://github.com/Rotten194/summarize.py.git
    cd summarize.py
    ./summarize.py http://www.washingtonpost.com/blogs/the-switch/wp/2013/08/01/how-vermont-could-save-the-nation-from-patent-trolls/

Example:

    $ ./summarize.py http://www.theverge.com/2013/8/1/4580718/fbi-can-remotely-activate-android-and-laptop-microphones-reports-wsj
    FBI can remotely activate Android and laptop microphones, reports WSJ | The Verge
    
    The Wall Street Journal reports that the FBI can already remotely activate those microphones to record conversations.
    
    Remotely activated cell phone bugs predate iOS and Android
    
    What's new, according to several former anonymous officials, is a dedicated FBI group which regularly hacks into computers, using both custom and off-the-shelf surveillance software which it buys from private companies.
    
    " While that source also claims the FBI takes care to make sure that only "relevant data" gets collected, it's still a little troubling to know that such a thing is easily possible and regularly done.
