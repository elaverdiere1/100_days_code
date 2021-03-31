import requests
from twilio.rest import Client

account_sid = 'twilioSID'
auth_token = 'twilioAUTHTOKEN'
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
alpha_api = 'AlphaVantageAPIKey'
alpha_website = 'https://www.alphavantage.co/query'
alpha_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': alpha_api,
}

response = requests.get(alpha_website, params=alpha_parameters)
response.raise_for_status()
data = response.json()
yesterday = float((list(data['Time Series (Daily)'].values())[0]['4. close']))
day_before = float((list(data['Time Series (Daily)'].values())[1]['4. close']))
daily_difference = yesterday - day_before
up_down = None
if daily_difference > 0:
    up_down = 'up'
else:
    up_down = 'down'
percent_change = round(daily_difference / yesterday * 100)

news_website = 'https://newsapi.org/v2/everything'
news_api = 'NewsAppAPIKey'
news_parameters = {
    'qInTitle': COMPANY_NAME,
    'pageSize': '3',
    'sortBy': 'publishedAt',
    'apikey': news_api,
}


if abs(percent_change) > 3:
    news_response = requests.get(news_website, params=news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()['articles']
    top_three = articles[:3]

    formatted_articles = [f"{STOCK}: {up_down}{percent_change}\nHeadline: {article['title']}\nBrief: {article['description']}" for article in top_three]

    client = Client(account_sid, auth_token)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='twilionumber',
            to='personalnumber',
        )

