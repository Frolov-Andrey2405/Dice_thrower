import random
import sys


class DiceThrower:
    def __init__(self):
        self.prompt = '''
        Dice thrower

        Enter what kind and how many dice to roll. The format is the number of
        dice, followed by "d", followed by the number of sides the dice have.
        You can also add a plus or minus adjustment.

        Examples:
            3d6 rolls three 6-sided dice
            1d10+2 rolls one 10-sided die, and adds 2
            2d38-1 rolls two 38-sided die, and subtracts 1
            QUIT quits the program
        '''

    def run(self):
        print(self.prompt)

        while True:
            try:
                dice_str = input('> ').lower().replace(' ', '')

                if dice_str == 'quit':
                    print('Thanks for playing!')
                    sys.exit()

                number_of_dice, d_index = self.parse_number_of_dice(dice_str)
                number_of_sides, mod_index, mod_amount = self.parse_number_of_sides_and_modifier(
                    dice_str, d_index)

                rolls = self.simulate_dice_rolls(
                    number_of_dice, number_of_sides)
                total = sum(rolls) + mod_amount

                self.display_results(
                    rolls, mod_amount, mod_index, dice_str, total)

            except Exception as exc:
                print('Invalid input. Enter something like "3d6" or "1d10+2".')
                print('Input was invalid because:', exc)

    def parse_number_of_dice(self, dice_str):
        d_index = dice_str.find('d')
        if d_index == -1:
            raise ValueError('Missing the "d" character.')

        number_of_dice = int(dice_str[:d_index])
        return number_of_dice, d_index

    def parse_number_of_sides_and_modifier(self, dice_str, d_index):
        mod_index = dice_str.find('+')
        if mod_index == -1:
            mod_index = dice_str.find('-')

        number_of_sides = int(
            dice_str[d_index + 1:mod_index]) if mod_index != -1 else int(
                dice_str[d_index + 1:]
        )
        mod_amount = int(dice_str[mod_index + 1:]) if mod_index != -1 else 0
        if mod_index != -1 and dice_str[mod_index] == '-':
            mod_amount = -mod_amount

        return number_of_sides, mod_index, mod_amount

    def simulate_dice_rolls(self, number_of_dice, number_of_sides):
        rolls = [
            random.randint(1, number_of_sides) for _ in range(number_of_dice)]
        return rolls

    def display_results(self, rolls, mod_amount, mod_index, dice_str, total):
        print(f'Total: {total} (Each die:', end='')

        rolls_str = ', '.join(map(str, rolls))
        print(rolls_str, end='')

        if mod_index != -1:
            mod_sign = dice_str[mod_index]
            print(f', {mod_sign}{abs(mod_amount)}', end='')

        print(')')


if __name__ == '__main__':
    dice_thrower = DiceThrower()
    dice_thrower.run()
