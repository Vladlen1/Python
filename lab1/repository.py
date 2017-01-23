__author__ = 'vladbirukov'
import pickle
import re
def rep():
    repository = set()
    while True:
        input_world = raw_input('What do you want add, remove, find, load, save, grep?')
        if input_world == 'close': break
        elif input_world == 'add':
            word_add = raw_input('What do you want to add?')
            word_one = word_add.split(',')
            for i in word_one:
                if i.isdigit():
                    repository.add(int(i))
                else:
                    repository.add(i)
            print repository
        elif input_world == 'remove':
            word_remove = raw_input('What do you want to remove?')
            word_two = word_remove.split(',')
            for i in word_two:
                try:
                    if i.isdigit():
                        repository.remove(int(i))
                    else:
                        repository.remove(i)
                except:
                    print 'No this number or word'
            print repository
        elif input_world == 'find':
            word_find = raw_input('What do you want to find?')
            word_thri = word_find.split(',')
            for i in word_thri:
                if i.isdigit():
                    find = int(i)   # in
                else:
                    find = i
                for j in repository:
                    if find == j:
                        print 'Find:',find
        elif input_world == 'list':
            print repository
        elif input_world == 'save':
            file = open('prym', 'wb')
            pickle.dump(repository, file)
            file.close()
        elif input_world == 'load':
            file = open('prym')
            repository = pickle.load(file)
            file.close()
        elif input_world == 'grep':
            regexp_word = raw_input('What do you want to find regexp look/(.*)/(.*)/(.*)')
            res = re.match('/(.*)/(.*)/(.*)', regexp_word)
            res = res.group()
            for i in repository:
                for k in res:
                    if i == k:
                        print 'Find', k
        else:
            print 'Try again'