MailSnake 
=========
Python wrapper for MailChimp API 1.3

Usage
=====
    >>> from mailsnake import MailSnake 
    >>> ms = MailSnake('YOUR MAILCHIMP API KEY')
    >>> ms.ping()
    u "Everything's Chimpy!"

Note
====
API parameters must be passed by name. For example:
    >>> ms.listMemberInfo(id='YOUR LIST ID', email_address='name@email.com')

MailChimp API v1.3 documentation
================================
http://www.mailchimp.com/api/1.3/
