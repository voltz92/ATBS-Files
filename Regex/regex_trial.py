#! python3

# this programm will find all the australian phone numbers and email addresses present in the text copied to the clipboard
import re,pyperclip

text = pyperclip.paste()
phoneNum = re.compile(r'\+\d\d\s\d\s\d\d\d\d\s\d\d\d\d')   # setting up the phoneNumber pattern as +61 X XXXX XXXX
emailAdd = re.compile(r'[a-zA-z0-9.+_]+@[a-zA-Z0-9.+_]+') # setting up the email pattern as letters_or_numbers@lettersornumbers << not checking for a dot for the domain
numbers = phoneNum.findall(text)
emails = emailAdd.findall(text)

op = []

for number in numbers:
    op.append(number)
for email in emails:
    op.append(email)

pyperclip.copy(' \n '.join(op))
