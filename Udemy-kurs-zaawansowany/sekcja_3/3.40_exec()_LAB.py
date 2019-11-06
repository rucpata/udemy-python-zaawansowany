files_to_process = [r'Users/wlasciciel/Desktop/programowanie/udemy/python/python_zaawansowany/Udemy-kurs-zaawansowany/sekcja_3/math_sin_quare.py',
                    r'Users/wlasciciel/Desktop/programowanie/udemy/python/python_zaawansowany/Udemy-kurs-zaawansowany/sekcja_3/math_square_root.py'
                    ]

for file_path in files_to_process:
    with open(file_path, 'r') as f:
        print('File {} ...'.format(file_path))
        source = f.read()
        exec(source)