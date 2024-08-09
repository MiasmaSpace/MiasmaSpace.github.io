---
# title, date, ect are just extra key values
title: This is actually just an arbitrary string

# jinja template to apply to this file
_template: "article.html"

date:   2024-08-04

# puts the rendered file 
_targets: 
- test.html

# adds this page to the given tags
_tags:
    - tag
    - tag2

# replaces this attribute with the frontmatter of the pages that match the tag
_collections: 
    - tag
    - tag2
---


This is whatever content we want in markdown

## Test

First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell


content in paragraph with footnote[^1] markup.

| Days of Maintenance | XP Multiplier  |
| ------------------- | -------------- |
|                   1 |             x1 |
|                   2 |             x2 |
|                   3 |             x3 |
|                   5 |             x4 |
|                   8 |             x5 |
|                  13 |             x6 |
|                  21 |             x7 |
|                  34 |             x8 |
|                  55 |             x9 |
|                  89 |            x10 |
|                 144 |            x11 |
|                 233 |            x12 |
|                 377 |            x13 |


[^1]: footnote explain


> block
> quote
> here
