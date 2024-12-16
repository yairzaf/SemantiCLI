import pytest
import argparse
from semanticli.cli import create_parser

@pytest.fixture
def parser():
    return create_parser()
