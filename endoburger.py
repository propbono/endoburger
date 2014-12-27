import bs4
import time


__author__ = 'propbono'

from bs4 import BeautifulSoup
import requests
import gspread

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

        #2 parse site adn return burned burgers
        endo_page = session.get(endomondo_home_url)

        burned_burgers = get_burgers_from_html(endo_page)

        return burned_burgers


#3 create google client
def _get_number_of_burned_burgers(endmondo_password, endomondo_user):
    burgers_to_update = ""
    if endomondo_user and endmondo_password:
        burgers_to_update = get_endomondo_site(endomondo_user,
                                               endmondo_password)
    else:
        endomondo_user = input("Endomondo login: ")
        endmondo_password = input("Endomondo password: ")
        try:
            burgers_to_update = get_endomondo_site(endomondo_user,
                                                   endmondo_password)
        except:
            "Login or password incorrect"
    return burgers_to_update


def update_number_of_burgers_in_spreadsheet(user, password, endomondo_user,
                                            endmondo_password):
    start_time_endomondo = time.time()
    burgers_to_update = _get_number_of_burned_burgers(endmondo_password,
                                                      endomondo_user)
    end_time_endomondo = time.time()

    start_time_google = time.time()

    spreadsheet_name = "Hamburgersy"
    client = gspread.login(user,password)

    spreadsheet = client.open(spreadsheet_name).sheet1

    current_burgers_count = spreadsheet.acell("B5").value
    burgers_to_use = spreadsheet.acell("D5").value
    burgers_to_eat = spreadsheet.acell("G7").value
    kebabs_to_eat =spreadsheet.acell("H7").value
    pizzas_to_eat = spreadsheet.acell("I7").value



    end_time_endomondo = time.time()

    spreadsheet.update_acell("B5", burgers_to_update)
    end_time_google = time.time()

    print("Burgers burned: ", burgers_to_update)
    print("Endomondo time: ", (end_time_endomondo-start_time_endomondo))
    print("Google time: ", (end_time_google-start_time_google))

#4 get proper spreadsheet
#5 update cells
#6 return curent values

update_number_of_burgers_in_spreadsheet(GOOGLE_USER, GOOGLE_PASSWORD,
                                        ENDOMONDO_USER, ENDMONDO_PASSWORD)
