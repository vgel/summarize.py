summarize.py
============

A python script for summarizing articles using nltk.

## Requires:
* python2.7 / python 3
* nltk (if using Python 3, see note below)
* nltk `stopwords` corpora (`python -c 'import nltk; nltk.download("stopwords")'`) 
* bs4 (only for opening urls)
* requests (only for opening urls)

## Usage:

    git clone https://github.com/Rotten194/summarize.py.git
    cd summarize.py/summarize
    ./summarize.py http://www.washingtonpost.com/blogs/the-switch/wp/2013/08/01/how-vermont-could-save-the-nation-from-patent-trolls/

Usage from code:

    # sudo python setup.py install
    # then
    import summarize
    summarize.summarize_text(large_text)

## Python 3 Support Notes:

To use NLTK with Python 3 currently, you must install the NLTK 3.0 alpha packages available at [nltk.org](http://www.nltk.org/nltk3-alpha). All other libraries required by summarize.py have Python 3 versions.


## Example:

    $ python3 summarize.py "http://www.theverge.com/2013/8/1/4580718/fbi-can-remotely-activate-android-and-laptop-microphones-reports-wsj"
    FBI can remotely activate Android and laptop microphones, reports WSJ | The Verge - http://www.theverge.com/2013/8/1/4580718/fbi-can-remotely-activate-android-and-laptop-microphones-reports-wsj

    Remotely activated cell phone bugs predate iOS and Android
    What's new, according to several former anonymous officials, is a dedicated FBI group which regularly hacks into computers, using both custom and off-the-shelf surveillance software which it buys from private companies.
    While that source also claims the FBI takes care to make sure that only "relevant data" gets collected, it's still a little troubling to know that such a thing is easily possible and regularly done.
