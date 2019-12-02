import requests
import os
import functools


def save_url_file(url, dir, file, msg):
    print(msg.format(file))

    r = requests.get(url, stream=True)
    file_path = os.path.join(dir, file)

    with open(file_path, "wb") as f:
        f.write(r.content)

save_url_to_dir = functools.partial(save_url_file, dir='Users/wlasciciel/Desktop/programowanie/udemy/python/python_zaawansowany/Udemy-kurs-zaawansowany/sekcja_5/',
                                    msg = 'Please wait {}')
url = 'http://mobilo24.eu/spis'
file = 'spis.html'
save_url_to_dir = functools.partial(save_url_file, dir='Users/wlasciciel/Desktop/programowanie/udemy/python/python_zaawansowany/Udemy-kurs-zaawansowany/sekcja_5/',
                                    msg = 'Please wait {}')
save_url_to_dir(url = url, file = file)

save_url_to_dir = functools.partial(save_url_file, url, msg = 'Please wait {}')
dir = 'Users/wlasciciel/Desktop/programowanie/udemy/python/python_zaawansowany/Udemy-kurs-zaawansowany/sekcja_5/'
file = 'logo.png'
save_url_to_dir(url = url, file = file)

