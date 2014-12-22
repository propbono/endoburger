import bs4


__author__ = 'propbono'

from bs4 import BeautifulSoup
import requests

ENDOMONDO_USER = ''
ENDMONDO_PASSWORD = ''
GOOGLE_USER = ''
GOOGLE_PASSWORD = ''

#1 get endomondo site
def get_burgers_from_html(endo_page):
    html = BeautifulSoup(endo_page.content)
    burned_burgers = html.find("li", class_ = "burgers").find("span",
                                                              class_ = "value")
    return burned_burgers.string

def get_endomondo_site(endo_user, endo_password):
    with requests.Session() as session:
        endomondo_login_url = "https://www.endomondo.com/login"
        endomondo_home_url = "https://www.endomondo.com/home"
        user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0"
        session.get(endomondo_login_url)

        session.headers.update({
            "User-Agent": user_agent,
            "Referer" : endomondo_home_url
        })

        session.cookies.update({
            "EndomondoApplication_USER" : endo_user,
            "EndomondoApplication_AUTH" : endo_password
        })

        session.post(endomondo_login_url)

        endo_page = session.get(endomondo_home_url)

        burned_burgers = get_burgers_from_html(endo_page)

        return burned_burgers

#2 parse site adn return burned burgers
#3 create google client
#4 get proper spreadsheet
#5 update cells
#6 return curent values

if ENDOMONDO_USER and ENDMONDO_PASSWORD:
    get_endomondo_site(ENDOMONDO_USER, ENDMONDO_PASSWORD)
else:
    ENDOMONDO_USER = input("Endomondo login: ")
    ENDMONDO_PASSWORD = input("Endomondo password: ")
    try:
        get_endomondo_site(ENDOMONDO_USER, ENDMONDO_PASSWORD)
    except:
        "Login or password incorrect"
