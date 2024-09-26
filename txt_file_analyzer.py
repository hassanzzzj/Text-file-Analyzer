from collections import Counter
import re

def analyze_text_file(file_path):
    # Initialize counters
    line_count = 0
    word_count = 0
    word_frequency = Counter()

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:

            line_count += 1
            
            words = re.findall(r'\b\w+\b', line.lower())
            word_count += len(words)
            
            word_frequency.update(words)

    most_common_words = word_frequency.most_common(10) 

    print(f"Total Lines: {line_count}")
    print(f"Total Words: {word_count}")
    print("Most Frequent Words:")
    for word, count in most_common_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    # replace the name of file with explain.txt to run this code successfully
    file_path = 'explain.txt'  
    analyze_text_file(file_path)