from time import sleep
from config import SILENCE
from excel_data import models_price

from scrapping.naver_login import naver_login, set_cookies

# models_price = get_price_from_excel(EXCEL)
login = naver_login(SILENCE)
driver = login['driver']
cookies = login['cookies']
req_session = set_cookies(cookies)
print(req_session)
while(True):
    print(1)
    sleep(0.1)