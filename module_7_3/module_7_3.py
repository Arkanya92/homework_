class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                stirings = file.read().lower()
                for symbol in punctuation:
                    stirings = stirings.replace(symbol, '')
                words = stirings.split()
                all_words[file_name] = words

        return all_words

    def find(self, word):
        word = word.lower()
        result_find = {}
        for name, words in self.get_all_words().items():
            if word in words:
                result_find[name] = words.index(word) + 1
        return result_find

    def count(self, word):
        word = word.lower()
        result_count = {}
        for name, words in self.get_all_words().items():
            __count = 0
            for w in words:
                if word == w:
                    __count += 1
            result_count[name] = __count
        return result_count

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего