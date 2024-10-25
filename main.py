# Import Modules
import requests
import os
import env


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
aas_api_key = os.environ.get("AAS_API_KEY")
news_api_key = os.environ.get("NEWS_API_KEY")

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "outputsize" : "compact",
    "apikey" : aas_api_key,
}

news_parameters = {
    "q" : "tesla",
    "from" : "2024-09-25",
    "sortBy" : "publishedAt",
    "apikey" : news_api_key,
}

response = requests.get(url = STOCK_ENDPOINT, params= stock_parameters)

response.raise_for_status()

# print(response.status_code)

stock_data = response.json()["Time Series (Daily)"]
stock_list = [value for (key, value) in stock_data.items()]

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

yesterday_stock_price = float(stock_list[0]["4. close"])
print(yesterday_stock_price)

#TODO 2. - Get the day before yesterday's closing stock price
two_days_before_stock_price = float(stock_list[1]["4. close"])
print(two_days_before_stock_price)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

stock_price_difference = abs(two_days_before_stock_price - yesterday_stock_price)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

diff_perc = (stock_price_difference/two_days_before_stock_price)*100
print(diff_perc)

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

if perc_diff > 5:
    print("Get News")



https://newsapi.org/v2/everything?q=tesla&from=2024-09-25&sortBy=publishedAt&apiKey=API_KEY

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

