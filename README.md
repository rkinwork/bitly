# Bitly url shorterer

This command-line utility that may or to turn http urls to bitlinks or get statistics of bitlink clicks
This command-line utility shorten URLs using [bitly](https://bitly.com) service. Also you can get statistics of clicks on your bitlinkls
via same interface

### How to install
Python3 should be already installed. This script tested and run on `Python==3.7`
 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```console
foo@bar:~$ pip install -r requirements.txt
```

Before run script 

1) Get API Token key according bitly [documentation](https://dev.bitly.com/get_started.html)
1) Assign token value to environment variable `export BITLY_TOKEN=YOURSECRETTOKEN`
or create `.env` file in the root folder according [python-dotenv](https://pypi.org/project/python-dotenv/#usages) documentation


### How to use

#### How to shorten URL
```console
foo@bar:~$ python3 main.py http://google.com
http://bit.ly/2IGA2RF

foo@bar:~$ echo 'https://devman.org' | python3 main.py
http://bit.ly/2TKc5x4
```

Caveat: script shortens only the URLs with specified protocol

These will shorten: `https://devman.org` `http://google.com`

These __will not__: `devman.org` `google.com`

#### How to get clicks statistics

Pass bitlink to the script like you did in shorten URL step

```console
foo@bar:~$ python3 main.py https://bit.ly/2IGA2RF
56

foo@bar:~$ python3 main.py bit.ly/2IGA2RF
56

foo@bar:~$ echo 'bit.ly/2IGA2RF' | python3.6 main.py
56
```


### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).