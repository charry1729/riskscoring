# # from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# import pandas as pd
# from datetime import datetime
# # from webdriver_manager.chrome import ChromeDriverManager
# # driver = webdriver.Chrome(ChromeDriverManager().install())
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# # Open Scrapingbee's website
# # driver.get("http://www.scrapingbee.com")
# # ... (imports)

# def bitcoin_scrape(entity, start_date, end_date):
#     column_names = ['date_time', 'title', 'excerpt', 'article_url', 'image_url', 'category']
#     output = pd.DataFrame(columns=column_names)

#     options = Options()
#     options.headless = True
#     driver = webdriver.Chrome(ChromeDriverManager().install())

#     page_number = 1
#     continue_search = True

#     while continue_search:
#         try:
#             url = f"https://news.bitcoin.com/page/{page_number}"
#             driver.get(url)
#             html_content = driver.page_source
#             soup = BeautifulSoup(html_content, 'html.parser')
#             print("soup",soup)
#             # Extract information for each article
#             news = soup.find_all('div', class_='td_module_16 td_module_wrap td-animation-stack')
#             for article in news:
#                 title = article.find('h3', class_='entry-title').text.strip()
#                 # Extract other information (excerpt, article URL, etc.) similarly

#                 # Append data to the DataFrame
#                 row_data = {'date_time': '', 'title': title, 'excerpt': '', 'article_url': '', 'image_url': '', 'category': ''}
#                 output = output.append(row_data, ignore_index=True)

#             page_number += 1

#             # Break loop if no search results
#             if len(news) == 0:
#                 break

#             # Implement date filtering logic here

#         except Exception as e:
#             print(f"Error: {e}")

#     driver.quit()
#     return output

# # ... (rest of your code)

# # Testing function
# start_date = datetime(2020, 8, 20)
# end_date = datetime(2023, 8, 30)
# test = bitcoin_scrape("bitcoin", start_date, end_date)
# print(test)


# # def bitcoin_scrape(entity, start_date, end_date):
# #     # create output df
# #     column_names = ['date_time', 'title', 'excerpt', 'article_url', 'image_url', 'category']
# #     output = pd.DataFrame(columns=column_names)

# #     # Configure Selenium options
# #     options = Options()
# #     options.headless = True

# #     # Initialize Selenium WebDriver
# #     # driver = webdriver.Chrome(options=options)
# #     driver = webdriver.Chrome(ChromeDriverManager().install())

# #     page_number = 1
# #     continue_search = True

# #     while continue_search:
# #         try:

# #             url = f"https://news.bitcoin.com/page/{page_number}"

# #             # Use Selenium to load the page
# #             driver.get(url)
# #             html_content = driver.page_source

# #             # Use BeautifulSoup to parse the HTML
# #             soup = BeautifulSoup(html_content, 'html.parser')
# #             print(soup)
# #             # Locate relevant sections
# #             news = soup.find_all('div', class_='td_module_16 td_module_wrap td-animation-stack')
# #             news_details = soup.find_all('div', class_='td-module-meta-info')
# #             news_excerpt = soup.find_all('div', class_='td-excerpt')

# #             # ... (rest of your code for processing articles)

# #             # Increment page number
# #             page_number += 1

# #             # Break loop if no search results
# #             if len(news) == 0:
# #                 break
# #             # Your scraping code here
# #         except Exception as e:
# #             print(f"Error: {e}")

# #     # Close the Selenium WebDriver
# #     driver.quit()

# #     return output

# # # Testing function
# # start_date = datetime(2020, 8, 20)
# # end_date = datetime(2023, 8, 30)
# # test = bitcoin_scrape("bitcoin", start_date, end_date)
# # print(test)



# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from bs4 import BeautifulSoup
# import pandas as pd
# from datetime import datetime
# from webdriver_manager.chrome import ChromeDriverManager

# def bitcoin_scrape_page(page_number):
#     column_names = ['date_time', 'title', 'excerpt', 'article_url', 'image_url', 'category']
#     output = pd.DataFrame(columns=column_names)

#     options = Options()
#     options.headless = True
#     driver = webdriver.Chrome(ChromeDriverManager().install())

#     try:
#         url = f"https://news.bitcoin.com/page/{page_number}"
#         driver.get(url)
#         html_content = driver.page_source
#         soup = BeautifulSoup(html_content, 'html.parser')
#         print("soup",soup)
#         # Extract information for each article
#         news = soup.find_all('div', class_='td_module_16 td_module_wrap td-animation-stack')
#         for article in news:
#             title = article.find('h3', class_='entry-title').text.strip()
#             # Extract other information (excerpt, article URL, etc.) similarly

#             # Append data to the DataFrame
#             row_data = {'date_time': '', 'title': title, 'excerpt': '', 'article_url': '', 'image_url': '', 'category': ''}
#             output = output.append(row_data, ignore_index=True)

#         # Implement date filtering logic here if needed

#     except Exception as e:
#         print(f"Error: {e}")

#     finally:
#         driver.quit()

#     return output

# # Specify the page number you want to scrape
# page_to_scrape = 2
# scraped_data = bitcoin_scrape_page(page_to_scrape)
# print(scraped_data)



# from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def bitcoin_scrape(entity, start_date, end_date):
    # create output df
    column_names = ['date_time', 'title', 'excerpt', 'article_url', 'image_url', 'category']
    output = pd.DataFrame(columns=column_names)

    # Configure Selenium options
    options = Options()
    options.headless = True

    from webdriver_manager.chrome import ChromeDriverManager
    from selenium import webdriver



    # Initialize Selenium WebDriver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver.set_page_load_timeout(30)  # Set the timeout to 30 seconds (adjust as needed)

    page_number = 1
    continue_search = True
    text_contents=[]

    # while continue_search:
    try:
        url = f"https://news.bitcoin.com/page/{page_number}"

        # Use Selenium to load the page
        driver.get(url)
        # Wait for the articles to be present on the page class="sc-fgavSd sc-gBwwDl buPdnA fnlpuo"
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'sc-fgavSd'))
        )
        html_content = driver.page_source
        # print("html_content",html_content)
        # Use BeautifulSoup to parse the HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        # print("soup",soup)

        a_element = soup.find_all('a', class_='sc-LGbXC bAnYxi')
        print("a_element",a_element)
        hrefs = []

        for element in a_element:
            try:
                if element:
                    href = element.get('href')
                    # print(href)
                else:
                    print("No matching 'a' element found.")


                # href = element.text
                hrefs.append(href)

            except Exception as e:
                print(f"Error while processing element: {e}")
       
        hrefs = list(set(hrefs))
        print("hrefs",hrefs)

        title_element = soup.find_all('h6', class_='sc-fgavSd sc-gBwwDl buPdnA fnlpuo')
        print('title_element',title_element)

        titles = []
        for element in title_element:
            try:
                title = element.text
                titles.append(title)
            except Exception as e:
                print(f"Error while processing element: {e}")

        # Extract image URL
        # image_url = article.find('img')['src'] if article.find('img') else None

        # # Extract title
        # title_container = article.find('h6')
        # print(title_container)
        # title = title_container.text.strip() if title_container else None

        # Append to the output DataFrame
        # output = output.append({'title': title, 'image_url': image_url}, ignore_index=True)
        # print("text_contents",text_contents)

        # Increment page number
        page_number += 1

        # Break loop if no search results
        # if len(text_contents) == 0:
        #     break
    except Exception as e:
        print(f"Error: {e}")
    # except TimeoutException:
    #     print("Timed out waiting for page to load")
    # Close the Selenium WebDriver
    for title in titles:
        print(title)

    driver.quit()

    return "data"

# Testing function
start_date = datetime(2020, 8, 20)
end_date = datetime(2023, 8, 30)
test = bitcoin_scrape("bitcoin", start_date, end_date)
print(test)
