# TODO create class that will automatically decompile an inputted equation to an easily understandable format
# TODO find the indexes of each variable in the equation
# TODO output the divided up equation in a list along with the indexes of each variable in a tuple

class Recompiler:
    def __init__(self, equation):
        self.equation = equation
        self.equation_list = []
        self.index_dictionary = {}
        self.functions = ('+', '-', '*', '/', '=')

    def separator(self):
        # TODO define sets for managing equation changes
        do_add = bool

        for item in self.equation:

            if item != ' ':
                try:
                    item = int(item, 10)
                except ValueError:
                    item = str(item)
                finally:
                    self.equation_list.append(item)

                try:
                    if item in self.functions or item.isalpha():
                        do_add = True
                except AttributeError:
                    do_add = False

                if do_add:
                    self.add_to_dict(item=item)

    def add_to_dict(self, item):
        self.index_dictionary[len(self.equation_list) - 1] = item

    def editor(self):
        pass

    def compiler(self):
        pass
