# Tracking Program Execution with Logging
import logging

# Configure the logger
logging.basicConfig(filename='data.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')
def calculate(num1, num2):
    # Log an informational message
    logging.info('Calculation started...')

    try:
        result = num1/num2
        logging.info(f'{num1} divided by {num2} = {result}')
        logging.info('Done with division!')

    except Exception as e:
        # Log an error message
        logging.error(f'Error occurred: {str(e)}')

    # Log a final message
    logging.info('Done with calculations')

calculate(10, 2)
calculate(5, 0)
