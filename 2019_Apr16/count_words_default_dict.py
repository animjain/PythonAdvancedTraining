def count_words(line):
    count = defaultdict(int)
    for word in line.split():
        count[word] += 1

    for w, c in count.items():
        print(f"'{w}' occurs {c} times")

