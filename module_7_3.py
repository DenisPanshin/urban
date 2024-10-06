class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = []
        for i in file_names:
            self.file_names.append(i)

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                for j in file:
                    for k in j.split():
                        all_words.setdefault(i, []).append(k.lower().strip(',.=!?;:-'))

        return all_words

    def find(self, word):
        my_dict = {}
        for name, words in self.get_all_words().items():
            for j in range(len(words)):
                if word.lower() == words[j]:
                    my_dict.update({name: j + 1})
                    break
        return my_dict

    def count(self, word):
        my_dict = {}
        num = 0
        for name, words in self.get_all_words().items():
            for j in range(len(words)):
                if word.lower() == words[j]:
                    num += 1
            my_dict.update({name: num})

        return my_dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
