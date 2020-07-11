import requests
import random
from books_and_chapters import books_and_chapters
from twitter_keys import twitter_keys
import twitter

#what should we call the Christian twitter bot?

def get_verse(book, chapter):
	print(f'requesting {book}:{chapter}...')
	r = requests.get(f'http://bible-api.com/{book}{chapter}')
	verses = r.json()['verses']
	verse_metadata = random.choice(verses)
	return f'{verse_metadata["book_name"]}:{verse_metadata["chapter"]}:{verse_metadata["verse"]} {verse_metadata["text"]}'

books = [k for k,v in books_and_chapters.items()]
random_book = random.choice(books)
random_book_chapters = books_and_chapters[random_book]
random_chapter = random.randint(1, random_book_chapters)

api = twitter.Api(consumer_key=twitter_keys['consumer_key'],
                  consumer_secret=twitter_keys['consumer_secret'],
                  access_token_key=twitter_keys['access_token_key'],
                  access_token_secret=twitter_keys['access_token_secret'],
                  input_encoding="UTF-8")

verse = get_verse(random_book, random_chapter)
print(f'tweeting {verse}...')
api.PostUpdate(verse)

