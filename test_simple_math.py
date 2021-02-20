# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 15:31:07 2021

@author: oscbr226
"""
'''Test function for simple_math.py. Tests addition, subtraction, 
multiplication, division, first degree polynomials and 
second degree polynomials.'''

import simple_math as sm
import pytest

@pytest.mark.parametrize("add_a, add_b, add_expected", [
    (1,1,2),
    (1,2,3),
    (4,3,7)
    ])

def test_simple_add(add_a, add_b, add_expected):
    assert sm.simple_add(add_a,add_b) == add_expected
   
@pytest.mark.parametrize("sub_a, sub_b, sub_expected", [
    (1,1,0),
    (1,2,-1),
    (4,3,1)
    ])
     
def test_simple_sub(sub_a, sub_b, sub_expected):
    assert sm.simple_sub(sub_a,sub_b) == sub_expected
      
@pytest.mark.parametrize("mult_a, mult_b, mult_expected", [
    (1,1,1),
    (1,2,2),
    (4,3,12)
    ])
    
def test_simple_mult(mult_a, mult_b, mult_expected):
    assert sm.simple_mult(mult_a,mult_b) == mult_expected

@pytest.mark.parametrize("div_a, div_b, div_expected", [
    (100,10,10),
    (1,2,0.5),
    (0,3,0)
    ])    
def test_simple_div(div_a, div_b, div_expected):
    assert sm.simple_div(div_a,div_b) == div_expected
        
    
@pytest.mark.parametrize("pf_x, pf_a0, pf_a1, pf_expected", [
    (1,1,1,2),
    (10,2,3,32),
    (-8,0,10,-80)
    ])
    
def test_poly_first(pf_x, pf_a0, pf_a1, pf_expected):
    assert sm.poly_first(pf_x, pf_a0, pf_a1) == pf_expected
 
    
@pytest.mark.parametrize("ps_x, ps_a0, ps_a1, ps_a2, ps_expected", [
    (1,1,1,1,3),
    (2,0,2,1,8),
    (-3,5,10,2,-7)
    ])
def test_poly_second(ps_x, ps_a0, ps_a1, ps_a2, ps_expected):
    assert sm.poly_second(ps_x, ps_a0, ps_a1, ps_a2) == ps_expected