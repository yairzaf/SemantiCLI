import argparse
from semanticli.model.install import DEFAULT_MODEL

'''default parameters'''
COS_SIM = 0.8
SEPARATOR = '\n\n'
CHUNK_SIZE = 4000
CHUNK_OVERLAP = 200
EMBED_MODEL = DEFAULT_MODEL

def create_parser():
    """Create the parser."""
    parser = argparse.ArgumentParser(
        description='Semantic Text Search',
        prog='smnti',
        epilog='Example useage: $ cat Alice.txt |  smnti -c 512 -o 128 "Deck of cards" -- note: Chunck size will overflow if seperator is not encountered.'
    )

    parser.add_argument(
        '-V','--version',
        action='store_true',
        help='Print SemantiCLI Version and exit'
    )

    parser.add_argument(
        '--debug',
        action='store_true',
        help='Enable debug logging'
    )

    parser.add_argument(
        '-m','--model',
        type=str,
        default=EMBED_MODEL,
        metavar='model_name',
        help='The embedding model used for the search, default {model}'.format(model=EMBED_MODEL)
    )

    parser.add_argument(
        '-im','--install-model',
        type=str,
        metavar='model_name',
        help='Name of the model repo to be installed from huggingface (e.g mixedbread-ai/mxbai-embed-large-v1)'
    )

    parser.add_argument(
        '-rm','--remove-model',
        type=str,
        metavar='model_name',
        help='Remove embedding model from local'
    )

    parser.add_argument(
        '-lm','--list-models',
        action='store_true',
        help='List locally installed models',
    )

    parser.add_argument(
        '-cs','--cos-sim',
        type=float,
        default=COS_SIM,
        metavar='similarity',
        help='Target cosine similarity for text (between 0-1), default {cosim}'.format(cosim=COS_SIM)
    )

    parser.add_argument(
        '-s','--separator',
        type=str,
        default=SEPARATOR,
        metavar='separator_string',
        help='Separation string for chunks, default \\n\\n'
    )

    parser.add_argument(
        '-c','--chunk-size',
        type=int,
        default=CHUNK_SIZE,
        metavar='size',
        help='Maximum chunk size to split on, default {cs}'.format(cs=CHUNK_SIZE)
    )

    parser.add_argument(
        '-o','--chunk-overlap',
        type=int,
        default=CHUNK_OVERLAP,
        metavar='size',
        help='Chunk overlapping, default {co}'.format(co=CHUNK_OVERLAP)
    )

    parser.add_argument(
        '-n','--line-number',
        action='store_true',
        help='Print line number of the match'
    )

    parser.add_argument(
        '-v','--invert-match',
        action='store_true',
        help='Invert match (lower then target cosine similarity)'
    )

    parser.add_argument(
        'search_pattern',
        nargs='?',
        type=str,
        default=None,
        metavar='search_text',
        help='Text to search for'
    )

    parser.add_argument(
        'search_input',
        nargs='?',
        type=str,
        default=None,
        metavar='target_text',
        help='Text to search in, can also be passed in STDIN with a pipe'
    )

    parser.add_argument(
        '-f','--file',
        type=str,
        nargs='+',
        help='File/s to search in'
    )

    return parser