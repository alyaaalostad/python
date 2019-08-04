print("Mad libs where libs get Mad")
print("  Start Below")

time= input("Number:  ")
items= input("Noun(plural): ")
name= input("Name: ")
name_title= name.upper()
scream= input("Any sentence: ")
scream_upper= scream.upper()
action= input("Verb:  ")
story= """ It was {} o'clock when I heard a knock on the door.
I opened the door and there was a box full of {} with a note saying "from Mr. {}."
Just as I closed the door I heard a scream "{}".
I froze in place and all I could do was {}
""" .format(time, items, name_title, scream_upper, action)
print(story)
