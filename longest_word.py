def longest_word(sen):
    for ch in sen:
        if not char.isalnum():
            sen = sen.replace(char, ' ')

    return max(sen.split(), key = len)


if __name__ == "__main__":
    sen1 = "fun&!! time"
    sen2 = "I love dogs"

    res1 = longest_word(sen1)
    print(res1)

    res2 = longest_word(sen2)
    print(res2)
