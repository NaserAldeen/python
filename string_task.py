story_string = """It was {} o'clock when I heard a knock at the door.
I opened the door and there was a box full of {} with a note saying "From Mr. {}".
Just as I closed the door I heard a scream "{}".
I froze in place and all I could do was {}."""

print("Mad libs where libs get Mad\nStart Below:\n\n")

time = input("Number: ")
item = input("Noun(Plural): ")
name = input("Name: ")
scream = input("Any sentence: ")
action = input("Verb: ")

formated_story = story_string.format(time, item, name.title(), scream.upper(), action)
print (formated_story)
