from tkinter import *

root = Tk()
text_widget = Text(root, height=2, width=10)
text_widget.pack(fill=X)

text_widget.tag_configure('tag-left', justify='left')
text_widget.insert('end', 'text\n' * 10, 'tag-left')

text_widget1 = Text(root, height=2, width=10)
text_widget1.pack(fill=X)

text_widget1.tag_configure('tag-right', justify='right')
text_widget1.insert('end', 'text\n' * 10, 'tag-right')


root.mainloop()