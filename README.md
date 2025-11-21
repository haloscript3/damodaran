# Sahibinden.com Price Analysis Bot

This project is a Python bot that collects property listing prices from sahibinden.com and performs statistical analysis.

## Features

- Automatic price data collection from sahibinden.com
- Pagination support to scan all listings
- Statistical analysis (average, minimum, maximum price)
- Uses undetected-chromedriver to bypass anti-bot detection systems
- Automatic login page detection and waiting mechanism
- Natural browsing behavior simulation with random wait times

## Requirements

### System Requirements

- Python 3.7 or higher
- Google Chrome browser
- ChromeDriver (automatically managed by undetected-chromedriver)

### Python Packages

Install the required Python packages before running the project:

```bash
pip install selenium undetected-chromedriver
```

## Installation

1. Clone or download the project
2. Install required packages:

```bash
pip install -r requirements.txt
```

If the `requirements.txt` file does not exist, install packages manually:

```bash
pip install selenium undetected-chromedriver
```

## Usage

1. Navigate to the project directory in terminal or command line
2. Run the script:

```bash
python damodaran.py
```

3. The program will prompt you for a sahibinden.com URL. Example:

```
PLEASE ENTER THE SAHIBINDEN.COM URL:
URL: https://www.sahibinden.com/satilik-daire/istanbul?pagingSize=50
```

4. When the first page loads, there is a 45-second waiting period. You can manually log in during this time if necessary.

5. The bot will automatically scan all pages and collect price data.

6. When the process is completed or stopped, a statistical summary of the collected data will be displayed.

## How It Works

1. **URL Processing**: The `pagingSize=50` parameter is added to the given URL (if not present)
2. **Browser Initialization**: Browser is started with Undetected ChromeDriver
3. **Page Scanning**: For each page:
   - The `pagingOffset` parameter is added to the URL
   - Page is loaded and random wait times are applied
   - Page is scrolled and price elements are found
   - Prices are cleaned and converted to numeric values
4. **Data Collection**: Prices collected from all pages are accumulated in a list
5. **Statistical Calculation**: Minimum, maximum, and average prices are calculated from the collected data

## Output Format

When the program runs, it displays the following information:

```
FINAL REPORT
TOTAL PAGES SCANNED : 5
TOTAL ITEMS         : 250
MIN PRICE           : 500,000.00
MAX PRICE           : 2,500,000.00
AVERAGE PRICE       : 1,200,000.00
```

## Important Notes

- There is a 45-second waiting period when the first page loads. You can manually log in during this time if necessary.
- If a login page is detected, a 45-second waiting period is provided.
- The program can be stopped with `Ctrl+C` while running.
- Random wait times between 10-15 seconds are applied between each page.
- Page scrolling operations are performed at random intervals.

## Error Handling

- If no URL is entered, the program displays an error message and exits
- If price elements cannot be found, the program terminates
- If login is not completed after 45 seconds on the login page, the program terminates
- Safe exit can be performed with KeyboardInterrupt (Ctrl+C)

## Technical Details

- **Selenium**: Used for web automation
- **undetected-chromedriver**: Used to bypass bot detection systems
- **SSL**: SSL verification is disabled (for development purposes)
- **Randomness**: Random module is used to simulate natural user behavior

## License

This project is for educational and personal use only. It should be used in accordance with sahibinden.com's terms of use.

## Disclaimer

This bot is for educational and research purposes only. Web scraping operations should be performed in accordance with the terms of use of websites. The user is responsible for complying with the service terms and legal regulations of the relevant website when using this tool.
