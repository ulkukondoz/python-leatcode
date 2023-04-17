
 #  isAnagram("Steer", Set.of("Trees")) ==> true
 #  isAnagram("Steer", Set.of("Street")) ==> false
 #  isAnagram("Steer", Set.of("Trees", "Street", "Aardvark")) == true
 #  isAnagram("Stress", Set.of("Trees", "Street", "Aardvark")) == false
 #  Java 8 or lower which codility appears to be
 #  isAnagram("Steer", new HashSet(Arrays.asList("Trees")) == true
 #  isAnagram("Steer", new HashSet(Arrays.asList("Street")) == false
 #  isAnagram("Steer", new HashSet(Arrays.asList("Trees", "Street", "Aardvark")) == true
 #  isAnagram("Stress", new HashSet(Arrays.asList("Trees", "Street", "Aardvark"))) == false

def is_anagram(word, word_set):

    for string in word_set:
        chars_dict = convert_to_chars(word)

        for char in string.lower():
            if char in chars_dict:
                counter = chars_dict[char] - 1
                if counter == 0:
                    del chars_dict[char]
                else:
                    chars_dict[char] = counter
            else:
                continue

        return True if len(chars_dict) == 0 else False

def convert_to_chars(word):
     chars_dict = {}

     for letter in word.lower():
         if letter in chars_dict:
             counter = chars_dict[letter]
             chars_dict[letter] = counter + 1
         else:
             chars_dict[letter] = 1
     return chars_dict


print(is_anagram("Trees", {"Trees", "Street", "Aardvark"}))
print(is_anagram("Stress", {"Trees", "Street", "Aardvark"}))
print(is_anagram("Steer", {"Trees", "Street", "Aardvark"}))
