switch = input("Every other word removed or every other other? Write 1 for other other, and 0 for other.")

switch = int(switch)

verse = "For we are God’s handiwork, created in Christ Jesus to do good works, which God prepared in advance for us to do. Ephesians 2:10"
#put a hashtag before the second verse if you wanna study in english
verse = "Cuando vieron al niño, contaron lo que les habían dicho acerca de él y cuantos lo oyeron se asombraron de lo que los pastores decían. María, por su parte, guardaba todas estas cosas en su corazón y meditaba acerca de ellas. Los pastores regresaron glorificando y alabando a Dios por lo que habían visto y oído, pues todo sucedió tal como se les había dicho."

#the verse split into a list
splitverse = verse.split()

#the verse, with every other word replaced by "_"
down_verse = []

#the verse, with the only words being the words replace by "_"
up_verse = []

#this creates up_verse and down_verse
for i in splitverse:
    if switch == 0:
        down_verse.append(i)
        switch = 1
    elif switch == 1:
        down_verse.append(" __ ")
        up_verse.append(i)
        switch = 0

#print down_verse as a string, not a list
print(''.join(down_verse))

#number off words missing
nowm = len(up_verse)
#NOW you got correct
nowm_good = 0
#the words you got incorrect
nowm_bad = []
#the words you shouldve written instead
nowm_should = []

answer = input("Enter the missing words! No commas, just spaces. Do note that there is some trouble with punctuation.")
answer = answer.split()

#compare your answer with the real answer
for f, b in zip(up_verse, answer):
    if f == b:
        nowm_good += 1
    if f != b:
        nowm_bad.append(f)
        nowm_should.append(b)

print(f"You got {nowm_good} words out of {nowm} correct!")

if len(nowm_bad) != 0 or len(nowm_bad) != 1:
    print(f"You messed up {nowm_bad} and you wrote them as {nowm_should}, respectively.")
if len(nowm_bad) == 1:
    print(f"You messed up {nowm_bad} and you wrote it as {nowm_should}.")
