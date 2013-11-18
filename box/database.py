import threading
import Queue
import sqlite3
import logging

class Database(threading.Thread):

	def __init__(self, queue):
		threading.Thread.__init__(self)
		self.queue = queue
		self.daemon = True
		
		self.log = logging.getLogger(__name__)

		#self.con = sqlite3.connect('box.db')
		#self.cur = self.con.cursor()

		#self._check_schema()

	def _check_schema(self):
		self.cur.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='points';")
		exists = self.cur.fetchone()[0];
		if exists != 1: 
			self._create_schema()

	def _create_schema(self):
		f = open('box/schema.sql','r')
		sql = f.read()
		print sql
		self.cur.executescript(sql)

	def insert(self, datapoint):
		con = sqlite3.connect('box.db')
		cur = con.cursor()
		cur.execute("INSERT INTO points(speed) VALUES (?)", (123,))
		con.close()

	def run(self):
		while True:
			data = self.queue.get()
			self.insert(data)
			self.queue.task_done()
