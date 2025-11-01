import os

def test_transcrypt_output():
    """Test that transcrypt output exists and contains expected content."""
    # Check that the file exists
    js_file_path = os.path.join(os.path.dirname(__file__), '..', 'static', 'js', 'hello.js')
    assert os.path.exists(js_file_path)

    # Check that the file contains the expected content
    with open(js_file_path, 'r') as f:
        content = f.read()
        assert "alert ('hello world')" in content
