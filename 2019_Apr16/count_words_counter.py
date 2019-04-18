def count_words(line):
    from collections import Counter
    count = Counter()
    for word in line.split():
        count[word] += 1

    for w, c in count.items():
        print(f"'{w}' occurs {c} times")

