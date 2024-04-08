import requests
from bs4 import BeautifulSoup


def scrape_page(url):
    session = requests.Session()
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article', class_='widget-entry entry-large col-sm-6')
    article_data_list = []

    for article in articles:
        try:
            article_category = article.find('span', class_='entry-category').text
            article_date = article.find('span', class_='entry-date').text
            article_title = article.find('h3', class_='entry-title').text
            article_link = article.find('a')['href']
            article_author = article.find('div', class_='entry-author text-uppercase small').text
            article_content_short = article.find('div', class_='entry-content').text
            article_thumbnail_element = article.find('img')
            article_thumbnail_link = article_thumbnail_element['src'] if article_thumbnail_element else 'N/A'
            article_content_long_response = session.get(article_link)
            content_soup = BeautifulSoup(article_content_long_response.text, 'html.parser')
            article_long_content = content_soup.find('div', class_='entry-content').text

            article_data = {
                'category': article_category,
                'date': article_date,
                'title': article_title,
                'link': article_link,
                'author': article_author,
                'content_short': article_content_short,
                'thumbnail_link': article_thumbnail_link,
                'content_long': article_long_content
            }
            article_data_list.append(article_data)
        except Exception as e:
            print(f"Error scraping article: {e}")
            continue

    return article_data_list
