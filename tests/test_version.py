"""Test for version file syntax."""
import re

from transpose_dict.__version__ import __version__


def test_version():
    """Test the version string for PEP440 compatibility."""
    pattern = re.compile(r"\d+\.\d+\.\d+")
    assert pattern.match(__version__)