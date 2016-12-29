
import midi
pattern = midi.read_midifile("test.mid")

notes = []

for a in pattern:
    for b in a:
        if "Note" in str(b) and a.tick and a.data:
            notes.append(b)

