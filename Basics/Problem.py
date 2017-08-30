# Use the count method to determine how many vowels are in the string prophecy. Store this count in the vowel_count variable. 
# Note: the vowels are a, e, i, o and u. 
# Hint: You may want to call the count method multiple times, and increment vowel_count multiple times.

prophecy = "And there shall in that time be rumours of things going astray, and there will be a great confusion as to where things really are, and nobody will really know where lieth those little things with the sort of raffia work base, that has an attachment…at this time, a friend shall lose his friends’s hammer and the young shall not know where lieth the things possessed by their fathers that their fathers put there only just the night before around eight o’clock…"

# Solution

vowel_count += prophecy.count('a')
vowel_count += prophecy.count('A')
vowel_count += prophecy.count('e')
vowel_count += prophecy.count('E')
vowel_count += prophecy.count('i')
vowel_count += prophecy.count('I')
vowel_count += prophecy.count('o')
vowel_count += prophecy.count('O')
vowel_count += prophecy.count('u')
vowel_count += prophecy.count('U')

'''
Another easier way is to convert the whole string into lower case so that we don't have to 
write code for counting upper case vowels. 
'''

vowel_count = 0
lower_prophecy = prophecy.lower()
vowel_count += lower_prophecy.count('a')
vowel_count += lower_prophecy.count('e')
vowel_count += lower_prophecy.count('i')
vowel_count += lower_prophecy.count('o')
vowel_count += lower_prophecy.count('u')
print(vowel_count)

'''
It's easy to check that I got the same result with my new, shorter version. 
There was nothing especially wrong with the first version, but it was only 
after I had written my first idea that I realised the efficiency I could make
in the second attempt. Getting started with a simple idea and then improving 
my work from there is a common pattern I use when programming, I recommend 
you try it too.
'''

