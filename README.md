# True random numbers password generator

A short python script that connects to RANDOM.ORG API (through `requests` library) and gets true random numbers which are then
used to pick a set of words to create a new password.

If you've changed the `words.txt` file, use `update_max()` from `hlpr_scrpts.py`.

First password created by this script:
*androdioecious bronchocephalitis disabuses hearken marchite spasmotoxin*

`words.txt` file is from: https://github.com/dwyl/english-words
`requests`: http://docs.python-requests.org/en/latest/
