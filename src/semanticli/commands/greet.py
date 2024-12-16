import argparse
import logging

logger = logging.getLogger(__name__)

def setup_parser(subparsers):
    """Add parser for the greet command."""
    parser = subparsers.add_parser(
        'greet',
        help='Greet someone'
    )
    parser.add_argument(
        'name',
        help='Name of the person to greet'
    )
    parser.add_argument(
        '-c', '--count',
        type=int,
        default=1,
        help='Number of times to greet'
    )
    return parser

def run(args):
    """Run the greet command."""
    logger.debug(f"Greeting {args.name} {args.count} times")
    for _ in range(args.count):
        print(f"Hello, {args.name}!")

