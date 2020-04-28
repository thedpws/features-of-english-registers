from nltk.corpus import brown
import nltk
import re
import random
import requests
import time

nltk.download('brown')

keywords = [w.lower() for w in brown.words(categories='learned') if re.fullmatch('\\w{8,}', w)]

def get_academic_articles(N=10):
    def get_article_summaries(keyword, max_results):
        url = f'http://export.arxiv.org/api/query?search_query=all:{keyword}&id_list=&start=0&max_results={max_results}'
        raw_response = requests.get(url).content.decode()
        time.sleep(0.25)
        # Find all summary content
        re_summary = re.compile('<summary>(.*?)</summary>', flags=re.DOTALL)
        matches = re_summary.findall(raw_response)

        # Standardize whitespace
        clean_matches = [re.sub('\\s+',' ',match) for match in matches]
        return clean_matches

    # Aggregate articles
    academic_articles = []

    # Avoid duplicating articles already seeen
    seen_articles = set()

    # Keep querying until we have N articles
    n = 0
    while n < N:
        keyword = random.choice(keywords)
        max_results = min(100, N-n)
        summaries = set(get_article_summaries(keyword=keyword, max_results=max_results)) - seen_articles

        seen_articles.update(summaries)

        academic_articles.extend(summaries)
    
        n += len(summaries)
        print(f'{n}/{N} articles downloaded')

    return academic_articles