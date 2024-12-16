import argparse
import sys
from semanticli import __version__
from semanticli.commands import greet, version
from semanticli.utils.logger import setup_logger

def create_parser():
    """Create the top-level parser."""
    parser = argparse.ArgumentParser(
        description="A command line tool using argparse",
        prog="semanticli"
    )
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Enable debug logging'
    )
    
    # Create subparsers for different commands
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Add commands
    greet.setup_parser(subparsers)
    version.setup_parser(subparsers)
    
    return parser

def main():
    """Main entry point for the CLI."""
    parser = create_parser()
    args = parser.parse_args()
    
    # Setup logging
    logger = setup_logger(debug=args.debug)
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    try:
        # Dispatch to appropriate command
        if args.command == 'greet':
            greet.run(args)
        elif args.command == 'version':
            version.run(args)
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        if args.debug:
            raise
        sys.exit(1)