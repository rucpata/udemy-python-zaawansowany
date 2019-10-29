import os

def CountWords(path):
    with open(path, 'r') as f:
        content = f.read()
        word_count = len(content.split())
    return word_count

path = r'/Users/wlasciciel/Desktop/programowanie/udemy/python/Python dla średnio zaawansowanych/mydata.txt'
if os.path.isfile(path):
    print('The are {} words in the file {}'.format(CountWords(path), path))
os.path.isfile(path) and print('There are {} words in the file {}'.format(CountWords(path), path))


