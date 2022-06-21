#!/usr/bin/env python
# coding: utf-8


import pandas as pd

import plotly.graph_objects as go

import numpy as np

# Pulls in html tables from URL
discog = pd.read_html('https://en.wikipedia.org/wiki/Peter_Gabriel_discography')

# Check to see how many tables are present
len(discog)

# Accessing the 6th table
discog[6]


# Create a dataframe called df_singles
df_singles = pd.DataFrame(discog[6])


df_singles


df_singles.columns.droplevel(level=0)


# Remove the first level via droplevel:
df_singles = df_singles.droplevel(level=0, axis=1)


# Get columns
for col in df_singles:
    print(col)

df_singles


# Remove the last row
df_singles.drop(index=df_singles.index[-1], 
        axis=0, 
        inplace=True)


# Replace NaN values with '0'
df_singles['Certifications'] = df_singles['Certifications'].fillna(0)


# remove [ ]
to_replace = {'[': '',
              ']': ''
             }

for k, v in to_replace.items():
    df_singles.columns = df_singles.columns.str.replace(k, v)

# remove numbers
df_singles.columns = df_singles.columns .str.replace('\d+', '')


from IPython.display import HTML


# define hover
def hover(hover_color="#ADD8E6"):
    return dict(selector="tr:hover",
                props=[("background-color", "%s" % hover_color)])

# define styles
styles = [
    hover(),
    dict(selector="th", props=[("font-size", "100%"),
                               ("text-align", "center")]),
    dict(selector="caption", props=[("caption-side", "top")])
]


# set datafarame to styles
html = (df_singles.style.set_table_styles(styles)
          .set_caption("Hover to highlight."))


html
