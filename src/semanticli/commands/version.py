def setup_parser(subparsers):
    """Add parser for the version command."""
    parser = subparsers.add_parser(
        'version',
        help='Show version information'
    )
    return parser

def run(args):
    """Run the version command."""
    from semanticli import __version__
    print(f"semanticli version {__version__}")