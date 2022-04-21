import requests
from bs4 import BeautifulSoup


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.op.gg/summoners/kr/%EC%98%81%ED%99%94%EB%8A%94%ED%98%BC%EC%98%81%EC%9D%B4%EC%A3%A0',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')


### 승패 ###
#__next > div.css-19ozhet.e1sjz9pt1 > div.css-1sq1kbv.e3mqlfu0 > ul > li:nth-child(1) > div > div.info > div.game-result
#__next > div.css-19ozhet.e1sjz9pt1 > div.css-1sq1kbv.e3mqlfu0 > ul > li:nth-child(2) > div > div.info > div.game-result

### kda ###
#__next > div.css-19ozhet.e1sjz9pt1 > div.css-1sq1kbv.e3mqlfu0 > ul > li:nth-child(1) > div > div.kda > div.k-d-a

### 플레이한 챔피언  ###
#__next > div.css-19ozhet.e1sjz9pt1 > div.css-1sq1kbv.e3mqlfu0 > ul > li:nth-child(1) > div > div.champion > div.name

### 게임을 한 시간 ###
#__next > div.css-19ozhet.e1sjz9pt1 > div.css-1sq1kbv.e3mqlfu0 > ul > li:nth-child(1) > div > div.info > div:nth-child(2) > div

games=soup.select("#__next > div.css-19ozhet.e1sjz9pt1 > div.css-1sq1kbv.e3mqlfu0 > ul > li")
result=[]
for i in range(20):
    winOrLose=games[i].select_one("div > div.info > div.game-result")
    kda=games[i].select_one("div > div.kda > div.k-d-a")
    champion=games[i].select_one("div > div.champion > div.name")
    when=games[i].select_one("div > div.info > div:nth-child(2) > div")
    #print(winOrLose.text)
    #print(playTime.text)
    #print(champion.text)
    #print(when.text)
    result.append([winOrLose.text, kda.text, champion.text, when.text]) # 플라스크 연결은 나중에 하자...
