import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
matches = pattern.finditer(emails)

for match in matches:
    print(match)

# Output -
# <re.Match object; span=(1, 24), match='CoreyMSchafer@gmail.com'>
# <re.Match object; span=(25, 53), match='corey.schafer@university.edu'>
# <re.Match object; span=(54, 83), match='corey-321-schafer@my-work.net'>

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
sentence = 'Start a sentence and then bring it to an end'
pattern = re.compile(r'start', re.I)
matches = pattern.search(sentence)
print(matches)

# Output -
# <re.Match object; span=(0, 5), match='Start'>

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)

# Output -
# google.com
# coreyms.com
# youtube.com
# nasa.gov

matches = pattern.finditer(urls)
for match in matches:
    print(match.group(3))

# Output -
# .com
# .com
# .com
# .gov