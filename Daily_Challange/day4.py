
def dompier_music(switches):
  # Write code below 💖
  # DICTIONARY FOR THE NOTES
  Notes_map = {261: "C4",
               294: "D4",
               329: "E4",
               349: "F4",
               392: "G4",
               440: "A4",
               494: "B4",
               523: "C5",
               0: "REST",
               }
  
  result_notes = [] # List to store the integer values of the notes
  Finish = [] # List to store the final note names
  # Convert each binary string in switches to an integer and store in result_notes
  for notes in switches:
    A = int(notes, 2)
    result_notes.append(A)
    note_name = Notes_map[A]
    Finish.append(note_name)
  return Finish