"""Validation tests to ensure the testing infrastructure is working correctly."""

import sys
from pathlib import Path

import pytest


class TestSetupValidation:
    """Test class to validate testing infrastructure setup."""
    
    def test_python_version(self):
        """Test that Python version is compatible."""
        assert sys.version_info >= (3, 8), f"Python 3.8+ required, got {sys.version_info}"
    
    def test_pytest_markers_registered(self, pytestconfig):
        """Test that custom markers are properly registered."""
        # Get registered markers from config
        markers = list(pytestconfig.getini("markers"))
        marker_names = [marker.split(":")[0].strip() for marker in markers]
        assert "unit" in marker_names, "unit marker should be registered"
        assert "integration" in marker_names, "integration marker should be registered" 
        assert "slow" in marker_names, "slow marker should be registered"
    
    @pytest.mark.unit
    def test_unit_marker(self):
        """Test that unit marker works."""
        assert True, "Unit marker test passed"
    
    @pytest.mark.integration  
    def test_integration_marker(self):
        """Test that integration marker works."""
        assert True, "Integration marker test passed"
    
    @pytest.mark.slow
    def test_slow_marker(self):
        """Test that slow marker works."""
        assert True, "Slow marker test passed"
    
    def test_project_structure(self):
        """Test that project structure is correct."""
        project_root = Path(__file__).parent.parent
        
        # Check main files exist
        assert (project_root / "pyae.py").exists(), "pyae.py should exist"
        assert (project_root / "pyproject.toml").exists(), "pyproject.toml should exist"
        assert (project_root / "README.md").exists(), "README.md should exist"
        
        # Check test structure
        tests_dir = project_root / "tests"
        assert tests_dir.exists(), "tests directory should exist"
        assert (tests_dir / "__init__.py").exists(), "tests/__init__.py should exist"
        assert (tests_dir / "conftest.py").exists(), "tests/conftest.py should exist"
        assert (tests_dir / "unit").exists(), "tests/unit should exist"
        assert (tests_dir / "unit" / "__init__.py").exists(), "tests/unit/__init__.py should exist"
        assert (tests_dir / "integration").exists(), "tests/integration should exist"  
        assert (tests_dir / "integration" / "__init__.py").exists(), "tests/integration/__init__.py should exist"
    
    def test_fixtures_available(self, temp_dir, temp_file, sample_data, sample_text):
        """Test that shared fixtures are available and working."""
        # Test temp_dir fixture
        assert temp_dir.exists(), "temp_dir fixture should create directory"
        assert temp_dir.is_dir(), "temp_dir should be a directory"
        
        # Test temp_file fixture  
        assert temp_file.exists(), "temp_file fixture should create file"
        assert temp_file.is_file(), "temp_file should be a file"
        assert temp_file.parent == temp_dir, "temp_file should be in temp_dir"
        
        # Test sample data fixtures
        assert isinstance(sample_data, bytes), "sample_data should be bytes"
        assert len(sample_data) > 0, "sample_data should not be empty"
        assert isinstance(sample_text, str), "sample_text should be string"
        assert len(sample_text) > 0, "sample_text should not be empty"
    
    def test_mocking_available(self, mock_file_operations):
        """Test that mocking utilities are available."""
        assert mock_file_operations is not None, "mock_file_operations fixture should be available"
        
        # Test that we can use the mock
        with mock_file_operations():
            pass  # Mock is working if no exception
    
    def test_parametrized_fixtures(self, various_binary_inputs, various_text_inputs):
        """Test that parametrized fixtures work."""
        assert isinstance(various_binary_inputs, bytes), "various_binary_inputs should be bytes"
        assert isinstance(various_text_inputs, str), "various_text_inputs should be string"


def test_coverage_configuration():
    """Test that coverage configuration is working."""
    # This test will be covered and should appear in coverage report
    covered_line = "This line should be covered"
    assert covered_line == "This line should be covered"


def test_simple_assertion():
    """Simple test to verify pytest is working."""
    assert 1 + 1 == 2, "Basic math should work"
    assert "hello".upper() == "HELLO", "String methods should work"
    assert [1, 2, 3] == [1, 2, 3], "List comparison should work"