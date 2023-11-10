import feedparser, time

URL="https://terrypotter.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = """
![header](https://capsule-render.vercel.app/api?type=slice&color=auto&height=180&section=header&text=Terry&desc=iOS%20Developer&fontSize=90&rotate=13&fontAlignY=15&fontAlign=75&descAlignY=34&descAlign=73&&animation=twinkling)

# 👋 Hi, I'm Bonsung Koo 
 
    만나서 반갑습니다!

    - 기술적으로 깊게 파고들어 탐구하는 것을 즐깁니다.

    - 팀원들과 함께 성장하며 얻는 가치를 중요하게 생각합니다.

    - 다양한 사람들과의 커뮤니케이션을 통해 성장하는 것을 좋아합니다.

## 📚 Career

- Apple Developer Academy @ POSTECH 1기

- WWDC22 Challenge Winner (애플 장학생)



<!-- ![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=terry-koo&show_icons=true&theme=radical&hide=stars) -->

## 💎 Tech Stack

**Language**

![Swift](https://img.shields.io/badge/swift-F05138?style=for-the-badge&logo=swift&logoColor=white)
![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=java&logoColor=white)

**Framework**

<img src="https://img.shields.io/badge/SwiftUI-F05138?style=for-the-badge&logo=Swift&logoColor=white"/> <img src="https://img.shields.io/badge/UIKit-F05138?style=for-the-badge&logo=Swift&logoColor=white"/>



## 📫 Social
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white&link=mailto:devterrykoo@gmail.com)](mailto:devterrykoo@gmail.com)
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white&link=https://www.linkedin.com/in/terry-koo/)](https://www.linkedin.com/in/terry-koo/)
[![Tistory](https://img.shields.io/badge/Tistory-000000?style=for-the-badge&logo=TVTime&logoColor=white&link=https://terrypotter.tistory.com/)](https://terrypotter.tistory.com/)



## ✍ Recent blog posts 
""" # list of blog posts will be appended here


for idx, feed in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
