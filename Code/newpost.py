#!/usr/bin/env python3
from datetime import datetime
from pathlib import Path
import digger

pelroot = Path.cwd()
postfolder = Path(pelroot,'content')

header = {'Title': "",
'Date': "2024-05-21 20:00",
'Author': "Dr. Gerg",
'Category': "category",
'Tags': "life,living,people,philosophy,poetry,politics",
'Slug': "slug",
'Status': "draft"
}

bodyblock = str('![default blossom image]({photo}/blossom.png){width="40%"}</br><span style="color:green; font-size:smaller;">Caption</span>\n\n\nThis is a **a thing that works!**.\n\n\n[![link to home page]({photo}/basic/cropped-drgerg_wpLogo-1-2.png "https://www.drgerg.com")](https://www.drgerg.com)')

thisdate = datetime.now().strftime("%Y-%m-%d %H:%M")

header["Date"] = thisdate
header["Title"] = input("Title: ")

print("\n\tSelect the category: \n")
header["Category"] = digger.buildkeepers('cat')
# print("Category is " + header["Category"])

print("\n\tCreate the list of tags: \n")
header["Tags"] = digger.buildkeepers('tag')
# print("Tags is " + header["Tags"])

header["Slug"] = input("Slug: ")

guts = str("Title: "+header["Title"]+'\n'+
"Date: "+header["Date"]+'\n'+
"Category: "+header["Category"]+'\n'+
"Tags: "+header["Tags"]+'\n'+
"Slug: "+header["Slug"]+'\n'+
"Status: "+header["Status"]+'\n\n'+
bodyblock+'\n'
)

outfile = Path(postfolder,str(header["Slug"] + '.md'))
with open(outfile, mode='w') as post:
    post.write(guts)
print("Saved " + str(outfile) + '\n')