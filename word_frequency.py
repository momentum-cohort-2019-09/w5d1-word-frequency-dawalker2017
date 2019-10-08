import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def remove_stop_words(words): #creating a function that loops through the text and
                              # removes any word stated in the "STOP_WORDS" array above.

    filtered_words = [] # creating an array to hold the new text.
    for word in words: # using a for-in loop to loop through each word.
        if word not in STOP_WORDS: # "if (this word) is not in the 'STOP_WORDS'...
            filtered_words.append(word) # ...then add (this word) into the new array."

    return filtered_words # now return the new array of words NOT found in 'STOP_WORDS'.

def clean_word(word): # creating a function to correspond with 'cleaned_words()'
    word = word.strip(string.punctuation) 
    word = word.lower() # '.lower()' is a predetermined function in Python that,
                        # whatever is before it, will make all values lower-cased.

    if word[-2:] == "'s": 
    # wrote an 'if' statement stating that, starting at -2 in the string of characters, would snip off everything after -2.
        
        # Ex: [in a sting of characters, say "chamber's", 'c' would be (0) going
        # up to 's'(9), reversing this would cause 's' to be (0) coming
        # down to 'c' which would be (-9).]

        word = word[:-2] 

    return word

def clean_words(words): # creating a 'function' to sort through the words and 'cleans' them.
    
    cleaned_words = [] # creating and declaring an empty array to put the soon-to-be cleaned words in.
    
    for word in words: # using a for-in loop to go through each word.
        
        cleaned_words.append(clean_word(word)) # camelCase is to Javascript as underscore is to Python. 
            # Also '.append' adds a single item to the end of a list.
            # In this case, we are adding every word being 'cleaned' into the new list
            # being made in the new array. 
   
    return  cleaned_words # and after, returns the newly edited words and their array.
        # !! return must be inline with whatever started it,
        # !! otherwise it behaives unlike what you might want.

def calculate_word_freqs(words): # creating a function that tags each time a word is encountered.
    freqs = {} # created a new array.
    for word in words:
         freqs[word] = freqs.get(word, 0) + 1
    return freqs # return the new array.

def get_longest_word(words):
    return sorted(words, key=len, reverse=True)[0]

def print_word_freq(filename):
    """Read in `file` and print out the frequency of words in that file."""
    with open(filename) as file:
        text = file.read()
 
    words = text.split()

    words = clean_words(words)

    words = remove_stop_words(words)

    freqs = calculate_word_freqs(words)

    sorted_freqs = sorted(freqs.items(), key=lambda pair: pair[1], reverse=True)

    longest_word_len = len(get_longest_word(words))

    for word, freq in sorted_freqs[:10]:
        print (word.rjust(longest_word_len), "|", str(freq).ljust(3), "*" * freq)

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
