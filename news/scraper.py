import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# from .models import Category

class Scraper:
    def __init__(self):
        self.base_url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFZxYUdjU0JXVnVMVWRDR2dKT1J5Z0FQAQ?hl=en-NG&gl=NG&ceid=NG%3Aen"
        response = requests.get(self.base_url) 
        self.soup = BeautifulSoup(response.text, 'html.parser')
    
    def latest(self):
        stories = []
        
        articles = self.soup.find_all("article", {"jscontroller": "HyhIue"})
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
            
            story = {"url": urljoin(self.base_url, url), "title": title, "image": image, 
                    "source_url": urljoin(self.base_url, source_url), "time": time, "source": source}
            stories.append(story)
        return stories
    
    def categories(self):
        all = []
        
        lists = self.soup.find_all("a", {"class": "SFllF"})
        for list in lists:
            url = list.get("href")
            title = list.text
            all.append({"title": title, "url": urljoin(self.base_url, url)})
        return all[2:11]
    
    def world_news(self):
        self.base_url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JXVnVMVWRDR2dKT1J5Z0FQAQ?hl=en-NG&gl=NG&ceid=NG%3Aen"
        response = requests.get(self.base_url) 
        self.soup = BeautifulSoup(response.text, 'html.parser')
        
        stories = []
        
        articles = self.soup.find_all("article", {"jscontroller": "HyhIue"})
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
            
            story = {"url": urljoin(self.base_url, url), "title": title, "image": image, 
                    "source_url": urljoin(self.base_url, source_url), "time": time, "source": source}
            stories.append(story)
        return stories
    
    def business_news(self):
        self.base_url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JXVnVMVWRDR2dKT1J5Z0FQAQ?hl=en-NG&gl=NG&ceid=NG%3Aen"
        response = requests.get(self.base_url) 
        self.soup = BeautifulSoup(response.text, 'html.parser')
        
        stories = []
        
        articles = self.soup.find_all("article", {"jscontroller": "HyhIue"})
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
            
            story = {"url": urljoin(self.base_url, url), "title": title, "image": image, 
                    "source_url": urljoin(self.base_url, source_url), "time": time, "source": source}
            stories.append(story)
        return stories
    
    def technology_news(self):
        self.base_url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGRqTVhZU0JXVnVMVWRDR2dKT1J5Z0FQAQ?hl=en-NG&gl=NG&ceid=NG%3Aen"
        response = requests.get(self.base_url) 
        self.soup = BeautifulSoup(response.text, 'html.parser')
        
        stories = []
        
        articles = self.soup.find_all("article", {"jscontroller": "HyhIue"})
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
            
            story = {"url": urljoin(self.base_url, url), "title": title, "image": image, 
                    "source_url": urljoin(self.base_url, source_url), "time": time, "source": source}
            stories.append(story)
        return stories
    
    def entertainment_news(self):
        self.base_url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNREpxYW5RU0JXVnVMVWRDR2dKT1J5Z0FQAQ?hl=en-NG&gl=NG&ceid=NG%3Aen"
        response = requests.get(self.base_url) 
        self.soup = BeautifulSoup(response.text, 'html.parser')
        
        stories = []
        
        articles = self.soup.find_all("article", {"jscontroller": "HyhIue"})
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
            
            story = {"url": urljoin(self.base_url, url), "title": title, "image": image, 
                    "source_url": urljoin(self.base_url, source_url), "time": time, "source": source}
            stories.append(story)
        return stories
    
    def sport_news(self):
        self.base_url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JXVnVMVWRDR2dKT1J5Z0FQAQ?hl=en-NG&gl=NG&ceid=NG%3Aen"
        response = requests.get(self.base_url) 
        self.soup = BeautifulSoup(response.text, 'html.parser')
        
        stories = []
        
        articles = self.soup.find_all("article", {"jscontroller": "HyhIue"})
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
            
            story = {"url": urljoin(self.base_url, url), "title": title, "image": image, 
                    "source_url": urljoin(self.base_url, source_url), "time": time, "source": source}
            stories.append(story)
        return stories
    
    def science_news(self):
        self.base_url = "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp0Y1RjU0JXVnVMVWRDR2dKT1J5Z0FQAQ?hl=en-NG&gl=NG&ceid=NG%3Aen"
        response = requests.get(self.base_url) 
        self.soup = BeautifulSoup(response.text, 'html.parser')
        
        stories = []
        
        articles = self.soup.find_all("article", {"jscontroller": "HyhIue"})
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
            
            story = {"url": urljoin(self.base_url, url), "title": title, "image": image, 
                    "source_url": urljoin(self.base_url, source_url), "time": time, "source": source}
            stories.append(story)
        return stories
    
    def health_news(self):
        self.base_url = "https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JXVnVMVWRDS0FBUAE?hl=en-NG&gl=NG&ceid=NG%3Aen"
        response = requests.get(self.base_url) 
        self.soup = BeautifulSoup(response.text, 'html.parser')
        
        stories = []
        
        articles = self.soup.find_all("article", {"jscontroller": "HyhIue"})
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
            
            story = {"url": urljoin(self.base_url, url), "title": title, "image": image, 
                    "source_url": urljoin(self.base_url, source_url), "time": time, "source": source}
            stories.append(story)
        return stories



if __name__ == "__main__":
    scraper = Scraper()
    # categories = scraper.categories()
    
    # for category in categories:
    #     new = Category.objects.create(title=category.title, url=category.url)
    #     new.save()
    
    news = scraper.health_news()
    print(news)
    
    