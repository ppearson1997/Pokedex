import logging


logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
logging.basicConfig(
    format='[%(asctime)s] - %(name)s - %(levelname)s: %(message)s',
    handlers=[
        logging.StreamHandler(),
    ]
)