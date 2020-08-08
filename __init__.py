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
    negated = []
    for term in terms:
        if term[0] == "-":
            term = term[1:]
            negated.append(term)
            continue
        if ':' in term:
            processed.append(term)
        else:
            processed.append("nc:" + term)
    ctx.search = ' '.join('"{0}"'.format(t) for t in processed)
    ctx.search += ' '
    ctx.search += ' '.join('-"{0}"'.format(t) for t in negated)
    print(ctx.search)
    return ''

gui_hooks.browser_will_search.append(willSearch)