### Crypto Telegram Bot

A simple Telegram bot that provides real-time cryptocurrency prices and historical price charts for Bitcoin and Ethereum. The bot integrates the CoinGecko API for fetching cryptocurrency data and uses Matplotlib to generate historical charts.
Features

- Fetch current prices for Bitcoin and Ethereum using the `/price` command.  
- Generate historical price charts for a specified cryptocurrency and time range using the /chart command.  
- User-friendly interaction with robust error handling.

## Getting Started
### Prerequisites

1. To run this project, you need the following installed on your machine:

    - Python 3.7 or later

    - Required Python packages (see below)

    - A Telegram bot token (from the BotFather)

    - An OpenAI API key (optional if extending functionality)

2. Installation

Clone the repository or download the code:
```
git clone https://github.com/Sam-Nyalik/simple-telegram-bot.git
cd simple-telegram-bot
```

3. Install the required Python librariesm using `pip`
  
    matplotlib
    requests
    pyTelegramBotAPI
    openai

4. Replace placeholders in the main.py file:
       
  - Replace `{Use your telegram bot api}` with your Telegram bot token.
    
  - Replace `{Use your OPENAI API Key}` with your OpenAI API key (optional).

5. Running the Bot

  Navigate to the project directory:
```
  cd simple-telegram-bot
```

6. Run the bot:
  ```
    python main.py
 ```

7. Interact with the bot on Telegram.

## How to Use the Bot
Commands

1. Start the Bot:

  - Use the `/start` command to initiate interaction with the bot.

  - The bot will display a welcome message.

  - Check Current Prices:

  Use the `/price` command to fetch real-time prices for Bitcoin and Ethereum.

  Example response:
  ```
    Current cryptocurrency prices:
    Bitcoin: $36000
    Ethereum: $2500
  ```

2. Generate Historical Charts:

  - Use the `/chart` command followed by the cryptocurrency name and number of days.

  Example:
```
        Enter: bitcoin 30
```
  - The bot will generate a chart showing the historical price trend of Bitcoin over the last 30 days and send it as an image.

## Code Overview

  `main.py`: Contains the bot's logic, including fetching data from the CoinGecko API, generating charts, and handling user interactions.

  Functions:

  `get_crypto_prices()`: Fetches current prices for Bitcoin and Ethereum.  

  `get_historical_data(crypto_id, days)`: Retrieves historical price data.  

   `plot_historical_chart(prices, crypto_name)`: Generates and saves a price chart.  

## Error Handling

  - If the input format for the `/chart` command is incorrect, the bot prompts the user with the correct format.  

  - If the cryptocurrency name is invalid or not supported, the bot informs the user.  

  - All exceptions are logged for debugging purposes.

## Future Enhancements

  - Add support for more cryptocurrencies.

  - Integrate OpenAI's API to generate market insights.

  - Deploy the bot on a server for continuous availability.

## License

- This project is licensed under the MIT License. 
