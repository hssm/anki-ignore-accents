# anki-ignore-accents
Anki add-on that forces browser search to always ignore accents/diacritical marks. Compatible with **Anki 2.1.28** and newer.

![Ignore accents](https://raw.github.com/hssm/anki-ignore-accents/master/docs/example.png "Ignore accents in browser search")

Since version 2.1.24, Anki allows you to search in the browser while ignoring accents or diacritial marks by adding a marker to each word you want to search for: `nc:something`. This is not very intuitive for those who frequenty rely on this behavior or when multiple terms are included in the search.

This add-on will do the hard work for you and ensure every term in your search is automatically converted to `nc:myword` without you doing anything else. Once the add-on is installed, the behavior is always enabled and it will always modify your browser searches.

It is safe to search with other modifiers included. E.g:

`"deck:Chinese::Let's try 2500 Most Frequent Chinese Characters With Pinyin Only" chuan is:new zhuan`

Will be converted to

`"deck:Chinese::Let's try 2500 Most Frequent Chinese Characters With Pinyin Only" nc:chuan is:new nc:zhuan`
