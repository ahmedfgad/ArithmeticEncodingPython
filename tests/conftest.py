"""Shared pytest fixtures for the ArithmeticEncodingPython project."""

import tempfile
import shutil
from pathlib import Path
from typing import Generator, Any

import pytest


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory that gets cleaned up after the test."""
    temp_path = Path(tempfile.mkdtemp())
    try:
        yield temp_path
    finally:
        shutil.rmtree(temp_path, ignore_errors=True)


@pytest.fixture
def temp_file(temp_dir: Path) -> Path:
    """Create a temporary file in the temp directory."""
    temp_file_path = temp_dir / "test_file.txt"
    temp_file_path.touch()
    return temp_file_path


@pytest.fixture
def sample_data() -> bytes:
    """Provide sample binary data for testing."""
    return b"Hello, World! This is sample data for arithmetic encoding tests."


@pytest.fixture
def sample_text() -> str:
    """Provide sample text data for testing."""
    return "Hello, World! This is sample text for arithmetic encoding tests."


@pytest.fixture
def sample_frequencies() -> dict[str, int]:
    """Provide sample character frequencies for testing."""
    return {
        'a': 5,
        'b': 3,
        'c': 2,
        'd': 1,
        'e': 8,
        'f': 1,
        'g': 2,
        'h': 4,
        'i': 6,
        'j': 1,
        'k': 1,
        'l': 3,
        'm': 2,
        'n': 6,
        'o': 7,
        'p': 2,
        'q': 1,
        'r': 6,
        's': 6,
        't': 9,
        'u': 3,
        'v': 2,
        'w': 2,
        'x': 1,
        'y': 2,
        'z': 1,
        ' ': 10
    }


@pytest.fixture
def mock_file_operations(mocker):
    """Mock file operations for testing."""
    mock_open = mocker.mock_open()
    mocker.patch('builtins.open', mock_open)
    return mock_open


@pytest.fixture(autouse=True)
def reset_module_state():
    """Reset any global module state before each test."""
    # This fixture runs automatically before each test
    # Add any module-specific state reset logic here if needed
    yield


@pytest.fixture
def capture_output(capsys):
    """Fixture to capture stdout/stderr output."""
    def _capture():
        return capsys.readouterr()
    return _capture


@pytest.fixture(scope="session")
def test_data_dir() -> Path:
    """Path to test data directory."""
    return Path(__file__).parent / "data"


@pytest.fixture
def mock_random_seed(mocker):
    """Mock random seed for reproducible tests."""
    mocker.patch('random.seed')
    return mocker


# Parametrized fixtures for common test scenarios
@pytest.fixture(params=[
    b"a",
    b"abc",
    b"hello world",
    b"The quick brown fox jumps over the lazy dog",
    bytes(range(256)),  # All possible byte values
])
def various_binary_inputs(request) -> bytes:
    """Provide various binary inputs for comprehensive testing."""
    return request.param


@pytest.fixture(params=[
    "",
    "a",
    "abc",
    "hello world",
    "The quick brown fox jumps over the lazy dog",
    "Special chars: !@#$%^&*()_+-={}[]|\\:;\"'<>?,./"
])
def various_text_inputs(request) -> str:
    """Provide various text inputs for comprehensive testing."""
    return request.param