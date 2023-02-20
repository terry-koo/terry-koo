import feedparser, time

URL="https://terrypotter.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST=7

markdown_text = """
![header](https://capsule-render.vercel.app/api?type=slice&color=auto&height=180&section=header&text=Terry&desc=iOS%20Developer&fontSize=90&rotate=13&fontAlignY=15&fontAlign=75&descAlignY=34&descAlign=72.5&&animation=twinkling)

# 👋 Hi, I'm Bonsung Koo 

![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=terry-koo&show_icons=true&theme=radical&hide=stars)

## 😆 Get in touch
[![Gmail Badge](https://img.shields.io/badge/-Gmail-d14836?style=flat-square&logo=Gmail&logoColor=white&link=mailto:devterrykoo@gmail.com)](mailto:devterrykoo@gmail.com)
[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/terry-koo/)](https://www.linkedin.com/in/terry-koo/)

## ✍ Recent blog posts 
""" # list of blog posts will be appended here


for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
