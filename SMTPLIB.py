from email import message
from logging import exception
from operator import truediv
import requests
import smtplib
from apscheduler.schedulers.blocking import BlockingScheduler
from hashlib import new

sender = 'data_scraping@coneasorin.ro'
subject = 'Pretul a scazut la: '
to_addr_list = ['comorschi_tudor@inbox.ru']
cc_addr_list = ['']

def sendemail(sender,message, subject,to_addr_list, cc_addr_list=[]):
    try:
        smtpserver='mail.x-it.ro:26'

        header = 'From: %s\n' % sender
        header += 'To: %s\n' % ','.join(to_addr_list)
        header += 'Cc: %s\n' % ','.join(cc_addr_list)
        header += 'Subject: %s\n\n' % subject
        message = header + message

        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(sender, "stiinte217_2022")
        problems = server.sendemail(sender, to_addr_list, message)
        server.quit()
        return True
    except:
        return False


# def data_scraping():
#     req=requests.get("https://www.emag.ro/telefon-mobil-apple-iphone-14-pro-max-128gb-5g-deep-purple-mq9t3rx-a/pd/DXDY4LMBM/?cmpid=99160&gclid=CjwKCAjw7p6aBhBiEiwA83fGutQEzd8jTFRrgGNgq-64rJSekVI_-HBUv2ljRnybUWvX7Ny_Rzh68hoClScQAvD_BwE")
#     soup=BeautifulSoup(req.text,"html.parser")
#     price=soup.find('p', attrs={'class': 'product-new-price'}).text
#     new_price=price[0:5]
#     new_price=new_price.replace(".","")
#     new_price=int(new_price)
#     pret_referinta = 7079
#     if ( new_price<pret_referinta)
#         sendemail(sender, "Pretul a scazut la: ", subject, to_addr_list, cc_addr_list)
#         print("Pretul a scazut la: ")


#data_scraping()
sendemail(sender,, subject,to_addr_list, cc_addr_list=[]):