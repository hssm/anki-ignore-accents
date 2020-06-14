# -*- coding: utf-8 -*-
# Version: 2.0
# See github page to report issues or contribute:
# https://github.com/hssm/anki-ignore-accents

from aqt import gui_hooks
from aqt.browser import SearchContext

def willSearch(ctx: SearchContext):
    terms = ctx.search.split()
    processed = []
    for term in terms:
        if ':' in term:
            processed.append(term)
        else:
            processed.append("nc:" + term)
    ctx.search = ' '.join(processed)
    return ''

gui_hooks.browser_will_search.append(willSearch)