from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#ListingsSheet: SPREADSHEET = '1JzuPUV8zKEXSwwXB5o7TbqfuULKk9vBgBd8HGlubVVE'
#UsersSheet:


def GetRelevantListings(input : str) -> list[str]:
    SPREADSHEET = '1JzuPUV8zKEXSwwXB5o7TbqfuULKk9vBgBd8HGlubVVE'
    SAMPLE_RANGE_NAME = 'A2:A'
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET,range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    sales = []
    for sale in values:
        if input in sale[0].lower():
            sales.append(sale[0])
    return sales

def GetInformationAboutListing(listing : str):
    SPREADSHEET = '1JzuPUV8zKEXSwwXB5o7TbqfuULKk9vBgBd8HGlubVVE'
    SAMPLE_RANGE_NAME = 'A2:A'
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET,range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    for index, sale in enumerate(values):
        if sale[0] == listing:
            return sheet.values().get(spreadsheetId=SPREADSHEET,range="A" + str(index + 2) + ":H" + str(index + 2)).execute().get('values', [])[0]

def PopulateTable():
    from random import randint
    from extra import POKEMON
    SPREADSHEET = '1JzuPUV8zKEXSwwXB5o7TbqfuULKk9vBgBd8HGlubVVE'
    service = build('sheets', 'v4', credentials=creds)

    values = [[mon, "A strong " + mon, "",  randint(1000, 10000), "02/02/2022"] for mon in POKEMON]

    body = {
        'values': values
    }
    result = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET, range= "A2:E",valueInputOption='RAW', body=body).execute()
    '''
    for index, i in enumerate(POKEMON):
        for setting in "ABDE":

            if setting is "A":
                values = [
                    [i]
                ]

            elif setting is "B":
                values = [
                    ["A strong " + i]
                ]

            elif setting is "D":
                values = [
                    [str(randint(100, 500))]
                ]

            else:
                values = [
                    ['02/02/2022']
                ]
            body = {
                'values': values
            }
            result = service.spreadsheets().values().update(spreadsheetId=SPREADSHEET, range=setting + str(index + 2),valueInputOption='RAW', body=body).execute()
    '''

def LogIn(username, password):
    SPREADSHEET = '1tiEM_5_s7dBH6ZmPYc-6xahE5cQcAU5pmZ8R-F4mUSo'
    SAMPLE_RANGE_NAME = 'B2:H'
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET,range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    for sale in values:
        if username == sale[0] and password == sale[-1]:
            return True
    return False


def Register(information):
    service = build('sheets', 'v4', credentials=creds)
    spreadsheet_id = '1tiEM_5_s7dBH6ZmPYc-6xahE5cQcAU5pmZ8R-F4mUSo'
    range_ = 'A:K'
    value_range_body = {
        "values": [information]
    }

    request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_, valueInputOption='RAW', body=value_range_body)
    response = request.execute()

def VerifyUser(number: str):
    from twilio.rest import Client
    from random import randint
    code = randint(1000000, 9999999)
    account_sid = 'ACe52cd1bed6f876f7a5bad70ef28bf4e8'
    auth_token = '070a76cbea69fdc82ae3de8752a01b53'
    client = Client(account_sid, auth_token)
    number = number.strip().replace(" ", "")
    number = "+1" + number
    message = client.messages \
                    .create(
                        body="Your verification code is: " + str(code),
                        from_='+12264074033',
                        to=number
                    )

    return str(code)

#No Testing
def CreateAuction(saleInfo):
    service = build('sheets', 'v4', credentials=creds)
    spreadsheet_id = '1JzuPUV8zKEXSwwXB5o7TbqfuULKk9vBgBd8HGlubVVE'
    range_ = 'A:H'
    value_range_body = {
        "values": [saleInfo]
    }

    request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_, valueInputOption='RAW', body=value_range_body)
    response = request.execute()

def getAuction(auction : str):
    SPREADSHEET = '1JzuPUV8zKEXSwwXB5o7TbqfuULKk9vBgBd8HGlubVVE' 
    SAMPLE_RANGE_NAME = 'A2:B'
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET,range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    for index, each in enumerate(values):
        if each[0] == auction:
            SAMPLE_RANGE_NAME = 'A' + str(index + 2) + ":H" + str(index + 2)
            result = sheet.values().get(spreadsheetId=SPREADSHEET,range=SAMPLE_RANGE_NAME).execute()
            return result.get('values')

def placeBid(amount : int, auction : str, auctioneer : str, buyout : int):
    SPREADSHEET = '1JzuPUV8zKEXSwwXB5o7TbqfuULKk9vBgBd8HGlubVVE' 
    SAMPLE_RANGE_NAME = 'A2:B'
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET,range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    for index, each in enumerate(values):
        if each[0] == auction:
            SAMPLE_RANGE_NAME = 'A' + str(index + 2) + ":H" + str(index + 2)
            result = sheet.values().get(spreadsheetId=SPREADSHEET,range=SAMPLE_RANGE_NAME).execute()
            bids = result.get('values', [])[-1][-2]
            currBid = bids.split("|")[-1]
            startingBid = result.get('values', [])[-1][3]


            if int(startingBid) > int(amount):
                return ("Your bid must be larger then the starting bid.", '#FF0000')

            elif int(amount) >= int(buyout):
                BuyItem(amount, auction, auctioneer)
                return ("Your bid has passed the buyout price. Congratulations on your purchase!", "#428AF5")

            elif currBid == '':
                value = [[str(amount) + " - " + auctioneer]]
                body = {
                    'values': value
                }
                service.spreadsheets().values().update(spreadsheetId=SPREADSHEET, range= "G" + str(index + 2) + ":H" + str(index + 2),valueInputOption='RAW', body=body).execute()
                return ("Your bid has been successfully placed!", "#00AB00")

            elif int(currBid[0:currBid.find('-')]) < int(amount):
                value = [[bids + "|" + str(amount) + " - " + auctioneer]]
                body = {
                    'values': value
                }
                service.spreadsheets().values().update(spreadsheetId=SPREADSHEET, range= "G" + str(index + 2) + ":H" + str(index + 2),valueInputOption='RAW', body=body).execute()
                return ("Your bid has been successfully placed!", "#00AB00")
            else:
                return ("Your bid is lower then the current highest, and was thus not applied", "#FF0000")

#Purchase an item (final sale part)
def BuyItem(amount, auction, buyer):
    #Get buyer phone number
    SPREADSHEET = '1tiEM_5_s7dBH6ZmPYc-6xahE5cQcAU5pmZ8R-F4mUSo'
    SAMPLE_RANGE_NAME = 'B2:D'
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET,range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    for sale in values:
        if buyer == sale[0]:
            number = sale[2]
            break

    #Text buyer
    from twilio.rest import Client
    account_sid = 'ACe52cd1bed6f876f7a5bad70ef28bf4e8'
    auth_token = '070a76cbea69fdc82ae3de8752a01b53'
    client = Client(account_sid, auth_token)
    number = "+1" + number
    message = client.messages.create(
                        body="You have successfully purchased " + auction + " for " + str(amount) + ". Congratulations on your purchase!",
                        from_='+12264074033',
                        to=number
                    )

    #Remove from sale
    SPREADSHEET = '1JzuPUV8zKEXSwwXB5o7TbqfuULKk9vBgBd8HGlubVVE' 
    SAMPLE_RANGE_NAME = 'A2:F'
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET,range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    for index, each in enumerate(values):
        if each[0] == auction:
            seller = each[-1]
            SAMPLE_RANGE_NAME = 'A' + str(index + 2) + ":H" + str(index + 2)

    request = service.spreadsheets().values().clear(spreadsheetId=SPREADSHEET, range=SAMPLE_RANGE_NAME, body={})
    response = request.execute()
    #get seller number
    SPREADSHEET = '1tiEM_5_s7dBH6ZmPYc-6xahE5cQcAU5pmZ8R-F4mUSo'
    SAMPLE_RANGE_NAME = 'B2:H'
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET,range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    for sale in values:
        if seller == sale[0]:
            number = sale[2]

    #Text seller
    from twilio.rest import Client
    account_sid = 'ACe52cd1bed6f876f7a5bad70ef28bf4e8'
    auth_token = '070a76cbea69fdc82ae3de8752a01b53'
    client = Client(account_sid, auth_token)
    number = "+1" + number
    message = client.messages.create(
                        body="Your auction for " + auction + " has successfully been sold for  " + str(amount) + ". Congratulations on your sale!",
                        from_='+12264074033',
                        to=number
                    )
    print('sold')


def wrapText(description ,index):
    OutTextRaw = description
    while len(OutTextRaw) > index:

        if OutTextRaw.find('\n', index - 55) != -1:
            index = OutTextRaw.find('\n', index - 55) + 60

        else:
            while OutTextRaw[index] != " ":
                index = index - 1

            OutTextRaw = OutTextRaw[0:index] + "\n" + OutTextRaw[index + 1:]
            index += 60
    return OutTextRaw

def ForgotPassword(number):
    from twilio.rest import Client
    SPREADSHEET = '1tiEM_5_s7dBH6ZmPYc-6xahE5cQcAU5pmZ8R-F4mUSo'
    SAMPLE_RANGE_NAME = 'D2:H'
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET,range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])
    password = ""

    for each in values:
        if each[0] == number:
            password = each[4]
            break

    if password == "":
        return

    account_sid = 'ACe52cd1bed6f876f7a5bad70ef28bf4e8'
    auth_token = '070a76cbea69fdc82ae3de8752a01b53'
    client = Client(account_sid, auth_token)
    number = "+1" + str(number)
    message = client.messages.create(
                        body="Your password is " + password,
                        from_='+12264074033',
                        to=number
                    )
    return
    