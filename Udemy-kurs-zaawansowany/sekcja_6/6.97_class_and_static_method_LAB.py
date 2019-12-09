'''Jeśli f to uchwyt do pliku, a obj to jakiś obiekt, to możesz go zapisać na dysku poleceniem:
pickle.dump(obj, f)
A jeśli potem ten obiekt chcesz odczytać, to możesz to zrobić tak:
new_obj = pickle.load(f)
'''
import pickle
import glob


class Cake:

    know_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):
        self.name = name
        if kind in self.know_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print('>>>>>>Text can be set only for cake ({})'.format(name))

    def showInfo(self):
        print('{}'.format(self.name).upper())
        print('Taste: {}'.format(self.taste))
        if len(self.additives) > 0:
            print('Additives:')
            for a in self.additives:
                print('\t{}'.format(a))
        if len(self.filling) > 0:
            print('Filling: {}'.format(self.filling))
        print('Gluten: free: {}'.format(self.__gluten_free))
        print('-' * 20)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)

    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>>>Text can be only for cake ({})'.format(self.name))

    Text = property(__get_text, __set_text, None, 'Text on tje cake')

    def save_to_file(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        with open(path, 'rb') as f:
            new_cake = pickle.load(f)

        cls.bakery_offer.append(new_cake)
        return new_cake

    @staticmethod
    def get_bakery_files(catalog):
        return glob.glob(catalog+'/*.bakery')




cake_01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, 'Happy Birthday Margaret!')
cake_02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', True, '')
cake_03 = Cake('Super Sweet Maringue', 'maringue', 'very sweet', [], '', False, '')
cake_04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', True, 'Good Luck!')

cake_01.save_to_file('/Users/wlasciciel/Desktop/programowanie/udemy/python/python_zaawansowany/Udemy-kurs-zaawansowany/'
                     'sekcja_6/cake_01.bakery')
cake_01.save_to_file('/Users/wlasciciel/Desktop/programowanie/udemy/python/python_zaawansowany/Udemy-kurs-zaawansowany/'
                     'sekcja_6/cake_02.bakery')


cake_05 = Cake.read_from_file('/Users/wlasciciel/Desktop/programowanie/udemy/python/python_zaawansowany/Udemy-kurs-zaawansowany/'
                     'sekcja_6/cake_01.bakery')
cake_05.showInfo()
print(Cake.get_bakery_files('/Users/wlasciciel/Desktop/programowanie/udemy/python/python_zaawansowany/Udemy-kurs-zaawansowany/'
                     'sekcja_6/'))