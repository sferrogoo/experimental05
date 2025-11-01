import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_for_three_js(client):
    """Test the index page for three.js scripts."""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>' in rv.data
    assert b'<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>' in rv.data
    assert b'<script src="/static/js/three_app.js"></script>' in rv.data
    assert b'<div id="container">' in rv.data

def test_index_for_gui(client):
    """Test the index page for GUI scripts."""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'<script src="https://cdnjs.cloudflare.com/ajax/libs/dat-gui/0.7.9/dat.gui.min.js"></script>' in rv.data
