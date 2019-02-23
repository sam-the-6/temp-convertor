__author__ = "Soheil Asadi"
__licence__ = "MIT"
__maintainer__ = "Soheil Asadi"
__email__ = "suheyl.asadi@gmail.com"

CUSTOM_ERROR_MESSAGE = """Enter the temperature associated with degrees(Celsius or Fahrenheit) [c / f].
Example: 25 c  (or)  56 f - Don't forget the space between digits and letters!"""


class Temp:

    # main method when __name__ == __main__
    # will call calc() at the end.
    @classmethod
    def get_user_temp_calc(cls):
        user_input = input('Enter Temperature with degree, ex: 25 c: ')
        try:
            temp = [int(s) for s in user_input.split() if s.isdigit()]
            unit = [str(s) for s in user_input.split() if not s.isdigit()]
            temp = temp[0]
            unit = unit[0].lower()
            cls.calc(temp, unit)
        except IndexError:
            print(CUSTOM_ERROR_MESSAGE)
            cls.repeat()

    # calculation method: can be imported into single use method.
    @classmethod
    def calc(cls, temp, unit):
        if unit == 'c':
            fahrenheit = (9.0 / 5.0) * (temp + 32.0)
            print(f"{temp:.2f}(°C) is equal to {fahrenheit:.2f}(°F)")
        elif unit == 'f':
            celsius = (5.0 * float(temp) - 160.0) / 9.0
            print(f"{temp:.2f}(°F) is equal to {celsius:.2f}(°C)")
        else:
            print(CUSTOM_ERROR_MESSAGE)

        cls.repeat()

    # asking user to continue or abort the program.
    @classmethod
    def repeat(cls):
        user_repeat = input('Continue (y/n)?').lower()
        if user_repeat == 'y':
            cls.get_user_temp_calc()
        if user_repeat != 'y' and user_repeat != 'n':
            print("Sorry! Yes(y) - No(n)")
            cls.repeat()


def main():
    Temp.get_user_temp_calc()


if __name__ == '__main__':
    main()
