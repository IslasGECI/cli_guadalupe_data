import cli_for_tools as dt


def test_version():
    expected = "0.1.1"
    obtained = dt.__version__
    assert expected == obtained
