import unittest

def reverse_characters(message, start, end):

    # Decode the message by reversing the words
    #start, end = 0, len(message)-1
    while start < end:
        message[start], message[end] = message[end], message[start]
        start += 1
        end -= 1
        
    #print("".join(message))


def reverse_words(message):
    
    reverse_characters(message, 0, len(message)-1)
    
    current_word_start_index = 0

    for i in range(len(message)+1):
        if (i==len(message)) or (message[i] == ' '):
            reverse_characters(message, current_word_start_index, i-1)
            current_word_start_index = i +1
        
    print("".join(message))



# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)
