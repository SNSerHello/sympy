#!/usr/bin/env python
"""
Run tests for specific packages that use optional dependencies.

The optional dependencies need to be installed before running this.
"""


# Add the local sympy to sys.path (needed for CI)
from get_sympy import path_hack
path_hack()


class TestsFailedError(Exception):
    pass


test_list = [
    # numpy
    '*numpy*',
    'sympy/core/',
    'sympy/matrices/',
    'sympy/physics/quantum/',
    'sympy/utilities/tests/test_lambdify.py',

    # scipy
    '*scipy*',

    # matplotlib
    'sympy/plotting/',

    # llvmlite
    '*llvm*',

    # aesara
    '*aesara*',

    # jax
    '*jax*',

    # gmpy
    'polys',

    # autowrap
    '*autowrap*',

    # ipython
    '*ipython*',

    # antlr, lfortran, clang
    'sympy/parsing/',

    # matchpy
    '*rubi*',

    # codegen
    'sympy/codegen/',
    'sympy/utilities/tests/test_codegen',
    'sympy/utilities/_compilation/tests/test_compilation',

    # cloudpickle
    'pickling',

    # pycosat
    'sympy/logic',
    'sympy/assumptions',

    #stats
    'sympy/stats',

]


blacklist = [
    'sympy/physics/quantum/tests/test_circuitplot.py',
]


doctest_list = [
    # numpy
    'sympy/matrices/',
    'sympy/utilities/lambdify.py',

    # scipy
    '*scipy*',

    # matplotlib
    'sympy/plotting/',

    # llvmlite
    '*llvm*',

    # aesara
    '*aesara*',

    # gmpy
    'polys',

    # autowrap
    '*autowrap*',

    # ipython
    '*ipython*',

    # antlr, lfortran, clang
    'sympy/parsing/',

    # matchpy
    '*rubi*',

    # codegen
    'sympy/codegen/',

    # pycosat
    'sympy/logic',
    'sympy/assumptions',

    #stats
    'sympy/stats',

]


print('Testing optional dependencies')


from sympy import test, doctest


tests_passed = test(*test_list, blacklist=blacklist)
doctests_passed = doctest(*doctest_list)


if not tests_passed and not doctests_passed:
    raise TestsFailedError('Tests and doctests failed')
elif not tests_passed:
    raise TestsFailedError('Doctests passed but tests failed')
elif not doctests_passed:
    raise TestsFailedError('Tests passed but doctests failed')
