# TODO create function that will automatically decompile an inputted equation to an easily understandable format
# TODO find the indexes of each variable in the equation
# TODO output the divided up equation in a list along with the indexes of each variable in a tuple

class Decompiler:
    def __init__(self, equation: str) -> None:
        self.equation_list = equation

    def decompile(self,) -> list:
        """
        Decompiles an equation into a list of terms and variables.

        :param equation: equation to be decompiled
        :return: list of terms and variables
        """
        equation = str

        equation = input('Enter equation: ')

        terms = self.get_terms(equation)
        variables = self.get_variables(equation)

        equation_list = [terms, variables]

        return equation_list

    def get_variables(self) -> list:
        """
        Gets the variables from an equation.

        :param equation: equation to get variables from
        :return: list of variables
        """
        variables = list

        for char in self.equation:
            if char.isalpha():
                variables.append(char)

        return variables

    def get_terms(self) -> list:
        """
        Gets the terms from an equation.

        :param equation: equation to get terms from
        :return: list of terms
        """
        terms = list

        for char in self.equation:
            if char.isdigit():
                terms.append(char)

        return terms
