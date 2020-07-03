import requests
import bs4
import string


base_url = "https://www.austinpetsalive.org/adopt/dogs/p{}#puppers"


for d in range(1,10):
    res = requests.get(base_url.format(d))
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    pound = str(soup.select('div.row.justify-center')[0])
    pound_count = pound.count('large-tile mr-auto ml-auto mb-50 relative')

    for p in range(0, pound_count):
        post = soup.select('div.large-tile.mr-auto.mb-50.relative')[p]
        post_pic = post.select('img')[0]
        pic = post_pic['src']
        image = requests.get(pic)
        post_name = post.select('a.orange')[0]
        name = post_name.text

        try:
            f = open(f"hotel_for_dogs/{name}.png", 'wb')
        except:
            f = open(f"hotel_for_dogs/pup{d*100 + p}.png", 'wb')
        f.write(image.content)
        f.close()