import os
import logging
import threading
import re
import glob
import sys

from pathlib import Path


try:
	root_dir = f'{os.path.expanduser("~")}'
	os.makedirs(f'{root_dir}/crest')
	os.makedirs(f'{root_dir}/crest/data')
except OSError:
	pass

working_dir = f'{root_dir}/crest'
data_dir = f'{working_dir}/data'
log_file = f"{working_dir}/search_results.log"


file_handler = logging.FileHandler(filename=log_file)
stdout_handler = logging.StreamHandler(stream=sys.stdout)
handlers = [file_handler, stdout_handler]

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s - CDS Keyword found in file: %(message)s',
    handlers=handlers
)

logger = logging.getLogger('LOGGER_NAME')


class FileManagementSystem:
	def __init__(self):
		self.last_run_file_name = f"{working_dir}/last_run"
		Path(self.last_run_file_name).touch()

	def __enter__(self):
		self.last_run_time_stamp = self.get_last_run_file_time_stamp()
		print(f"Last Processed File Time Stamp: {self.last_run_time_stamp}")
		return self

	def __exit__(self, exc_type, exc_value, exc_traceback):
		pass

	def get_files_by_time_stamp(self, time_stamp):
		files = glob.glob(f"{data_dir}/{time_stamp}_*")
		return files

	def get_all_time_stamp(self):
		all_files = os.listdir(data_dir)
		uniq_time_stamp = [file.split('_')[0] for file in all_files]
		return sorted(list(set(uniq_time_stamp)))

	def get_unprocessed_time_stamp(self):
		time_stamps = self.get_all_time_stamp()
		print(f"All Time Stamps: {time_stamps}")
		if not self.last_run_time_stamp:
			return time_stamps
		
		unprocessed = []
		for i in time_stamps:
			if int(i) > int(self.last_run_time_stamp):
				unprocessed.append(i)
		print(f"Unprocessed: {unprocessed}")
		return sorted(unprocessed)

	def process(self):
		unprocessed = self.get_unprocessed_time_stamp()
		if unprocessed:
			self.read_files_by_time_stamp(unprocessed)
			self.set_last_run_file_time_stamp(unprocessed[-1])

	def read_files_by_time_stamp(self, time_stamps):
		for stamp in time_stamps:
			files = self.get_files_by_time_stamp(stamp)
			for file in files:
				content = self.read_file(file)
				if "CDS" == content:
					logger.info(file)

	def read_file(self, file):
		with open(file, "r+") as f:
			content = f.readline()
		return content

	def set_last_run_file_time_stamp(self, time_stamp):
		print(f"Last Processed: {time_stamp}")
		with open(self.last_run_file_name, "w") as file:
			file.write(time_stamp)

	def get_last_run_file_time_stamp(self):
		return self.read_file(self.last_run_file_name)


with FileManagementSystem() as f:
	f.process()