import threading
import Queue
import sqlite3
import logging

class Database(threading.Thread):

	def __init__(self, queue):
		self.log = logging.getLogger(__name__)
		self.log.info('Initializing database')

		threading.Thread.__init__(self)
		self.queue = queue
		self.daemon = True
		
		#self.con = sqlite3.connect('box.db')
		#self.cur = self.con.cursor()

		#self._check_schema()

	def _check_schema(self):
		self.cur.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='points';")
		exists = self.cur.fetchone()[0];
		if exists != 1: 
			self._create_schema()

	def _create_schema(self):
		self.log.info('Creating database schema')
		
		f = open('box/schema.sql','r')
		sql = f.read()
		self.cur.executescript(sql)

	def insert(self, datapoint):
		self.log.info('Inserting new datapoint into db - %s', datapoint)
		
		con = sqlite3.connect('db/box.db')
		cur = con.cursor()
		cur.execute("INSERT INTO points(speed) VALUES (?)", (123,))
	def dummy(self, datapoint):
		con = sqlite3.connect('db/box.db')
		cur = con.cursor()
		cur.execute("INSERT INTO races (name, type) VALUES (?, ?)", ('Sample Race', datapoint))
		con.commit()
		con.close()

	def run(self):
		while True:
			data = self.queue.get()
			self.log.info('Received data from queue "%s"', data)
			self.insert(data)
			#self.insert(data)
			self.dummy(data)
			self.queue.task_done()
