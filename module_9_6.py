def all_variants(text):
    for i in text:
        yield i
    for j in range(len(text) - 1):
        yield text[j:j + 2]
    yield text


a = all_variants("abc")
for i in a:
    print(i)
