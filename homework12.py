import os
cwd = os.getcwd()
my_homework = os.path.join(cwd, "test.txt")


def amount_of_digits(file_name):
    text_list = []
    with open(file_name, "r") as me:
        line = 1
        for i in me.readlines():
            count = 0
            for e in i:
                if e.isdigit():
                    count += 1
            text_list.append(f"In line {line} you have {count} digits")
            line += 1
    return text_list


print(amount_of_digits(my_homework))


def unique_digit_counter(file_name):
    text_list = []
    with open(file_name, "r") as me:
        for i in me.readlines():
            for e in i:
                if e.isdigit():
                    if e not in text_list:
                        text_list.append(e)
    return len(text_list)


print(unique_digit_counter(my_homework))


def special_word(file_name):
    res = []
    with open(file_name, "r") as we:
        for i in we.readlines():
            us = i.split()
            for e in us:
                if e.startswith("<<") and e.endswith(">>"):
                    res.append(e)
    return res


def file_without_digits(file_name):
    res = []
    with open(file_name, "r") as can:
        for i in can.readlines():
            list_1 =[]
            for e in i:
                if not e.isdigit():
                    list_1.append(e)
            res.append("".join(list_1))
    with open("without_digits.txt", "w") as our:
        for i in res:
            our.write(" ".join(i.split()) + "\n")


file_without_digits(my_homework)
print(special_word(my_homework))
print(unique_digit_counter(my_homework))

