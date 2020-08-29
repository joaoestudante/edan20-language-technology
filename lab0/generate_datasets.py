import random

class Spell:
    def __init__(self, correct):
        self.correct = correct
        self.wrong = []

    def add_wrong_spelling(self, word):
        self.wrong.append(word)

    def __repr__(self):
        if len(self.wrong) >= 2:
            wrong_indexes = random.sample(range(0, len(self.wrong)), 2)
            return self.correct + ": " + self.wrong[wrong_indexes[0]] + " " + self.wrong[wrong_indexes[1]]
        else:
            return self.correct + ": " + self.wrong[0] + " " + self.wrong[0]

    def __str__(self):
        return self.__repr__()

right_wrong_list = []
with open('missp.dat', 'r') as file:
    lines = file.readlines()
    for word in lines:
        if '$' in word: # correct spelling
            right_wrong_list.append(Spell(word.replace("$", '').replace('\n', '')))
        else:
            right_wrong_list[-1].add_wrong_spelling(word.replace('\n', ''))

# Do actual generation, by splitting sets in half randomly:
first_set_indexes = random.sample(range(0, len(right_wrong_list)), int(len(right_wrong_list)/2))
second_set_indexes = [i for i in range(0, len(right_wrong_list)) if i not in first_set_indexes]

with open('generated-spell-testset1.txt', 'w') as first_set:
    for i in first_set_indexes:
        first_set.write(str(right_wrong_list[i]) + "\n")

    print("set1 generated")

with open('generated-spell-testset2.txt', 'w') as second_set:
    for i in second_set_indexes:
        second_set.write(str(right_wrong_list[i]) + "\n")

    print("set2 generated")
