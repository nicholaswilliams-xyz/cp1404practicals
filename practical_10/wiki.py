"""
Prompt user for page title or search phrase. Print summary of given page.
"""
import wikipedia


def main():
    search_phrase = get_search_phrase()
    while search_phrase != "":
        try:
            search_phrase_page = wikipedia.page(search_phrase)
            print(f"  Title: {search_phrase_page.title}")
            print(f"    URL: {search_phrase_page.url}")
            print(f"Summary: {wikipedia.summary(search_phrase)}")
        except wikipedia.exceptions.PageError:
            print(f"Page id {search_phrase} does not match any pages. Try another id!")
        print('')
        search_phrase = get_search_phrase()


def get_search_phrase():
    search_phrase = input("Enter search phrase or page title: ")
    return search_phrase


if __name__ == "__main__":
    main()
