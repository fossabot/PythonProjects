import pytest

def calc(num, value=2):
    return num ** value

'''
python -m pytest <filename>
pytest <filename>
pytest <filename>::<test_func_name>
pytest -m <marker> <filename>
'''

@pytest.mark.tstcalc
def test_calc_1():
    assert calc(5) == 125

@pytest.mark.tstcalc
def test_calc_2():
    assert calc(5, 3) == 125
