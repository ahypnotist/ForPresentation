#formula gotten from this website"
#https://www.education.com/science-fair/article/design-musical-instrument-play-pitches/

#thank you


# length in inches = (tube diameter in inches / 2) + (speed of sound in inches per second/ frequency in hertz x 2)


#speed of sound in inches per second
#this is a constant
SoS = 13397.244

#frequency in hertz
#this goes from c5 to c6
fih = [534.2511, 554.3653, 587.3295, 622.2540, 659.2551, 698.4565, 739.9888, 783.9909, 830.6094, 880, 932.3275, 987.7666, 1046.502, 1108.731, 1174.659, 1244.508, 1318.510, 1396.913]	
notes = ["C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5", "A#5", "B5", "C6", "C#6", "D6", "D#6", "E6", "F6"]

#tube diameter in inches

print("Welcome to the musical pipes calculator!")
print("Higher notes need less length! And pipes with smaller diameters also need less length!")
td = float(input("We only need 1 piece of information, what is the diameter of your pipe? Please give it in inches!"))
print("Thanks!")


#the formula
#L = (td / 2) +(SoS / (fih * 2))

totallength = 0

for (i, j) in zip(fih, notes):
    L = (td / 2) +(SoS / (i * 2))
    L = round(L, 3)
    print(f"{L} is the length needed for the note {j}.")
    totallength += L

print(f"{(totallength / 12)} is the total amount of feet of pipe you need")
