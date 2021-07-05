import os
import pytest
import typing as tp
import pandas as pd
import numpy as np
import pystable


@pytest.fixture
def data() -> tp.List[float]:
    """
    Fixture to get example dataset
    """
    base = os.path.dirname(os.path.abspath(__file__))
    base = os.path.join(base, 'helpers')
    base = os.path.join(base, 'data.csv')
    return pd.read_csv(base).to_numpy().tolist()


@pytest.fixture
def fit() -> tp.List[float]:
    """
    Fixture to get stable distribution example params.
    Should fit the example dataset.
    """
    base = os.path.dirname(os.path.abspath(__file__))
    base = os.path.join(base, 'helpers')
    base = os.path.join(base, 'fit.csv')
    return pd.read_csv(base).to_numpy().tolist()


@pytest.fixture
def cdfs() -> pd.DataFrame:
    """
    Fixture to get generated cdf values from example stable distribution
    """
    base = os.path.dirname(os.path.abspath(__file__))
    base = os.path.join(base, 'helpers')
    base = os.path.join(base, 'cdfs.csv')
    return pd.read_csv(base)


@pytest.fixture
def pdfs() -> pd.DataFrame:
    """
    Fixture to get generated pdf values from example stable distribution
    """
    base = os.path.dirname(os.path.abspath(__file__))
    base = os.path.join(base, 'helpers')
    base = os.path.join(base, 'pdfs.csv')
    return pd.read_csv(base)


@pytest.fixture
def quantiles() -> pd.DataFrame:
    """
    Fixture to get generated cdf^{-1} values from example stable distribution
    """
    base = os.path.dirname(os.path.abspath(__file__))
    base = os.path.join(base, 'helpers')
    base = os.path.join(base, 'quantiles.csv')
    return pd.read_csv(base)


def test_cdf(fit, cdfs):
    """
    Tests cdf values for stable example
    """
    expected = cdfs['value'].tolist()
    x = cdfs['x'].to_numpy().tolist()
    actual = pystable.cdf(x, *fit)
    assert np.testing.assert_allclose(expected, actual, rtol=1e-08)


def test_pdf(fit, pdfs):
    """
    Tests pdf values for stable example
    """
    expected = pdfs['value'].tolist()
    x = pdfs['x'].to_numpy().tolist()
    actual = pystable.pdf(x, *fit)
    assert np.testing.assert_allclose(expected, actual, rtol=1e-08)


def test_quantile(fit, quantiles):
    """
    Tests quantile values for stable example
    """
    expected = quantiles['value'].tolist()
    q = quantiles['q'].to_numpy().tolist()
    actual = pystable.q(q, *fit)
    assert np.testing.assert_allclose(expected, actual, rtol=1e-08)


def test_fit(fit, data):
    """
    Tests stable param estimation for dataset
    """
    expected = fit
    actual = pystable.fit(data)
    assert np.testing.assert_allclose(expected, actual, rtol=1e-08)
