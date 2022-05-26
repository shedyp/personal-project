# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(str1, str2):
    # [assignment] Add your code here
    str1_list = list(str1)
    str1_list.sort()
    str2_list = list(str2)
    str2_list.sort()

    return (str1_list == str2_list)


print(find_anagrams('Hello', 'lloHer'))
