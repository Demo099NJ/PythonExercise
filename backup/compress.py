import os
import time

def compress(sour_path, tar_path):
	source = [sour_path]

	target_dir = tar_path

	target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

	if not os.path.exists(target_dir):
		os.mkdir(target_dir)

	zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

	print 'Zip command is:', zip_command
	print 'Running:'

	if os.system(zip_command) == 0:
		print 'Successful backup to', target
	else:
		print 'Backup FAILED'

def process():
	source = raw_input("source file name: ")
	target = raw_input("target file name: ")
	#print('source = {}, target = {}'.format(source, target))
	compress(source, target)

process()
