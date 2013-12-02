import argparse
import logging

settings = {}
settings['port'] = 5050;
settings['log_file'] = 'box/logs/box.log'
settings['log_level'] = 'DEBUG'
settings['log_format'] = '%(asctime)s:%(levelname)s:%(module)s:%(message)s'
settings['database_file'] = 'box/db/box.db'
settings['template_dir'] = 'box/analyze/templates'
settings['static_dir'] = 'box/analyze/static'

def ArgumentParser():
	parser = argparse.ArgumentParser(description='Sailing Data Collection Server')
	parser.add_argument('-p','--port_number', type=int, metavar='Port', help='UDP port number', default=5050)
	parser.add_argument('-l', '--log_level', type=str, choices=['debug', 'info', 'warning', 'error', 'critical'], help='Log level to use', default='debug')
	return parser

def LogConfig():
	return logging.basicConfig(filename=settings['log_file'], 
		level=settings['log_level'].upper(), 
		format=settings['log_format'])