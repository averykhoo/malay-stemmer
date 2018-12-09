# malay-stemmer
affix removal for malay

## usage
-   the `stem` function will take a word and return all possible stems, along with the removed prefix(es) and suffix(es)
-   give it a lowercase word with at most one hyphen (and no apostrophe)
-   use the `recursive` flag if you want the stemmer to remove multiple layers of affixes