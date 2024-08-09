#!bin/python3

# sort out arguments

import argparse

parser = argparse.ArgumentParser(
                    prog='HNBlog',
                    description='Converts a pile of markdown files to a website',
                    epilog='Good Luck')

parser.add_argument('--from', dest='files', default="./content/",
                    help='Directory to pull markdown files from')

parser.add_argument('--to', dest='output', default="./docs",
                    help='Directory to pull markdown files from')



args = parser.parse_args()


# scan the content of the blog

import glob

files = glob.glob(args.files + '**/*.md', recursive=True)

# resources

import frontmatter

resources = [frontmatter.load(f) for f in files]

# Collect tagged posts by tag

tags = {"all":[]}
for r in resources:
	tags["all"].append(r)
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
    ''' Open "path" for writing, creating any parent directories as needed.
    '''
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return open(path, 'w')

import mistune

for r in resources:
	print(":\""+r["title"]+"\":")
	template = environment.get_template(r["_template"])
	output = template.render(args=r, content=mistune.html(str(r)), tags=tags, title=r["title"])

	for o in r["_targets"]:
		print("--> "+o)
		with safe_open_w(os.path.join(args.output,o)) as fp:
			fp.write(output)

