import os
import urllib.request

data_dir = '/Users/wlasciciel/Desktop/cwiczenia_udemy'
pages = [
    {'name' : 'mobilo', 'url' : 'http://www.mobilo24.eu/'},
    {'name' : 'nonexistent', 'url' : 'http://abc.cde.fgh.ijk.pl/' },
    {'name' : 'kursy', 'url' : 'http://www.kursyonline24.eu/'}]

for page in pages:
    try:
        file_name = '{}.html'.format(page['name'])
        path = os.path.join(data_dir, file_name)

        print('Processing: {} => {}...'.format(page['url'], file_name))

        urllib.request.urlretrieve(page['url'], path)
        print('...dome')

    except:
        print('FAILURE processing web page: {}'.format(page['name']))
        print('Stopping the process!')
        break

else:
    print('All pages downloaded successfully!')