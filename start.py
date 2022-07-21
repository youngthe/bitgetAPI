import bitget.mix.market_api as market
import telegram
import time

def get_bit_price_and_push_tellegram():
    if __name__ == '__main__':
        api_key = ""
        secret_key = ""
        passphrase = ""  # 口令
        symbol = 'BTCUSDT_UMCBL'
        marketApi = market.MarketApi(api_key, secret_key, passphrase, use_server_time=False, first=False)

        result = marketApi.market_price(symbol)
        print(result['data']['markPrice'])


        token = "5485472375:AAElgB2dPCgmRksLYrj1vN4FTmhyptQNOLM" #토큰을 변수에 저장
        bot = telegram.Bot(token = token)
        chat_id = "1519429923"
        bot.sendMessage(chat_id = chat_id , text=result['data']['markPrice'])

while 1:
    get_bit_price_and_push_tellegram()
    time.sleep(60)
