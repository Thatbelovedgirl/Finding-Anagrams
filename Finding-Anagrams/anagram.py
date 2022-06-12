 # Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True



def is_anagram(s1,s2):
    if (sorted(s1)==sorted(s2)):
        print(sorted(s1),(s2))
        return True
    else:
        return False

print(is_anagram("mean","name"))

