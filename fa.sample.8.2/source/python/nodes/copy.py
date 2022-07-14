import logging
import shutil


def irm_run(io_dict):
    logger = logging.getLogger(__name__)
    logger.info('Echo the input file to the output destination on the default master branch!')
    input_file_path = io_dict['input']
    output_file_path = io_dict['output']
    logger.info('Input file path: %s' % input_file_path)
    logger.info('Output file path: %s' % output_file_path)
    logger.info('Copying...')
    try:
        shutil.copy(input_file_path, output_file_path)
    except Exception as e:
        logger.error('Get exception %s' % e)

    logger.info('Done!')

