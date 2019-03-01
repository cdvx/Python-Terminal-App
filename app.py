"""Module for the python terminal app entry-point"""

# Default imports 
import  requests, json
from os import getenv

# Thir-party imports
import click

# constants
import constants as const


__author__="Cedric"

# NEWS_API_KEY = getenv("NEWS_API_KEY") or const.NEWS_API_KEY
NEWS_API_KEY = getenv("NEWS_API_KEY")
TOP_HEADLINES_URL = getenv("TOP_HEADLINES_URL") or const.TOP_HEADLINES_URL
EVERYTHING_URL = getenv("EVERYTHING_URL") or const.EVERYTHING_URL
SOURCES_URL = getenv("SOURCES_URL") or const.SOURCES_URL

headers = {
    'Content-Type': 'Application/JSON',
    'Authorization': NEWS_API_KEY
}

payload = {"q": "bitcoin"}


def organize_articles(response):
    display = []
    if response['status'] == 'ok' and response['totalResults']:
        articles = [
            article for article in response['articles']
        ]
        for article in articles:
            content = article['content']
            author = article['author']
            title = article['title']
            description = article['description']
            Id = articles.index(article) + 1
            display.append(f'\nArticle:{Id}\n\nTitle:{title}\n\nDescription:{description}\By:{author}\n\nBody:{content}')
    return display



top_headlines = requests.get(TOP_HEADLINES_URL, headers=headers, params=payload)
top_headlines = top_headlines.json()


@click.command()
@click.option("--news", "-n")
def start(news=None):
    articles = organize_articles(top_headlines)
    click.echo(click.style("\n\nHello, welcome to the News application 😊", bold=True, fg='yellow'))
    if news and news == "bitcoin":
        click.echo(click.style(f'\n\n The top {news} headlines from this week are -->', fg='green'))
        for article in articles:
            click.echo(click.style(f"\n {article} \n", bg='black'))
    elif news and news != "bitcon":
        click.echo(click.style(f'\n\n Sorry 🙁️, there are no headlines from this week for topic --> {news} ', fg='red'))
    else:
        if not news:
            click.echo(click.style("\n\nThank you!! and Goodbye 👋🏾", bold=True, fg='yellow'))



@click.command()
@click.argument("name")
@click.option("--greeting", "-g")
def greet(name, greeting=None):
    if greeting:
        click.echo(f"{greeting}, {name}")
    else:
        click.echo(f"Hello {name}, Hope you are doing fine today!")


if __name__ == "__main__":
    start()
    # greet()



# /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                        #   sources='bbc-news,the-verge',
                                        #   category='business',
                                        #   language='en',
                                        #   country='us'
                                        #   )

# /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2017-12-01',
#                                       to='2017-12-12',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)

# /v2/sources
# sources = newsapi.get_sources()



