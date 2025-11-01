import sys
import os
import subprocess

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.main import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "hello world\n"

