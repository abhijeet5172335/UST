def count_frequency(line):
    words = dict()
    if isinstance(line, str):
        for i in line.split():
            if i in words.keys():
                words[i] += 1
            else:
                words[i] = 1
        return sorted(words.items())
    raise TypeError


# print(count_frequency("which is better python 2 or python 3"))
# print(count_frequency([]))
