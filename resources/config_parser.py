#!/usr/bin/env python


class SquidConfigParser( object ):

	def __init__(self):
		self.configfile_path = 'new_squid.conf'
		self.actual_section = None

	def __get_configfile_content(self):
		configfile_pointer = open(self.configfile_path, 'r')
		configfile_content = configfile_pointer.readlines()
		configfile_pointer.close()

		return configfile_content

	def __get_sections(self, config_raw):
		for line in config_raw:
			if line.startswith('#'):
				if line.split(' ')[1] == 'init':
					print "Init: %s" % line.split(' ')[2].strip('\n')
					self.actual_section = line.split(' ')[2].strip('\n')

			if not line.startswith('#') and self.actual_section is not None:
				print "  %s --> %s" % (self.actual_section, line.strip('\n'))

			if line.startswith('#') and self.actual_section is not None:
				if line.split(' ')[1] == 'end':
					print "End: %s" % self.actual_section.strip('\n')
					self.actual_section = None

	def run(self):
		config_raw = self.__get_configfile_content()
		config = self.__get_sections(config_raw)


if __name__ == '__main__':
	scp = SquidConfigParser()
	scp.run()