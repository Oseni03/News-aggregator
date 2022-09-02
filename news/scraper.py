import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def latest():
    base_url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKT1J5Z0FQAQ?hl=en-NG&gl=NG&ceid=NG%3Aen"
    response = requests.get(base_url) 
    soup = BeautifulSoup(response.text, 'html.parser')
    stories = []
    
    articles = soup.find_all("article", {"jscontroller": "HyhIue"})
    for article in articles:
        url = article.a.get("href")
        try:
            image = article.find("figure").img.get("src")
        except:
            image = None
        
        try:
            title = article.h3.text
        except:
            title = article.h4.text
        source = article.div.div.a.text
        source_url = article.div.div.a.get("href")
        time = article.div.div.time.text        
        
        story = {"url": urljoin(base_url, url), "title": title, "image": image, 
                 "source_url": urljoin(base_url, source_url), "time": time, "source": source}
        stories.append(story)
    return stories
        
        


# c = Scraper()
# # news = c.all_news()
# world = c.all_news()
# print(world)

# news = latest()
# print(news)