from collections import defaultdict

def top_ten_words(file_path):
    word_count = defaultdict(int)

    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word_count[word.lower()] += 1

    sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)[:10]

    for word, count in sorted_words:
        print(f"{word}: {count}")

top_ten_words(r'03-python/question-3/sample.txt')
