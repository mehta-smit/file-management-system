import os
import threading
import random

from datetime import datetime
from uuid import uuid4

try:
	root_dir = f'{os.path.expanduser("~")}'
	os.makedirs(f'{root_dir}/crest')
	os.makedirs(f'{root_dir}/crest/data')
except OSError:
	pass
working_dir = f'{root_dir}/crest/data'

class PseudoRandomWriter:
	def __init__(self, interval):
		self._interval = interval

	def __enter__(self):
		self.refresh_current_timestamp()
		return self

	def __exit__(self, exc_type, exc_value, exc_traceback):
		pass

	def refresh_current_timestamp(self):
		self.current_timestamp = int(datetime.timestamp(datetime.now()))

	def uuid4(self):
		return "".join(str(uuid4()).split('-'))

	@property
	def file_name(self):
		return f"{working_dir}/{str(self.current_timestamp)}_{self.uuid4()}"

	def _generate_random_string(self):
		probability = random.choice((0, 1))
		if probability:
			return "CDS"
		else:
			return "".join([chr(random.randint(65,90)) for i in range(3)])

	def writing(self):
		file = open(self.file_name, "w+")
		file.write(self._generate_random_string())
		file.close()

	def write(self):
		for i in range(100):
			self.writing()

with PseudoRandomWriter(5) as f:
	f.write()