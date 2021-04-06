# TODO write tests for core_calc
# TODO test calc_decompiler for proper outputs
from core_calc.calc_recompiler import Recompiler
from test_lists.recompile_test import tests

tests_questions = tests['questions']
tests_answers = tests['answers']
control_number = 0

for test in tests_questions:
    control_number += 1
    recompiler = Recompiler(test)
    recompiler.separator()
    if recompiler.equation_list in tests_answers:
        print(f'{control_number}. Pass')
    else:
        print(f'{control_number}. Fail')
