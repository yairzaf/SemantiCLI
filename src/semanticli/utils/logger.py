import logging
import sys

def setup_logger(debug=False):
    """Configure logging for the application."""
    logger = logging.getLogger('semanticli')
    logger.setLevel(logging.DEBUG if debug else logging.INFO)
    
    # Create console handler
    handler = logging.StreamHandler(sys.stderr)
    handler.setLevel(logging.DEBUG if debug else logging.INFO)
    
    # Create formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    
    # Add handler to logger
    logger.addHandler(handler)
    
    return logger