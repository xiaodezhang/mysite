import markdown2
html = markdown2.markdown_path("note/templates/note/note.md")

s = open("note/templates/note/index.html").read()
s = s.replace('{% md "note.md" %}',html)
f = open("note/templates/note/index.html",'w')
f.write(s)
f.close()
