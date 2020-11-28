# anki-ignore-accents
Anki add-on that forces browser search to always ignore accents/diacritical marks. Compatible with **Anki 2.1.28** and newer.

![Ignore accents](https://raw.github.com/hssm/anki-ignore-accents/master/docs/example.png "Ignore accents in browser search")

Since version 2.1.24, Anki allows you to search in the browser while ignoring accents or diacritial marks by adding a marker to each word you want to search for: `nc:something`. This is not very intuitive for those who frequenty rely on this behavior or when multiple terms are included in the search.

This add-on will do the hard work for you and ensure every term in your search is automatically converted to `nc:myword` without you doing anything else. Once the add-on is installed, the behavior is always enabled and it will always modify your browser searches.

The add-on has no effect on any term that includes the `:` character as they are considered special Anki keywords. You **cannot** search for `field:myword`. Besides being difficult to implement, searching with `field:nc:myword` is not supported by Anki anyway.

Grouping, negation, and `and|or` keywords are safe to use normally; the add-on will find the right terms to annonate and preserve the quoting (previous versions stripped quoting).

My test string:

`"deck:Chinese::Let's learn words" black -(cat and ( mouse or carrot )) with "orange" -(dog or rabbit) is:new -house deck:"inner quotes test!"`

Produces this result:

`"deck:Chinese::Let's learn words" nc:black -(nc:cat and ( nc:mouse or nc:carrot )) nc:with "nc:orange" -(nc:dog or nc:rabbit) is:new -nc:house deck:"inner quotes test!"`
