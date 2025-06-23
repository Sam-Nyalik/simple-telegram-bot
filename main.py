import telebot
import openai
import requests
import datetime
import matplotlib.pyplot as plt

#API Keys
TELEGRAM_BOT_TOKEN = "{Use your telegram bot api}"
OPENAI_API_KEY = "{Use your OPENAI API Key}"
CRYPTO_API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"

# Initialize bot and OpenAI
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
openai.api_key = OPENAI_API_KEY

# Helper function to fetch crypto prices
def get_crypto_prices():
    try:
        response = requests.get(CRYPTO_API_URL)
        data = response.json()
        bitcoin_price = data["bitcoin"]["usd"]
        ethereum_price = data["ethereum"]["usd"]
        return f"Bitcoin: ${bitcoin_price}\n Ethereum: f{ethereum_price}"
    except Exception as e:
        return "Error fetching cryptocurrency prices!"
    
# Command handler for /start
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Sam Nyalik's Crypto bot! Use '/price' for current prices, amd use '/chart' to get the bitcoin or ethereum historical data!")
    
# Command handler for /price
@bot.message_handler(commands=["price"])
def send_price(message):
    prices = get_crypto_prices()
    bot.reply_to(message, f"Current cryptocurrency prices: \n\n {prices}")
    
# Fetch historical data
def get_historical_data(crypto_id, days):
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {"vs_currency": "usd", "days": days}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        prices = data["prices"]
        return prices
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []
    
# Generate a chart
def plot_historical_chart(prices, crypto_name):
    # Extract timestamps and prices 
    timestamps = [datetime.datetime.fromtimestamp(price[0] / 1000) for price in prices]
    values = [price[1] for price in prices]
    
    # Create the plot
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, values, label=crypto_name.capitalize(), color='blue')
    plt.title(f"{crypto_name.capitalize()} Price History")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    
    # Save the chart
    file_name = f"{crypto_name}_chart.png"
    plt.savefig(file_name)
    plt.close()
    return file_name

# Integrate the chart with our bot
@bot.message_handler(commands=["chart"])
def send_chart(message):
    try:
        bot.reply_to(message, "Enter the cryptocurrency and the number of days: (e.g:, 'bitcoin 30')")
        
        @bot.message_handler(func=lambda msg: True)
        def process_input(msg):
            try:
                input_data = msg.text.split()
                if len(input_data) != 2:
                    bot.reply_to(msg, "Please provide input in the format 'cryptocurrency days'.")
                    return 
                
                crypto_id, days = input_data[0].lower(), int(input_data[1])
                prices = get_historical_data(crypto_id, days)
                
                if not prices:
                    bot.reply_to(msg, "Could not fetch historical data.")
                    return
                
                file_name = plot_historical_chart(prices, crypto_id)
                
                with open(file_name, "rb") as chart:
                    bot.send_photo(msg.chat.id, chart)
            except Exception as e:
                bot.reply_to(msg, f"Error: {e}")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")
        
#Start the bot
if __name__ == "__main__":
    print("Bot is running...")
    bot.polling()