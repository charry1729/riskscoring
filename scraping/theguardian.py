import json
import requests
from datetime import datetime
import pandas as pd
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        return result['encoding']

def theguardian_scrape(entity, start_date, end_date):
    file_path = '/Users/charry/nft/lynx-blockchain-risk-scoring/scraping/api_key.json'

    # Detect the file encoding
    file_encoding = detect_encoding(file_path)

    # If encoding is not detected, default to 'utf-8'
    if file_encoding is None:
        file_encoding = 'latin1'

    try:
        # Open the file in binary mode, decode its contents using detected encoding
        with open(file_path, 'rb') as f:
            content = f.read().decode(file_encoding)

        # Load the JSON data
        api_key_data = json.loads(content)
        print("api_key_data", api_key_data)

    except UnicodeDecodeError as e:
        print(f"Error decoding file with encoding {file_encoding}: {e}")
        api_key_data = None  # Assign a default value to avoid UnboundLocalError

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        api_key_data = None  # Assign a default value to avoid UnboundLocalError

    # Check if api_key_data is None before using it
    if api_key_data is None:
        return pd.DataFrame(columns=["date_time", "title", "excerpt", "article_url", "source_id"])

    # ... rest of your code remains unchanged ...


    # set search parameters
    search_api_url = "http://content.guardianapis.com/search"
    search_params = {
        "q": entity,
        "from-date": start_date.strftime("%Y-%m-%d"),
        "to-date": end_date.strftime("%Y-%m-%d"),
        "order-by": "newest",
        "show-fields": "all",
        "page-size": 200,
        "api-key": api_key_data
    }

    # retrieve results
    page_num = 1
    total_pages = 1
    all_results = []

    column_names = ["date_time", "title", "excerpt", "article_url", "source_id"]
    df = pd.DataFrame(columns = column_names)

    try:
        while page_num <= total_pages:
            search_params["page"] = page_num
            page = requests.get(search_api_url, search_params)
            data = page.json()
            all_results.extend(data['response']['results'])
            
            # if there is more than one page
            page_num += 1
            total_pages = data['response']['pages']
    except:
        return df # empty dataframe
    
    # parse results into dataframe
    for result in all_results:
        try:
            # retrieve source id
            source_id = result["id"]

            # retrieve date
            date_string = result["webPublicationDate"]
            date_time = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")

            # retrieve title
            title_text = result["webTitle"]
            article_url = result["webUrl"]

            # retrieve excerpt
            excerpt = result["fields"]["bodyText"]

            # add information to dataframe when entity is in text (self-filter)
            if (entity.lower() in title_text.lower()) or (entity.lower() in excerpt.lower()):
                df = df.append({"date_time": date_time, "title": title_text, \
                        "excerpt": excerpt, "article_url": article_url, \
                            "source_id": source_id
                    }, ignore_index=True)
        except:
            continue # if error, skip 
    
    return df

entity = "Ethereum"
start_date = datetime(2019, 1, 1)
end_date = datetime(2023, 12, 30)
df = theguardian_scrape(entity, start_date, end_date)
print(df)