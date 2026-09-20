# Newpost
## Not Rocket Science.
### Just simple Python convenience.
#### Easily create an annotated template for a new Pelican static blog post.

**www.drgerg.com** runs on the [Pelican](https://getpelican.com) static blog system. I left Wordpress for Pelican in April of 2022 and never looked back.  My needs are simple: a nice-looking site with no commercial aspects at all.  Pelican met the need, and continues to make me happy here in September of 2026.  I don't see that changing.

For years I intended to write up a utility to help me get from **idea** to actually writing the post in the shortest amount of time possible.  I finally did just that.  I'm posting it here on github in the far-out chance someone else might benefit.

**Newpost.py** sits in the folder with your other pelican config files.  When you call it, it prompts you for the different bits of header information, compiles and displays a table of your categories and your tags so you can choose, then creates the new "post.md" file with the name you provided in the "Slug" attribute.

**digger.py** helps newpost.py with the gathering and displaying of categories and tags.  I probably could have just put them together, but I didn't.  So sue me.  ;-)

That's all it does, and that's just perfect.  If you can use any or all of it, go for it.  Happy days!
