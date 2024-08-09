---
_template: article.html
title:  "This Blog"
date:   2024-08-04
_tags:
- snippet 
_targets: ["snippets/this_blog.html"]
---

I stole most of the design language for this blog from [Gregory Gundersen](https://gregorygundersen.com/) with consent implied by [How I Built this Blog](https://gregorygundersen.com/How%20I%20Built%20This%20Blog.html).

I find jekyll and similar systems too opinionated on folder structure.
Static site generators all seem to demand you structure your website a certain way.

I want to ensure I never break links, so I am running a custom static site generation toolchain using:

- [python](https://www.python.org/)
- [frontmatter](https://pypi.org/project/python-frontmatter/)
	- Watch out for "no tabs in YAML".
- [jinja2](https://jinja.palletsprojects.com/en/3.1.x/)
	- I don't think I would use jinja in prod, but it is great for offline use.
- [mistune](https://mistune.lepture.com/en/latest/)
	- I had some trouble managing the plugins, but the default parser does everything I want.

I like putting basically all the configuration required into frontmatter.
The script itself is actually simple enough to cite here:


```
# scan the content of the blog

import glob

files = glob.glob("content/" + '**/*.md', recursive=True)

# resources

import frontmatter

resources = [frontmatter.load(f) for f in files]

tags = {}

# build an index of tags to pages

for r in resources:
	if "_tags" in r.keys():
		for t in r["_tags"]:
			if t in tags.keys():
				tags[t].append(r)
			else:
				tags[t] = [r]

# apply templates to resources

from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("templates/"))

import os, os.path

def safe_open_w(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return open(path, 'w')

import mistune

for r in resources:
	print(r["title"])
	template = environment.get_template(r["_template"])
	output = template.render(args=r, content=mistune.html(str(r)), tags=tags)

	for o in r["_targets"]:
		print(o)
		with safe_open_w(os.path.join("output/",o)) as fp:
			fp.write(output)


```

With this, I generate my articles. I can use the tag system to procedurally generate my indexes and rss feed.