from activecampaign.client import Client
from activecampaign.contacts import Contacts
# from activecampaign.account import Account
import activecampaign

def add_contact(email):

    URL = 'https://maged918.api-us1.com'
    APIKEY= '4b5ea30480c73f4ff3a1fdf8fd7b2bd9bc29303f73ac44349a819b0313a9b8f4a7e7d805'
    client = Client(URL, APIKEY)
    print(client)

    c = Contacts(client)
    c.create_contact(data={'email':email})