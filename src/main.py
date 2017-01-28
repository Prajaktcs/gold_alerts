"""
Module to fetch gold prices and send email to a configured list of sources
"""
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
import requests
import smtplib

import constants


def get_bid_price() -> float:
    """
    Method to fetch golds value today
    :return float: todays gold value
    """
    response = requests.get('http://www.sify.com/finance/gold_rates/')
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.select('#mbldelhigold')[0].find_all('a')[1].text


def send_email(gold_price: float) -> None:
    """
    Send email using my hotmail ADDRESS
    :param gold_price: Todays gold price
    """
    server = smtplib.SMTP('smtp.live.com', 587)
    server.starttls()
    server.login(constants.my_email, constants.my_password)
    msg = MIMEText('Todays gold price in Delhi - {}'.format(gold_price))
    msg['Subject'] = 'Gold Price'
    msg['From'] constants.my_email
    msg['To'] = constants.email
    server.send_message(msg)
    server.quit()


if __name__ == '__main__':
    send_email(get_bid_price())
    # get_bid_price()
