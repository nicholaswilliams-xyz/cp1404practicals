"""
Print the number of occurrences of each word in a string.
Estimated completion time: 30m
Actual completion time: 37m 20s
"""

text_string = sorted(input("Type a string of words: ").lower().split())

occurrences = [text_string.count(i) for i in text_string]

WORD_TO_COUNT = dict(zip(text_string, occurrences))
left_align = len(max(WORD_TO_COUNT, key=len))

for word, occurrences in WORD_TO_COUNT.items():
    print(f"{word:<{left_align + 1}}: {occurrences}")
