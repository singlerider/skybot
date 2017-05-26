import re

from util import hook, http


@hook.command('u')
@hook.command
def urban(inp):
    '''.u/.urban <phrase> -- looks up <phrase> on urbandictionary.com'''

    url = 'https://api.urbandictionary.com/v0/define?'
    page = http.get_json(url, term=inp, headers={'Referer': 'http://m.urbandictionary.com'})
    defs = page['list']

    if page['result_type'] == 'no_results':
        return 'not found.'

    out = defs[0]['word'] + ': ' + defs[0]['definition'].replace('\r\n', ' ')
    link = defs[0]['permalink']

    if len(out) > 400:
        out = out[:out.rfind(' ', 0, 400)] + '...'

    return out, link


# define plugin by GhettoWizard & Scaevolus
@hook.command('dictionary')
@hook.command
def define(inp):

    return urban(inp)


@hook.command('e')
@hook.command
def etymology(inp):
    ".e/.etymology <word> -- Retrieves the etymology of chosen word"

    url = 'http://www.etymonline.com/index.php'

    h = http.get_html(url, term=inp)

    etym = h.xpath('//dl')

    if not etym:
        return 'No etymology found for ' + inp

    etym = etym[0].text_content()

    etym = ' '.join(etym.split())

    if len(etym) > 400:
        etym = etym[:etym.rfind(' ', 0, 400)] + ' ...'

    return etym
