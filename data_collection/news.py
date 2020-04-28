import nltk
from nltk.corpus import reuters
nltk.download('reuters')
nltk.download('punkt')

def get_news_articles(N=10):
    # Get N articles
    news_article_fileids = [fileid for fileid in reuters.fileids()][:N]
    news_articles = list(map(' '.join, map(lambda x: x[0][0], map(reuters.paras, news_article_fileids))))

    return news_articles
