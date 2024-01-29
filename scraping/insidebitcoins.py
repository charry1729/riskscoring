import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime


def insidebitcoins_scrape(entity, start_date, end_date):
    website_url = "https://insidebitcoins.com/news"
    page_num = 1
    current_date = end_date

    # replace spaces in entity with a +
    entity_search = entity.replace(" ", "+")

    # create output dataframe
    column_names = ["date_time", "title", "excerpt", "article_url", "image_url", "source_id"]
    df = pd.DataFrame(columns = column_names)
    print(df)
    # keep retrieving data from next page as long as it is within date range
    while current_date >= start_date: 
        # new page of queries
        search = website_url + f"/page/{page_num}?s={entity_search}&submit=Search"
        page = requests.get(search)
        soup = BeautifulSoup(page.content, features="html.parser")
        # print(soup)
        # retrieve article items
        results = soup.find_all('a', class_='article-header-title') 
        # print(results)

        # Extract and format links and titles
        formatted_output = ""
        for i, a_element in enumerate(results, 1):
            href = a_element.get('href')
            title = a_element.text.strip()
            
            formatted_output += f"{i}\n<a href=\"{href}\" rel=\"nofollow\" target=\"_blank\">{title}</a>\n"

        # Print the formatted output
        print(formatted_output)

        # no articles retrieved from search
        if len(results) == 0:
            break

        # loop through results to extract information
        for i in range(len(results)): 
            try: 
                # retrieve date 
                date_string = results[i].find(class_="w-post-elm post_date entry-date updated")["datetime"]
                date_time = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")

                # date_string = results[i].find(class_="c-ArticleInfo--date").find("span").text
                # print(date_string)
            except:
                pass
                continue

            date_time = datetime.strptime(date_string, "%d %B %Y ") 
            current_date = date_time # update current date 
  
            if date_time > end_date:  # if after cut-off date, skip
                continue
            if date_time < start_date: # if before cut-off date, stop scraping
                break
            
            # retrieve title and article link
            title = results[i].find("a") 
            article_url = title["href"] 
            title_text = title.text

            # retrieve excerpt
            excerpt = results[i].find(class_="fin-excerpt").text.strip()

            # retrieve image link
            image_url = results[i].find("img")["src"]

            # retrieve source id
            source_id = results[i]['id']

            # add information to dataframe
            df = df.append({"date_time": date_time, "title": title_text, \
                            "excerpt": excerpt, "article_url": article_url, \
                            "image_url": image_url, "source_id": source_id,
                            }, ignore_index=True)

        page_num += 1 # scrape next page
        
    return df

# testing function
entity = "ethereum"
start_date = datetime(2020, 7, 17)
end_date = datetime(2023, 8, 17)
test = insidebitcoins_scrape(entity, start_date, end_date)
