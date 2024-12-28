
from semanticli import __version__
from semanticli.utils.logger import setup_logger
from semanticli.cli.parser_setup import create_parser

from semanticli.model.inference import Model
from semanticli.model.install import first_run
from semanticli.model.install import download_model
from semanticli.model.install import delete_model
from semanticli.model.install import list_models

from pathlib import Path
from appdirs import user_data_dir
import time
import numpy as np

import sys
import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)


def main():
    """Main entry point for the CLI."""
    first_run()
    parser = create_parser()
    args = parser.parse_args()
    
    # Setup logging
    logger = setup_logger(debug=args.debug)

    try:
        if(args.version):
            print("SemantiCLI Version: "+__version__)
            sys.exit(0)
        model_manage(args)
        required_args_check(args)
        search_all(args)

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        if args.debug:
            raise
        sys.exit(1)

def model_manage(args):
    if args.install_model != None:
        download_model(args.install_model)
        sys.exit(0)
    if args.remove_model != None:
        delete_model(args.remove_model)
        sys.exit(0)
    if args.list_models:
        list_models()
        sys.exit(0)

def required_args_check(args):
    if not args.search_pattern:
        print('Expected text to search for as an argument, e.g $ smnti Cards -f Alice.txt')
        sys.exit(1)
   
    args.is_stddin = False
    if not sys.stdin.isatty():
        args.is_stddin = True

    if not args.search_input and not args.is_stddin and not args.file:
        print('Expected text or file\s to search in as an argument, e.g $ smnti Cards -f Alice.txt or $ cat Alice.txt | smnti Cards')
        sys.exit(1)

def search_all(args):
    to_search = args.search_pattern
    separator = args.separator.replace('\\n','\n').replace('\\t','\t')
    text_splitter = CharacterTextSplitter(separator=args.separator, chunk_size=args.chunk_size, chunk_overlap=args.chunk_overlap)
    model = Model(args.model)
    search_embedding =  model([to_search])[0]
    timestamp = str(int(time.time()))
    app_dir = Path(user_data_dir("semanticli"))

    if args.search_input:
        if args.line_number:
            print("===> Searching text from cli parameter")
        fname = str(app_dir)+"/search_param_"+timestamp
        with open(fname,"w") as f:
            f.write(args.search_input)
        
        os.remove(fname)
    
    if args.is_stddin:
        if args.line_number:
            print("===> Searching STDIN")
        fname = str(app_dir)+"/stdin_"+timestamp
        with open(fname,"w") as f:
            while not sys.stdin.isatty():
                content = sys.stdin.readline()
                if not content:
                    break
                f.write(content)
        search_file(fname, model, text_splitter, search_embedding, args.cos_sim, args.line_number, args.invert_match)
        os.remove(fname)

    if args.file != None:
        for fname in args.file:
            if args.line_number:
                print("===> Searching text from {name}".format(name=fname))
            search_file(fname, model, text_splitter, search_embedding, args.cos_sim, args.line_number, args.invert_match)

def search_file(fname,model,splitter,embedding,cossim,is_lines,is_invert):
    loader = TextLoader(fname)
    documents = loader.load()
    docs = splitter.split_documents(documents)
    line = 1
    for doc in docs:
        content = doc.page_content
        cont_embd = model([content])[0]
        similarity = cosine_similarity(embedding,cont_embd)
        passed_threshold = similarity >= cossim
        if is_invert:
            passed_threshold = not passed_threshold
        if passed_threshold:
            if(is_lines):
                print("===========================")
                print("===>COS-SIMILARITY: "+str(similarity))
                end = content.count('\n')
                print("===>LINES: {start} - {end}".format(start=line,end=line+end))
                print("===========================")
                line+=end
            print(content)
        
        

def cosine_similarity(A, B):
    
    A = np.asarray(A).flatten()
    B = np.asarray(B).flatten()
    
    dot_product = np.dot(A, B)
    
    norm_A = np.linalg.norm(A)
    norm_B = np.linalg.norm(B)
    
    if norm_A == 0 or norm_B == 0:
        return 0.0
    
    similarity = dot_product / (norm_A * norm_B)
    
    return similarity