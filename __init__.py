# -*- coding: utf-8 -*-
# Version: 2.1
# See github page to report issues or contribute:
# https://github.com/hssm/anki-ignore-accents

from aqt import gui_hooks
from aqt.browser import SearchContext
import shlex

def willSearch(ctx: SearchContext):
    terms = shlex.split(ctx.search)
    processed = []
    for term in terms:
        if ':' in term:
            processed.append(term)
        else:
            processed.append("nc:" + term)
    ctx.search = ' '.join('"{0}"'.format(t) for t in processed)
    return ''

gui_hooks.browser_will_search.append(willSearch)