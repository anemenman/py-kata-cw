"""
Generate user links

Generate user links
Your task is to create userlinks for the url, you will be given a username and must return a valid link.

Example
generate_link('matt c')
http://www.codewars.com/users/matt%20c
"""
import urllib.parse


def generate_link(username):
    return f'http://www.codewars.com/users/{urllib.parse.quote(username)}'


assert generate_link('matt c') == 'http://www.codewars.com/users/matt%20c'
assert generate_link('g964') == 'http://www.codewars.com/users/g964'
assert generate_link('GiacomoSorbi') == 'http://www.codewars.com/users/GiacomoSorbi'
assert generate_link('ZozoFouchtra') == 'http://www.codewars.com/users/ZozoFouchtra'
assert generate_link('colbydauph') == 'http://www.codewars.com/users/colbydauph'
