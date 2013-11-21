import argparse
import logging

parser = argparse.ArgumentParser(description='Sailing Data Collection Server')
parser.add_argument('-p','--port_number', type=int, metavar='Port', help='UDP port number', default=5050)
parser.add_argument('-l', '--log_level', type=str, choices=['debug', 'info', 'warning', 'error', 'critical'], help='Log level to use', default='debug')


settings = {}
settings['port'] = 5050;
settings['log_file'] = 'logs/box.log'
settings['log_level'] = 'DEBUG'
settings['log_format'] = '%(asctime)s:%(levelname)s:%(module)s:%(message)s'
settings['database_file'] = 'db/box.db'

logging.basicConfig(filename=settings['log_file'], 
	level=settings['log_level'].upper(), 
	format=settings['log_format'])