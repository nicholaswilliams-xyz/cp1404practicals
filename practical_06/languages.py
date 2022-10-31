"""

Start date: 31.10.2022
Start time: 18:45
Estimated completion time: 30 minutes
Actual completion time:
"""

from programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)

programming_languages = [python, ruby, visual_basic]

print("The dynamically typed languages are:")
for language in programming_languages:
    if language.is_dynamic():
        print(language.name)
