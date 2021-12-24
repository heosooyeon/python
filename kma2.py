from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

# 웹 서버를 생성합니다.
app = Flask(__name__)
@app.route("/")

def kma1():
    target = request.urlopen("https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=159")

      # BeautifulSoup을 사용해 웹 페이지를 분석합니다.
    soup = BeautifulSoup(target, "html.parser")
    
    output = ""

    for item in soup.select("item"):
        output += "<h2>{}</h2><hr/>".format(item.select_one("title").string)
 
    # location 태그를 찾습니다.
    for location in soup.select("location"):
        # 내부의 city, wf, tmn, tmx, tmEf 태그를 찾아 출력합니다.
        output += "도시: {}</br>".format(location.select_one("city").string)
        output += "날씨: {}</br>". format(location.select_one("wf").string)
        output += "최저기온: {}</br>". format(location.select_one("tmn").string)
        output += "최고기온: {}</br>". format(location.select_one("tmx").string)
        output += "<hr>"
 
    # 제목, 날짜, 지역, 세부정보 출력
    output += "{}</br>".format(soup.select_one("title").string)
    output += "날짜: {}</br>".format(location.select_one("tmEf").string)
    output += "지역: {}</br>".format(soup.select_one("province").string)

    return output

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)







    