import pytest
from main import somar
from main import subtrair

def test_somar():
    assert somar(2,4)==6

def test_subtrair():
    assert subtrair(9,5)==4
 
