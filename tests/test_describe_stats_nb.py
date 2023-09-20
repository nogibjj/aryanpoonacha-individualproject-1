import pytest

@pytest.mark.parametrize("notebook_path", ["../describe_stats.ipynb"])  # Replace with your notebook filename
def test_notebook(notebook_path):
    """
    Test the Jupyter Notebook using nbval.
    """
    import nbval

    # Run the notebook and validate it
    result = nbval.validate(notebook_path)

    # Check if the notebook passed validation
    assert result['passed'], f"Notebook test failed: {result['notebook']}"
