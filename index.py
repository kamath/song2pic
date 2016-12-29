import midi
from PIL import Image
from math import floor, sqrt

pattern = midi.read_midifile("test.mid")

notes = []

for a in pattern:
    for b in a:
        if "Note" in str(b):
            notes.append(b)

print notes

size = int(floor(sqrt(len(notes))))

im = Image.new("RGB", (size, size), "white")

for i in range(size):
    for j in range(size):
        note = notes[i * size + j]
        im.putpixel((i, j), (note.tick % 256, note.data[0] % 256, note.data[1] % 256))

im.show()