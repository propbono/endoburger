# Endoburger

Simple python script for getting specific information from endomondo account
and put this information to google spreadsheet.

I use this for getting number of burned burgers from my endomondo account 
and putting this to google speradsheet where I have my own statistics about 
burned calories and allowances to eat unhealthy food :)

# Installation

To work it properly you must clone it to your harddrive and then add file 
credentials.py which should looks like this:

```
ENDOMONDO_USER = '' # EndomondoApplication_USER from coockies it could be 
normal user name to endomondo account
ENDMONDO_PASSWORD = '' # EndomondoApplication_AUTH from coockies it must be 
                       # the same value like in a coockie
GOOGLE_USER = '' # Normal user name for google account
GOOGLE_PASSWORD = '' # Normal password for google account   -
```

You don't have to add this file, but if You don't add it You will have to 
write your credentials to both accounts when programm will be runnining.

# Further improvements

In the future I'm planning to put this script into online web page, and grab
some more information from endomondo site. But this will be hard unless 
Endomondo team realese a free API.

In the meantime I will polish this version off app and I will prepare this 
for future improvements. 