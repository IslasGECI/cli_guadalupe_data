import cli_for_tools as dt


def test_version():
    expected = "0.2.0"
    obtained = dt.__version__
    assert expected == obtained
