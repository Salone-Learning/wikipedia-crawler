from bs4 import BeautifulSoup
import requests
import time
import urllib

start_url = "https://en.wikipedia.org/wiki/Special:Random"
target_url = "https://en.wikipedia.org/wiki/Philosophy"

def find_first_link(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")

    # This div contains the article's body
    content_div = soup.find(id="mw-content-text").find(class_="mw-parser-output")

    article_link = None

    # Find all the direct children of content_div that are paragraphs
    for element in content_div.find_all("p", recursive=False):
        # Find the first anchor tag that's a direct child of a paragraph.
        anchor = element.find("a", recursive=False)
        if anchor
            article_link = anchor.get("href")
            break

    if not article_link:
        return

    # Build a full url from the relative article_link url
    first_link = urllib.parse.urljoin("https://en.wikipedia.org/", article_link)

    return first_link

def continue_crawl(search_history, target_url, max_steps=25):
    if search_history[-1] == target_url:
        return False
    elif len(search_history) > max_steps:
        return False
    elif search_history[-1] in search_history[:-1]:
        return False
    else:
        return True

article_chain = [start_url]

while continue_crawl(article_chain, target_url):
    print(article_chain[-1])

    first_link = find_first_link(article_chain[-1])
    if not first_link:
        print("We've arrived at an article with no links, aborting search!")
        break

    article_chain.append(first_link)

    # Sleep for 2 seconds before next loop so as to not hammer Wikipedia
    time.sleep(2)
