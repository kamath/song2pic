import midi
from PIL import Image
from math import floor, sqrt, sin
import os

for filename in os.listdir('music'):
    if filename.endswith('.mid'):
        pattern = midi.read_midifile('music/%s' % filename)

        notes = []

        for a in pattern:
            for b in a:
                if "Note" in str(b):
                    notes.append(b)

        size = int(floor(sqrt(len(notes))))

        im = Image.new("RGB", (size, size), "white")

        for i in range(size):
            for j in range(size):
                note = notes[i * size + j]
                im.putpixel((i, j), (int(abs(sin(note.tick)) * 255), int(abs(sin(note.data[0])) * 255), int(abs(sin(note.data[1])) * 255)))

        im.save('images/%s' % filename.replace('.mid', '.png'), 'PNG')