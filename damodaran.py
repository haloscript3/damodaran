import time
import statistics
import ssl
import random
import sys
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By

ssl._create_default_https_context = ssl._create_unverified_context

def scroll_page(driver):
    try:
        driver.execute_script(f"window.scrollTo(0, {random.randint(300, 700)});")
        time.sleep(random.uniform(1, 2))
        driver.execute_script(f"window.scrollTo(0, {random.randint(800, 1200)});")
        time.sleep(random.uniform(1, 2))
    except:
        pass

def run():
    print("PLEASE ENTER THE SAHIBINDEN.COM URL:")
    base_url = input("URL: ").strip()
    
    if not base_url:
        print("ERROR: URL IS REQUIRED.")
        return

    if "pagingSize=50" not in base_url:
        separator = "&" if "?" in base_url else "?"
        base_url += f"{separator}pagingSize=50"

    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-popup-blocking")

    try:
        driver = uc.Chrome(options=options, use_subprocess=True)
    except Exception:
        driver = uc.Chrome(options=options)

    all_prices = []
    offset = 0
    page_number = 1

    try:
        while True:
            separator = "&" if "?" in base_url else "?"
            current_url = f"{base_url}{separator}pagingOffset={offset}"
            
            print(f"PROCESSING PAGE {page_number} (Total Items: {len(all_prices)})...")
            
            driver.get(current_url)
            
            if page_number == 1:
                print("WAITING 20 SECONDS FOR INITIAL LOAD OR LOGIN...")
                time.sleep(20)
            else:
                sleep_time = random.uniform(10, 15)
                print(f"WAITING {sleep_time:.1f} SECONDS")
                time.sleep(sleep_time)

            if "login" in driver.current_url:
                print("LOGIN PAGE DETECTED. PLEASE LOGIN WITHIN 30 SECONDS")
                time.sleep(45)
                if "login" in driver.current_url:
                    break

            scroll_page(driver)

            page_prices = []
            elements = driver.find_elements(By.CLASS_NAME, "searchResultsPriceValue")

            for el in elements:
                try:
                    text = el.text.strip()
                    clean_text = text.replace(" TL", "").replace(".", "").replace(",", ".")
                    if clean_text:
                        page_prices.append(float(clean_text))
                except ValueError:
                    pass
            
            if not page_prices:
                print("NO MORE ITEMS FOUND.")
                break
            
            print(f"FOUND {len(page_prices)} ITEMS ON THIS PAGE.")
            all_prices.extend(page_prices)
            
            offset += 50
            page_number += 1

    except KeyboardInterrupt:
        print("STOPPED BY USER.")
    except Exception as e:
        print(f"ERROR: {e}")
    finally:
        try:
            driver.quit()
        except:
            pass

    print("FINAL REPORT")

    if all_prices:
        avg_price = statistics.mean(all_prices)
        min_price = min(all_prices)
        max_price = max(all_prices)

        print(f"TOTAL PAGES SCANNED : {page_number - 1}")
        print(f"TOTAL ITEMS         : {len(all_prices)}")
        print(f"MIN PRICE           : {min_price:,.2f}")
        print(f"MAX PRICE           : {max_price:,.2f}")
        print(f"AVERAGE PRICE       : {avg_price:,.2f}")
    else:
        print("NO DATA COLLECTED.")

if __name__ == "__main__":
    run()
