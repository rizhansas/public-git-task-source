import logging
import irm_utils


logger = logging.getLogger(__name__)


def irm_run(io_dict):

    logger.info('Print a line from input on the branch dev-ver-3.0!')
    input_file_path = io_dict['input']
    logger.info('Get input file path: %s' % input_file_path)
    rank = int(irm_utils.get_task_rank(io_dict))
    logger.info('Get rank: %d' % rank)
    with open(input_file_path) as input_file:
        lines = input_file.readlines()
        index = rank
        if len(lines) >= rank:
            index = len(lines) - 1
        logger.info('Read %d line: %s' % (index, lines[index]))
    logger.info('Done!')

