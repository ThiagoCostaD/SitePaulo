# from inspect import signature
from random import randint

from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')
# print(signature(fake.random_number))


def make_pericia():
    return {
        'id': fake.random_number(digits=2, fix_len=True),
        'titulo': fake.sentence(nb_words=6),
        'descricao': fake.sentence(nb_words=77),

        'img': {
            'url': 'https://loremflickr.com/%s/%s/work,office' % rand_ratio(),
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_pericia())
