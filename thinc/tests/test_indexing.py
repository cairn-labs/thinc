import pytest
import numpy
from numpy.testing import assert_allclose
from thinc.types import Ragged


@pytest.fixture
def ragged():
    data = numpy.zeros((20, 4), dtype="f")
    lengths = numpy.array([4, 2, 8, 1, 4], dtype="i")
    data[0] = 0
    data[1] = 1
    data[2] = 2
    data[3] = 3
    data[4] = 4
    data[5] = 5
    return Ragged(data, lengths)

def test_ragged_starts_ends(ragged):
    starts = ragged._get_starts()
    ends = ragged._get_ends()
    assert list(starts) == [0, 4, 6, 14, 15]
    assert list(ends) == [4, 6, 14, 15, 19]


def test_ragged_simple_index(ragged, i=1):
    r = ragged[i]
    assert_allclose(r.data, ragged.data[4:6])
    assert_allclose(r.lengths, ragged.lengths[i:i+1])


def test_ragged_slice_index(ragged, start=0, end=2):
    r = ragged[start:end]
    size = ragged.lengths[start:end].sum()
    assert r.data.shape == (size, r.data.shape[1])
    assert_allclose(r.lengths, ragged.lengths[start:end])


def test_ragged_array_index(ragged):
    arr = numpy.array([2, 1, 4], dtype="i")
    print(arr)
    r = ragged[arr]
    assert r.data.shape[0] == ragged.lengths[arr].sum()
