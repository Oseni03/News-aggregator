import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd


class Scraper:
    def __init__(self):
        self.base_url = "https://news.google.com/"
        response = requests.get(self.base_url) 
        self.soup = BeautifulSoup(response.text, 'html.parser')
    
    def headline_news(self):        
        category = self.soup.find('div', {'jslog': '127062; 3:W251bGwsbnVsbCxudWxsLG51bGwsInNlY3Rpb24tdG9waWMtbWlkOi9tLzA1amhnIixudWxsLDE0MSxudWxsLG51bGwsbnVsbCwzMDIsbnVsbCxudWxsLFtbWyIvbS8wNWpoZyJdXSxudWxsLDhdXQ==; track:vis ; index:0'})
        category_name = category.find("div", {'class': 'cp7Yvc'}).h2.text
        category_url = category.find("div", {'class': "cp7Yvc"}).find("a").get("href")
        news = category.find_all("div", {'jscontroller': "MRcHif"})
        
        a = {"category": category_name, "url": urljoin(self.base_url, category_url), "stories": []}
        
        for new in news:
            image = new.find("div", {'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}).a.figure.img.get("src")
            title = new.find("article").h3.text
            # url = new.find("div", {'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}).a.get("href")
            url = new.find("article").h3.a.get("href")
            source = new.find("article").div.a.text
            time = new.find("article").div.time.text
            
            b = {"image": image, "title": title, "url": urljoin(self.base_url, url), "source": source, "time": time, "sub_stories": []}
            
            sub_stories = new.find("div", {"class": "SbNwzf eeoZZ"}).find_all("article")
            for story in sub_stories:
                title = story.h4.text
                url = story.a.get("href")
                source = story.div.a.text
                source_url = story.div.a.get("href")
                time = story.div.time.text
                
                c = {"title": title, "url": urljoin(self.base_url, url), "source": source, "source_url": source_url, "time": time}
            b["sub_stories"].append(c)
        a["stories"].append(b)
        return a


    def nigeria_news(self):
        print(self.soup)
        category = self.soup.find('div', {'jslog': '127062; 3:W251bGwsbnVsbCxudWxsLG51bGwsInNlY3Rpb24tdG9waWMtbWlkOi9tLzA1Z2Y1IixudWxsLDE0MSxudWxsLG51bGwsbnVsbCwzMDIsbnVsbCxudWxsLFtbWyIvbS8wNWdmNSJdXSxudWxsLDhdLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLFtdXQ==; track:vis ; index:1'})
        category_name = category.find("div", {'class': 'cp7Yvc'}).h2.text
        category_url = category.find("div", {'class': "cp7Yvc"}).find("a").get("href")
        news = category.find_all("div", {'jscontroller': "MRcHif"})
        
        a = {"category": category_name, "url": urljoin(self.base_url, category_url), "stories": []}
        
        for new in news:
            image = new.find("div", {'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}).a.figure.img.get("src")
            title = new.find("article").h3.text
            # url = new.find("div", {'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}).a.get("href")
            url = new.find("article").h3.a.get("href")
            source = new.find("article").div.a.text
            time = new.find("article").div.time.text
            
            b = {"image": image, "title": title, "url": urljoin(self.base_url, url), "source": source, "time": time, "sub_stories": []}
            
            sub_stories = new.find("div", {"class": "SbNwzf eeoZZ"}).find_all("article")
            for story in sub_stories:
                title = story.h4.text
                url = story.a.get("href")
                source = story.div.a.text
                source_url = story.div.a.get("href")
                time = story.div.time.text
                
                c = {"title": title, "url": urljoin(self.base_url, url), "source": source, "source_url": source_url, "time": time}
            b["sub_stories"].append(c)
        a["stories"].append(b)
        return a


    def world_news(self):
        category = self.soup.find('div', {'jslog': '127062; 3:W251bGwsbnVsbCxudWxsLG51bGwsInNlY3Rpb24tdG9waWMtbWlkOi9tLzA5bm1fIixudWxsLDE0MSxudWxsLG51bGwsbnVsbCwzMDIsbnVsbCxudWxsLFtbWyIvbS8wOW5tXyJdXSxudWxsLDhdLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLFtdXQ==; track:vis ; index:2'})
        category_name = category.find("div", {'class': 'cp7Yvc'}).h2.text
        category_url = category.find("div", {'class': "cp7Yvc"}).find("a").get("href")
        news = category.find_all("div", {'jscontroller': "MRcHif"})
        
        a = {"category": category_name, "url": urljoin(self.base_url, category_url), "stories": []}
        
        for new in news:
            image = new.find("div", {'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}).a.figure.img.get("src")
            title = new.find("article").h3.text
            # url = new.find("div", {'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}).a.get("href")
            url = new.find("article").h3.a.get("href")
            source = new.find("article").div.a.text
            time = new.find("article").div.time.text
            
            b = {"image": image, "title": title, "url": urljoin(self.base_url, url), "source": source, "time": time, "sub_stories": []}
            
            sub_stories = new.find("div", {"class": "SbNwzf eeoZZ"}).find_all("article")
            for story in sub_stories:
                title = story.h4.text
                url = story.a.get("href")
                source = story.div.a.text
                source_url = story.div.a.get("href")
                time = story.div.time.text
                
                c = {"title": title, "url": urljoin(self.base_url, url), "source": source, "source_url": source_url, "time": time}
            b["sub_stories"].append(c)
        a["stories"].append(b)
        return a


    def business_news(self):
        category = self.soup.find('div', {'jslog': '127062; 3:W251bGwsbnVsbCxudWxsLG51bGwsInNlY3Rpb24tdG9waWMtbWlkOi9tLzA5czFmIixudWxsLDE0MSxudWxsLG51bGwsbnVsbCwzMDIsbnVsbCxudWxsLFtbWyIvbS8wOXMxZiJdXSxudWxsLDhdLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLFtdXQ==; track:vis ; index:3'})
        category_name = category.find("div", {'class': 'cp7Yvc'}).h2.text
        category_url = category.find("div", {'class': "cp7Yvc"}).find("a").get("href")
        news = category.find_all("div", {'jscontroller': "MRcHif"})
        
        a = {"category": category_name, "url": urljoin(self.base_url, category_url), "stories": []}
        
        for new in news:
            image = new.find("div", {'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}).a.figure.img.get("src")
            title = new.find("article").h3.text
            # url = new.find("div", {'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}).a.get("href")
            url = new.find("article").h3.a.get("href")
            source = new.find("article").div.a.text
            time = new.find("article").div.time.text
            
            b = {"image": image, "title": title, "url": urljoin(self.base_url, url), "source": source, "time": time, "sub_stories": []}
            
            sub_stories = new.find("div", {"class": "SbNwzf eeoZZ"}).find_all("article")
            for story in sub_stories:
                title = story.h4.text
                url = story.a.get("href")
                source = story.div.a.text
                source_url = story.div.a.get("href")
                time = story.div.time.text
                
                c = {"title": title, "url": urljoin(self.base_url, url), "source": source, "source_url": source_url, "time": time}
            b["sub_stories"].append(c)
        a["stories"].append(b)
        return a


    def technology_news(self):
        category = self.soup.find('div', {'jslog': '127062; 3:W251bGwsbnVsbCxudWxsLG51bGwsInNlY3Rpb24tdG9waWMtbWlkOi9tLzA3YzF2IixudWxsLDE0MSxudWxsLG51bGwsbnVsbCwzMDIsbnVsbCxudWxsLFtbWyIvbS8wN2MxdiJdXSxudWxsLDhdLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLFtdXQ==; track:vis ; index:4'})
        category_name = category.find("div", {'class': 'cp7Yvc'}).h2.text
        category_url = category.find("div", {'class': "cp7Yvc"}).find("a").get("href")
        news = category.find_all("div", {'jscontroller': "MRcHif"})
        
        a = {"category": category_name, "url": urljoin(self.base_url, category_url), "stories": []}
        
        for new in news:
            image = new.find("div", {'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}).a.figure.img.get("src")
            title = new.find("article").h3.text
            # url = new.find("div", {'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}).a.get("href")
            url = new.find("article").h3.a.get("href")
            source = new.find("article").div.a.text
            time = new.find("article").div.time.text
            
            b = {"image": image, "title": title, "url": urljoin(self.base_url, url), "source": source, "time": time, "sub_stories": []}
            
            sub_stories = new.find("div", {"class": "SbNwzf eeoZZ"}).find_all("article")
            for story in sub_stories:
                title = story.h4.text
                url = story.a.get("href")
                source = story.div.a.text
                source_url = story.div.a.get("href")
                time = story.div.time.text
                
                c = {"title": title, "url": urljoin(self.base_url, url), "source": source, "source_url": source_url, "time": time}
            b["sub_stories"].append(c)
        a["stories"].append(b)
        return a


    def entertainment_news(self):
        category = self.soup.find('div', {'jslog': '127062; 3:W251bGwsbnVsbCxudWxsLG51bGwsInNlY3Rpb24tdG9waWMtbWlkOi9tLzAyamp0IixudWxsLDE0MSxudWxsLG51bGwsbnVsbCwzMDIsbnVsbCxudWxsLFtbWyIvbS8wMmpqdCJdXSxudWxsLDhdLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLFtdXQ==; track:vis ; index:5'})
        category_name = category.find("div", {'class': 'cp7Yvc'}).h2.text
        category_url = category.find("div", {'class': "cp7Yvc"}).find("a").get("href")
        news = category.find_all("div", {'jscontroller': "MRcHif"})
        
        a = {"category": category_name, "url": urljoin(self.base_url, category_url), "stories": []}
        
        for new in news:
            image = new.find("div", {'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}).a.figure.img.get("src")
            title = new.find("article").h3.text
            # url = new.find("div", {'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}).a.get("href")
            url = new.find("article").h3.a.get("href")
            source = new.find("article").div.a.text
            time = new.find("article").div.time.text
            
            b = {"image": image, "title": title, "url": urljoin(self.base_url, url), "source": source, "time": time, "sub_stories": []}
            
            sub_stories = new.find("div", {"class": "SbNwzf eeoZZ"}).find_all("article")
            for story in sub_stories:
                title = story.h4.text
                url = story.a.get("href")
                source = story.div.a.text
                source_url = story.div.a.get("href")
                time = story.div.time.text
                
                c = {"title": title, "url": urljoin(self.base_url, url), "source": source, "source_url": source_url, "time": time}
            b["sub_stories"].append(c)
        a["stories"].append(b)
        return a


    def sport_news(self):
        category = self.soup.find('div', {'jslog': '127062; 3:W251bGwsbnVsbCxudWxsLG51bGwsInNlY3Rpb24tdG9waWMtbWlkOi9tLzA2bnRqIixudWxsLDE0MSxudWxsLG51bGwsbnVsbCwzMDIsbnVsbCxudWxsLFtbWyIvbS8wNm50aiJdXSxudWxsLDhdLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLFtdXQ==; track:vis ; index:6'})
        category_name = category.find("div", {'class': 'cp7Yvc'}).h2.text
        category_url = category.find("div", {'class': "cp7Yvc"}).find("a").get("href")
        news = category.find_all("div", {'jscontroller': "MRcHif"})
        
        a = {"category": category_name, "url": urljoin(self.base_url, category_url), "stories": []}
        
        for new in news:
            image = new.find("div", {'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}).a.figure.img.get("src")
            title = new.find("article").h3.text
            # url = new.find("div", {'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}).a.get("href")
            url = new.find("article").h3.a.get("href")
            source = new.find("article").div.a.text
            time = new.find("article").div.time.text
            
            b = {"image": image, "title": title, "url": urljoin(self.base_url, url), "source": source, "time": time, "sub_stories": []}
            
            sub_stories = new.find("div", {"class": "SbNwzf eeoZZ"}).find_all("article")
            for story in sub_stories:
                title = story.h4.text
                url = story.a.get("href")
                source = story.div.a.text
                source_url = story.div.a.get("href")
                time = story.div.time.text
                
                c = {"title": title, "url": urljoin(self.base_url, url), "source": source, "source_url": source_url, "time": time}
            b["sub_stories"].append(c)
        a["stories"].append(b)
        return a


    def science_news(self):
        category = self.soup.find('div', {'jslog': '127062; 3:W251bGwsbnVsbCxudWxsLG51bGwsInNlY3Rpb24tdG9waWMtbWlkOi9tLzA2bXE3IixudWxsLDE0MSxudWxsLG51bGwsbnVsbCwzMDIsbnVsbCxudWxsLFtbWyIvbS8wNm1xNyJdXSxudWxsLDhdLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLFtdXQ==; track:vis ; index:7'})
        category_name = category.find("div", {'class': 'cp7Yvc'}).h2.text
        category_url = category.find("div", {'class': "cp7Yvc"}).find("a").get("href")
        news = category.find_all("div", {'jscontroller': "MRcHif"})
        
        a = {"category": category_name, "url": urljoin(self.base_url, category_url), "stories": []}
        
        for new in news:
            image = new.find("div", {'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}).a.figure.img.get("src")
            title = new.find("article").h3.text
            # url = new.find("div", {'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}).a.get("href")
            url = new.find("article").h3.a.get("href")
            source = new.find("article").div.a.text
            time = new.find("article").div.time.text
            
            b = {"image": image, "title": title, "url": urljoin(self.base_url, url), "source": source, "time": time, "sub_stories": []}
            
            sub_stories = new.find("div", {"class": "SbNwzf eeoZZ"}).find_all("article")
            for story in sub_stories:
                title = story.h4.text
                url = story.a.get("href")
                source = story.div.a.text
                source_url = story.div.a.get("href")
                time = story.div.time.text
                
                c = {"title": title, "url": urljoin(self.base_url, url), "source": source, "source_url": source_url, "time": time}
            b["sub_stories"].append(c)
        a["stories"].append(b)
        return a


    def health_news(self):
        category = self.soup.find('div', {'jslog': '127062; 3:W251bGwsbnVsbCxudWxsLG51bGwsInNlY3Rpb24tdG9waWMtbWlkOi9tLzBrdDUxIixudWxsLDE0MSxudWxsLG51bGwsbnVsbCwzMDIsbnVsbCxudWxsLFtbWyIvbS8wa3Q1MSJdXSxudWxsLDhdLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLFtdXQ==; track:vis ; index:8'})
        category_name = category.find("div", {'class': 'cp7Yvc'}).h2.text
        category_url = category.find("div", {'class': "cp7Yvc"}).find("a").get("href")
        news = category.find_all("div", {'jscontroller': "MRcHif"})
        
        a = {"category": category_name, "url": urljoin(self.base_url, category_url), "stories": []}
        
        for new in news:
            image = new.find("div", {'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}).a.figure.img.get("src")
            title = new.find("article").h3.text
            # url = new.find("div", {'xrnccd F6Welf R7GTQ keNKEd j7vNaf'}).a.get("href")
            url = new.find("article").h3.a.get("href")
            source = new.find("article").div.a.text
            time = new.find("article").div.time.text
            
            b = {"image": image, "title": title, "url": urljoin(self.base_url, url), "source": source, "time": time, "sub_stories": []}
            
            sub_stories = new.find("div", {"class": "SbNwzf eeoZZ"}).find_all("article")
            for story in sub_stories:
                title = story.h4.text
                url = story.a.get("href")
                source = story.div.a.text
                source_url = story.div.a.get("href")
                time = story.div.time.text
                
                c = {"title": title, "url": urljoin(self.base_url, url), "source": source, "source_url": source_url, "time": time}
            b["sub_stories"].append(c)
        a["stories"].append(b)
        return a
    
    
    def all_news(self):
        all = []
        all.append(self.headline_news())
        all.append(self.nigeria_news())
        all.append(self.world_news())
        all.append(self.business_news())
        all.append(self.technology_news())
        all.append(self.entertainment_news())
        all.append(self.sport_news())
        all.append(self.science_news())
        all.append(self.health_news())
        return all


c = Scraper()
# news = c.all_news()
world = c.nigeria_news()
print(world)