from cli_for_tools.paco_cli import app
import cli_for_tools as ct
from typer.testing import CliRunner

runner = CliRunner()


def test_app():
    result = runner.invoke(
        app,
        ["haz-mapa", "--help"],
    )
    assert result.exit_code == 0
    assert "positions_path" in result.stdout
    assert "mapsource_path" in result.stdout


def test_version():
    expected = "0.3.0"
    obtained = ct.__version__
    assert expected == obtained
