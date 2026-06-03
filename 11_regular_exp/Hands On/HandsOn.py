"""Basic regex basics under 40 lines."""

import re

text = 'Contact alice@example.com or call 123-456-7890.'


def main():
    print('search email:', re.search(r'[\w.-]+@[\w.-]+', text).group(0))
    print('all emails:', re.findall(r'[\w.-]+@[\w.-]+', text))
    print('match start:', bool(re.match(r'Contact', text)))
    print('phone parts:', re.search(r'(\d{3})-(\d{3})-(\d{4})', text).groups())
    print('mask:', re.sub(r'([\w.-]+)@([\w.-]+)', r'\1@hidden', text))
    print('words:', re.split(r'\s+', text))
    print('valid email:', bool(re.fullmatch(r'[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}', 'alice@example.com')))
    print('capital words:', re.findall(r'\b[A-Z][a-z]*\b', 'Python Regex Is Useful'))
    print('dates:', re.findall(r'(\d{4})-(\d{2})-(\d{2})', '2026-06-01, 2026-07-10'))


if __name__ == '__main__':
    main()
