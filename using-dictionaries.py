#!/usr/bin/env python3

emails = {}

assert emails == {}, f"Expected email to be {{}} but got: {repr(emails)}"

emails['ashley'] = 'ashley@example.com'
emails['craig'] = 'craig@example.com'
emails['elizabeth'] = 'elizabeth@example.com'

assert emails == {'ashley':'ashley@example.com','craig':'craig@example.com','elizabeth':'elizabeth@example.com'}, f"Expected emails to be {{'ashley':'ashley@example.com','craig':'craig@example.com','elizabeth':'elizabeth@example.com'}} but got: {repr(emails)}"

del emails['craig']
emails['dalton'] = 'dalton@example.com'

assert emails == {'ashley':'ashley@example.com','elizabeth':'elizabeth@example.com','dalton':'dalton@example.com'}, f"Expected emails to be {{'ashley':'ashley@example.com','elizabeth':'elizabeth@example.com','dalton':'dalton@example.com'}} but got: {repr(emails)}"

users = list(emails.keys())

assert users == ['ashley', 'elizabeth', 'dalton'], f"Expected users to be ['ashley', 'elizabeth', 'dalton'] but got: {repr(users)}"


email_list = list(emails.values())

assert email_list == ['ashley@example.com','elizabeth@example.com','dalton@example.com'], f"Expected emails to be ['ashley@example.com','elizabeth@example.com','dalton@example.com'], but got: {repr(email_list)}"

#pairs = [()]
pairs = list(emails.items())

assert pairs == [('ashley','ashley@example.com'),('elizabeth','elizabeth@example.com'),('dalton','dalton@example.com')], f"Expected emails to be [('ashley','ashley@example.com'),('elizabeth','elizabeth@example.com'),('dalton','dalton@example.com')] but got: {repr(pairs)}"






exit()
