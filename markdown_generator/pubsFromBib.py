#!/usr/bin/env python
# coding: utf-8

from pybtex.database.input import bibtex
import pybtex.database.input.bibtex 
from time import strptime
import string
import html
import os
import re

# The single source file
BIB_FILE = "proceedings.bib"

# Mapping BibTeX entry types to their specific "venue" fields and pretexts
TYPE_MAPPING = {
    "phdthesis": {
        "venuekey": "school",
        "venue-pretext": "PhD Dissertation, "
    },
    "mastersthesis": {
        "venuekey": "school",
        "venue-pretext": "Master's Thesis, "
    },
    "inproceedings": {
        "venuekey": "booktitle",
        "venue-pretext": "In the proceedings of "
    },
    "proceedings": {
        "venuekey": "booktitle",
        "venue-pretext": "In the proceedings of "
    },
    "article": {
        "venuekey": "journal",
        "venue-pretext": ""
    },
    "techreport": {
        "venuekey": "institution",
        "venue-pretext": "Technical Report, "
    }
}

# Default collection settings
COLLECTION = {"name": "publications", "permalink": "/publication/"}

html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
}

def html_escape(text):
    return "".join(html_escape_table.get(c, c) for c in text)

def rreplace(s, old, new):
    li = s.rsplit(old, 1)
    return new.join(li)

if not os.path.exists(BIB_FILE):
    print(f"ERROR: {BIB_FILE} not found.")
    exit(1)

parser = bibtex.Parser()
bibdata = parser.parse_file(BIB_FILE)

# Loop through all entries in the single bib file
for bib_id in bibdata.entries:
    entry = bibdata.entries[bib_id]
    entry_type = entry.type.lower() # e.g., 'phdthesis', 'article'
    b = entry.fields
    
    try:
        # 1. Handle Dates
        pub_year = b.get("year", "1900")
        pub_month = "01"
        pub_day = "01"

        if "month" in b:
            month_val = b["month"]
            if month_val.isdigit():
                pub_month = month_val.zfill(2)
            else:
                try:
                    tmnth = strptime(month_val[:3], '%b').tm_mon
                    pub_month = "{:02d}".format(tmnth)
                except ValueError:
                    pass
        
        if "day" in b:
            pub_day = b["day"].zfill(2)

        pub_date = f"{pub_year}-{pub_month}-{pub_day}"
        
        # 2. File and Slug naming
        clean_title = b["title"].replace("{", "").replace("}","").replace("\\","").replace(" ","-")
        url_slug = re.sub("\\[.*\\]|[^a-zA-Z0-9_-]", "", clean_title)
        url_slug = url_slug.replace("--","-")

        md_filename = f"{pub_date}-{url_slug}.md".replace("--","-")
        html_filename = f"{pub_date}-{url_slug}".replace("--","-")

        # 3. Authors and Citation
        citation = ""
        authors = ""
        for author in entry.persons.get("author", []):
            name = f"{author.first_names[0]} {author.last_names[0]}"
            citation += f"{name}, "
            authors += f"{name}, "
        
        authors = rreplace(authors[:-2].replace("Zachary Eberhart", "<b>Zachary Eberhart</b>"), ", ", ", and ")
        citation = f'{citation} "{b["title"].replace("{", "").replace("}","").replace("\\","")}."'

        # 4. Dynamic Venue Logic
        # Look up the config based on entry type, fallback to 'article' logic if unknown
        type_config = TYPE_MAPPING.get(entry_type, TYPE_MAPPING["article"])
        venue_key = type_config["venuekey"]
        venue_pretext = type_config["venue-pretext"]

        if venue_key in b:
            venue = venue_pretext + b[venue_key].replace("{", "").replace("}", "").replace("\\", "")
        else:
            venue = "Preprint"

        citation = f"{citation} {venue}, {pub_year}."

        # 5. Build Markdown/YAML
        md = "---\n"
        md += f'title: "{html_escape(b["title"].replace("{", "").replace("}","").replace("\\",""))}"\n'
        md += f"collection: {COLLECTION['name']}\n"
        md += f"authors: {html_escape(authors)}\n"
        md += f"permalink: {COLLECTION['permalink']}{html_filename}\n"
        
        if "note" in b and len(str(b["note"])) > 5:
            md += f"excerpt: '{html_escape(b['note'])}'\n"

        md += f"date: {pub_date}\n"
        md += f"venue: '{html_escape(venue)}'\n"
        
        url = False
        if "url" in b and len(str(b["url"])) > 5:
            md += f"paperurl: '{b['url']}'\n"
            url = True
            
        citation_final = html_escape(citation).replace("Zachary Eberhart", "<b>Zachary Eberhart</b>")
        md += f"citation: '{citation_final}'\n"
        md += "---\n"

        # 6. Page Content
        if "note" in b:
            md += f"\n{html_escape(b['note'])}\n"

        if url:
            md += f"\n[Access paper here]({b['url']}){{:target=\"_blank\"}}\n"
        else:
            search_query = clean_title.replace("-", "+")
            md += f"\nUse [Google Scholar](https://scholar.google.com/scholar?q={search_query}){{:target=\"_blank\"}} for full citation"

        # Save File
        out_dir = "../_publications/"
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        with open(os.path.join(out_dir, os.path.basename(md_filename)), 'w') as f:
            f.write(md)
            
        print(f"SUCCESS: {bib_id} ({entry_type})")
        
    except Exception as e:
        print(f"WARNING: Could not parse {bib_id}. Error: {e}")