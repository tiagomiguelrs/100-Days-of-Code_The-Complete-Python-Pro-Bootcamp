def loop(word, name, total):
    for l1 in word:
        counter = 0
        for l2 in name.upper():
            if l2 == l1:
                counter += 1
                total += 1
        if counter == 1:
            print(f"{l1} occurs {counter} time")
        else:
            print(f"{l1} occurs {counter} times")
    return total


def calculate_love_score(name1, name2):
    total1 = 0
    total2 = 0

    total1 = loop("TRUE", name1, total1)

    total1 = loop("LOVE", name1, total1)

    print(f"Total = {total1}")

    total2 = loop("TRUE", name2, total2)

    total2 = loop("LOVE", name2, total2)

    print(f"Total = {total2}")

    print(f"Love Score = {total1}{total2}")


calculate_love_score("Tiago", "Daniela")
