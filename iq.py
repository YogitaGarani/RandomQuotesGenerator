# wrapper around gazpacho to get quotes from goodreads.com
# adapted by Yogita G - from quote module (open source)
# changed it to include a tag argument to construct a tag based url
# URL was hardcoded to a find URL in quote module
# now, if the tag passed is null, the find URL is used with str to search

import re
from typing import Dict, List, Optional

from gazpacho import Soup

find_URL = "https://www.goodreads.com/quotes/search"
tag_base_URL = "https://www.goodreads.com/quotes/tag/"

# modified to take in tag
# if url is null, then use hardcoded findURL defined above
# adapt parameters for the https request accordingly

def _make_soup(tag: str, query: str, page: int = 1) -> Soup:
    params = {"q": query, "commit": "Search", "page": page}
    if tag == "":
        soup = Soup.get(find_URL, params) 
    else:
        params = {"page": page}
        soup = Soup.get(tag_base_URL + tag, params)
    return soup


def _parse_quote(quote_text: Soup) -> Dict[str, str]:
    b = quote_text.find("a", {"class": "authorOrTitle"}, mode="first")
    a = quote_text.find("span", {"class": "authorOrTitle"}, mode="first")
    q = re.search("(?<=“)(.*?)(?=”)", quote_text.strip())
    return {
        "author": "" if not isinstance(a, Soup) else a.text.replace(",", ""),
        "book": "" if not isinstance(b, Soup) else b.text,
        "quote": "" if not q else q.group(0),
    }


def _get_page_quotes(soup: Soup) -> List[Dict[str, str]]:
    quotes = []
    quote_texts = soup.find("div", {"class": "quoteText"}, mode="all")
    assert isinstance(quote_texts, list)
    for quote_text in quote_texts:
        quote = _parse_quote(quote_text)
        quotes.append(quote)
    return quotes


def iq(tag: str, search: str, limit: int = 20) -> Optional[List[Dict[str, str]]]:
    """\
    Retrieve quotes from Goodreads

    Params:

    - tag: tag to use to get quotes, if not specified, use find_URL
    - search: Author and/or book
    - limit: Number of quotes to return

    Example:

    ```
    iq("", 'shakespeare', limit=2)
    iq("love", "", limit=2)

    # [{'author': 'William Shakespeare',
    # 'book': 'As You Like It',
    # 'quote': 'The fool doth think he is wise, but the wise man knows himself to be a fool.'},
    # {'author': 'William Shakespeare',
    # 'book': "All's Well That Ends Well",
    # 'quote': 'Love all, trust a few, do wrong to none.'}]
    ```
    """
    page = 1
    quotes: List[Dict[str, str]] = []
    while len(quotes) < limit:
        soup = _make_soup(tag, search, page=page)
        page_quotes = _get_page_quotes(soup)
        if not page_quotes:
            return None
        quotes.extend(page_quotes)
        if not soup.find("div", {"style": "float: right"}).text: # type: ignore
            break
        page += 1
    return quotes[:limit]
