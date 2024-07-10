
from src.infra.application.application import Application
from src.infra.logging.logging_port import logger


def main():
    try:
        application = Application()
        application.run_server()
    except Exception as e:
        logger.error(f"Error during initialization: {e}", exc_info=True)
        raise

if __name__ == '__main__':
    main()
