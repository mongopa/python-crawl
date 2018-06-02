from selenium import webdriver
import pandas

browser = webdriver.Chrome(executable_path='c:/chromedriver/chromedriver.exe')
df = pandas.read_csv('init.csv', index_col=0)
url = "http://www.watanabepro.co.jp/artist/500/"

POSTS = "li.ArtistList-01.clearfix"
ACTOR_NAME = ".ArtistProf" #女優名
IMAGE = ".ArtistThumb img" #サムネイル画像のURL、srcで画像ファイルを取得できる

"""***************************************
実行部分
***************************************"""

browser.get(url)

while True: #continue until getting the last page

       print("Starting to get posts...")
       posts = browser.find_elements_by_css_selector(POSTS) #ページ内のタイトル複数
       print (len(posts))
       for post in posts:
           try:
               name = post.find_element_by_css_selector(ACTRESS_NAME).text
               print(name)
               thumnailURL = post.find_element_by_css_selector(IMAGE).get_attribute("src")
               print(thumnailURL)
               se = pandas.Series([name,thumnailURL],["name", "image"])
               df = df.append(se, ignore_index=True)
           except Exception as e:
               print(e)
       break
#6
print("Finished Scraping. Writing CSV.......")
df.to_csv("outman.csv",encoding="Shift_JIS")
print("DONE")
