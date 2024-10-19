def anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)
string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")
if anagrams(string1, string2):
    print("Строки являются анаграммами.")
else:
    print("Строки не являются анаграммами.")
