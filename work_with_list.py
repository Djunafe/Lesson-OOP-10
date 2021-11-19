import shelve

filename = 'links'

with shelve.open(filename) as links:
    links['https://www.youtube.com/watch?v=PBvOtA7ZcNE'] = 'David Bowie - Greatest Hits'
    links['https://www.youtube.com/watch?v=5JjKm8DBq9U'] = 'Queen - Greatest Hits Full Album'
    links['https://www.youtube.com/watch?v=KCJuBpZusFE'] = 'Ballads - Greatest Hits'


def work_with_list():
    question_1 = input('Do you want to add your link or use links from an existing dictionary? ( add / use ) : ')
    if question_1 == 'add':
        add_to_list()
        more()
    elif question_1 == 'use':
        spec_or_full()
    else:
        print('Wrong command!')
        work_with_list()


def add_to_list():
    with shelve.open(filename) as link_s:
        a_key = input('Enter your link: ')
        a_value = input('Enter your short name for link: ')
        link_s[a_key] = a_value


def more():
    question_2 = input('Do you want to enter another one? ( yes / no ) : ')
    if question_2 == 'yes':
        add_to_list()
        more()
    elif question_2 == 'no':
        more_work()
    else:
        print('Wrong command!')
        more()


def more_work():
    question_5 = input('Do you want yo do anything else? ( yes / no ) : ')
    if question_5 == 'yes':
        work_with_list()
    elif question_5 == 'no':
        print('See you soon!')
    else:
        print('Wrong command!')
        more_work()


def spec_or_full():
    question_4 = input('Do you want to get specific or full information?  ( spec / full ) : ')
    if question_4 == 'spec':
        use_list()
    elif question_4 == 'full':
        full_info()
        more_work()
    else:
        print('Wrong command!')
        spec_or_full()


def full_info():
    with shelve.open(filename) as link_s:
        for singer in link_s.items():
            print(singer)


def use_list():
    question_3 = input('What do you want to get? ( link / short_name ) : ')
    if question_3 == 'link':
        enter_links()
        more_use_links()
    elif question_3 == 'short_name':
        short_name()
        more_use_short_name()
    else:
        print('Wrong command!')
        use_list()


def more_use_short_name():
    question_7 = input('Do you want to get more short names? ( yes / no ) : ')
    if question_7 == 'yes':
        short_name()
        more_use_short_name()
    elif question_7 == 'no':
        more_work()
    else:
        print('Wrong command!')
        more_use_short_name()


def more_use_links():
    question_6 = input('Do you want to get more links? ( yes/ no ) : ')
    if question_6 == 'yes':
        enter_links()
        more_use_links()
    elif question_6 == 'no':
        more_work()
    else:
        print('Wrong command!')
        more_use_links()


def short_name():
    with shelve.open(filename) as link_s:
        key_1 = input('Enter link of what short name do you want to get: ')
        if key_1 in link_s:
            print(link_s[key_1])
        else:
            print('Here is not any short name with this link!')
            short_name()


def enter_links():
    with shelve.open(filename) as link_s:
        value_1 = input('Enter short name of what link dp you want to get: ')
        if value_1 in link_s.values():
            print(list(link_s.keys())[list(link_s.values()).index(value_1)])
        else:
            print('Here is not any links with this short name!')
            enter_links()
