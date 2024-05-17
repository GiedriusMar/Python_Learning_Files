# UZD 1 Parašyti klasę Sakinys, kuri turi savybę tekstas ir metodus, kurie:
# Gražina tekstą atbulai
# Gražina tekstą mažosiomis raidėmis
# Gražina tekstą didžiosiomis raidėmis
# Gražina žodį pagal nurodytą eilės numerį
# Gražina, kiek tekste yra nurodytų simbolių arba žodžių *********
# Gražina tekstą su pakeistu nurodytu žodžiu arba simboliu *********
# Atspausdina, kiek sakinyje yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
# Susikurti kelis klasės objektus ir išbandyti visus metodus

class Sentence:
    def __init__(self, text='Kazkoks 1 Parasytas 2 Tekstas 3'):
        self.text = text

    def printing_reverse(self):
        print(self.text[::-1])

    def lower_casing(self):
        print(self.text.lower())

    def upper_casing(self):
        print(self.text.upper())

#    def print_by_order(self):
#      KOL KAS  SITA PRALEIDZIU

    def count_symbols(self):
        print(self.text.count('s'))

    def change_word(self):
        print(self.text.replace('Kazkoks', 'Belekoks'))

    def count_symbols(self):
        result = {
            'words_number': len(self.text.split()),
            'numbers': sum(1 for letter in self.text if letter.isdigit()),
            'upper_letters': sum(1 for letter in self.text if letter.isupper()),
            'lower_letters': sum(1 for letter in self.text if letter.islower()),
        }
        return result
        print(count_symbols())

sentence= Sentence()

sentence.printing_reverse()
sentence.lower_casing()
sentence.upper_casing()
#  sentence.print_by_order()
sentence.count_symbols()
sentence.change_word()
sentence.count_symbols()