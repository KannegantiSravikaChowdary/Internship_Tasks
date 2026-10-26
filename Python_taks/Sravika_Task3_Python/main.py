from solutions import word_frequency 
s=word_frequency("python is easy and python is powerful")
print(s)

from solutions import character_freq 
s=character_freq("banana")
print(s)

from solutions import non_repeating 
w=non_repeating("swiss")
print(w)

from solutions import anagram
w=anagram("listen","silent")
print(w)

from solutions import repeating_char 
w=repeating_char("Programming")
print(w)

from solutions import zeroes_to_end
l=zeroes_to_end([0, 3, 0, 1, 2, 0, 4])
print(l)

from solutions import second_distinct 
h=second_distinct([10])
l=second_distinct([10, 20, 40, 30, 40, 20])
print(l)
print(h)

from solutions import unique 
l=unique([4, 2, 4, 5, 2, 7, 5])
print(l)

from solutions import missing_number
l=missing_number([1,2,4,5,6],6)
print(l)

from solutions import two_sum 
l=two_sum([2, 7, 11, 15],9)
print(l)

from solutions import closest_to_zero
l=closest_to_zero([-8, -3, 2, 5, -2])
print(l)

from solutions import common_elements
l=common_elements([ 3, 4, 5], [1,2,3])
print(l)

from solutions import rotate_right
l=rotate_right([1,2,3,4,5],2)
print(l)

from solutions import consecutive
print(consecutive([2, 7, 4, 9, 5]))


from solutions import find_pairs
l=find_pairs([2, 4, 3, 5, 7, 8, 1,3,6],9)
print(l)