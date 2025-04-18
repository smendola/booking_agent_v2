#!/usr/bin/env python
import os
import sys
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, 
                   format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    """Simple wrapper to run the app with debug output"""
    try:
        logger.info("Starting booking agent application")
        # Add the parent directory to the path so we can import modules
        sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        
        # Import the app module
        # We need to import the app.py module, not the app package
        import importlib.util
        spec = importlib.util.spec_from_file_location("app_module", 
                                                   os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "app.py"))
        app_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(app_module)
        logger.info("Successfully imported app module")
        
        # Run the app
        port = int(os.environ.get("GRADIO_SERVER_PORT", 7860))
        logger.info(f"Launching app on port {port}")
        app_module.demo.launch(server_port=port, share=False)
    except Exception as e:
        logger.error(f"Error running app: {str(e)}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
