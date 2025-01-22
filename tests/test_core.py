import numpy as np
import pytest
from pspy.core import lmax2alm

def test_lmax2alm():
    lmax = 300
    n_alm = lmax2alm(lmax)
    assert n_alm == 45451
    print(f'{lmax2alm(lmax)=}')