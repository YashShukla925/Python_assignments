# -*- coding: utf-8 -*-
# Regular Expression Assignment

import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


print("1. Extract Email Addresses")
text = "Contact us at support@test.com or admin123@gmail.com"
email_pattern = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"
emails = re.findall(email_pattern, text)
print(emails)


print("\n2. Validate Password")
passwords = ["Password@123", "password123"]
password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^a-zA-Z0-9]).{8,}$"

for password in passwords:
    if re.fullmatch(password_pattern, password):
        print(password, "# Valid")
    else:
        print(password, "# Invalid")


print("\n3. Extract Dates")
date_text = "Meeting on 12-05-2026 and another on 2026-06-01. Review on 15/07/2026"
date_pattern = r"\b(?:\d{2}[-/]\d{2}[-/]\d{4}|\d{4}-\d{2}-\d{2})\b"
dates = re.findall(date_pattern, date_text)
print(dates)


print("\n4. Find Duplicate Words")
duplicate_text = "This is is a sample sample text."
duplicate_pattern = r"\b(\w+)\s+\1\b"
duplicate_words = re.findall(duplicate_pattern, duplicate_text, flags=re.IGNORECASE)
print(duplicate_words)


print("\n5. Convert Multiple Spaces to One")
space_text = "Hello     World\t\tPython"
single_space_text = re.sub(r"\s+", " ", space_text).strip()
print(single_space_text)


print("\n6. Log File Parser")
log_entries = """2026-06-01 10:23:45 ERROR Database connection failed
2026-06-01 10:24:12 INFO User login successful"""
log_pattern = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+(\w+)\s+(.+)$"
parsed_logs = []

for line in log_entries.splitlines():
    match = re.match(log_pattern, line)
    if match:
        parsed_logs.append({
            "timestamp": match.group(1),
            "level": match.group(2),
            "message": match.group(3)
        })

print(parsed_logs)


print("\n7. Extract HTML Tags")
html_text = '<div>Hello</div>\n<p>World</p>\n<a href="#">Link</a>Give feedback'
tag_pattern = r"<\s*([a-zA-Z][a-zA-Z0-9]*)\b[^>]*>"
tags = re.findall(tag_pattern, html_text)
print(tags)


print("\n8. Extract Currency Values")
currency_text = "Revenue was $1,200.50, profit ₹50,000 and loss €300"
currency_pattern = r"[$₹€]\d{1,3}(?:,\d{3})*(?:\.\d+)?|[$₹€]\d+(?:\.\d+)?"
currency_values = re.findall(currency_pattern, currency_text)
print(currency_values)

