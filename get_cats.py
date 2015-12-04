import urllib.request
import urllib.parse
import collections
import json
import random


Query = collections.namedtuple('Query', 'q key part')
Result = collections.namedtuple('Result', 'ids names')


KEY = open('credentials').read().strip()
HOST_URL = 'https://www.googleapis.com/youtube/v3/search?%s'


adverb = ['cute', 'fun', 'funny', 'stupid', 'vine',
          'hilarious', 'compilation', 'silly', 'cool',
          'ultimate', 'happy', 'must watch', 'wow', 'guilty',
          'singing']


def get_cat_query():
    substantiv = ['cats', 'kitten', 'cat', 'kittens']
    rnd = lambda x: random.randint(0, len(x)-1)
    return '%s %s' % (adverb[rnd(adverb)], substantiv[rnd(substantiv)])


def get_bird_query():
    substantiv = ['bird']
    rnd = lambda x: random.randint(0, len(x)-1)
    return '%s %s' % (adverb[rnd(adverb)], substantiv[rnd(substantiv)])


def make_query(q):
    return Query(q, KEY, 'id,snippet')


def make_result():
    return Result([], [])


def result_add_pair(result, id, name):
    result.ids.append(id)
    result.names.append(name)


def download_random_animal_list(animal):
    if animal == 'I<3Cats':
        query = make_query(get_cat_query())
    else:
        query = make_query(get_bird_query())
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    response = opener.open(HOST_URL % (urllib.parse.urlencode({
        'q' : query.q,
        'key' : query.key,
        'part' : query.part
    }),))
    
    result = json.loads(response.read().decode('utf-8'))
    videoids = [entry['id']['videoId'] for entry in result['items']]
    names = [entry['snippet']['title'] for entry in result['items']]

    result = make_result()
    for id, name in zip(videoids, names):
        result_add_pair(result, id, name)

    return result


def main():
    download_random_list()


if __name__ == '__main__':
    main()
