# TODO write the management system for forwarding, retrieving and handling inputs and outputs to and from the decompiler
from .calc_recompiler import Recompiler


def recompile(equation):
    recompiler = Recompiler(equation=equation)
