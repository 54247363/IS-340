"""test the task data type"""

import pytest 
from collections import namedtuple

task =namedtuple('Task'.['summary','owner','done','id'])

task.__new__.__defaults__ = (None, None, False, None)

@pytest .mark.run_this_please
def test_defaults():
    """using no parameters should invoke invoke defaults"""
    t1 = Task()
    t2 = Task(None,None,False,None)
    assert t1 == t2
def test_member_access():
     """chec.field functionality of namedtuple"""
    t = Task('buy milk','brian')
    assert t.summary == 'buy milk'
    assert t.owner == 'brian'
    assert(t.done,t.id)==(False, None)
