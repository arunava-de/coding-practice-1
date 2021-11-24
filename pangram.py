def is_pangram(sentence):
    seen = set()

    for s in sentence:
        seen.add(s)

    return len(seen)==26