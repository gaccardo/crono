#!/usr/bin/env python

class HttpAccess( object ):

	def __init__(self, permission, acl):
		self.permission = permission
		self.acl = acl

	def __str__(self):
		return "<HttpAccess(permission=%s, acl=%s)>" % (self.permission, 
			                                              self.acl)

	def get_permission(self):
		return self.permission

	def get_acl(self):
		return self.acl

	def set_permission(self, permission):
		self.permission = permission

	def set_acl(self, acl):
		self.acl = acl


class SafePort( object ):

	def __init__(self, acl, port):
		self.acl = acl
		self.port = port

	def __str__(self):
		return "<SafePort(acl=%s, port=%s)>" % (self.acl, self.port)

	def get_acl(self):
		return self.acl

	def get_port(self):
		return self.port

	def set_acl(self, acl):
		self.acl = acl

	def set_port(self, port):
		self.port = port


class Network( object ):

	def __init__(self, name, new):
		self.name = name
		self.new = new

	def __str__(self):
		return "<Network(name=%s, new=%s)>" % (self.name, self.new)

	def get_name(self):
		return self.name

	def get_new(self):
		return self.new

	def set_name(self, name):
		self.name = name

	def set_new(self, new):
		self.new = new


class SquidConfigParser( object ):

	def __init__(self):
		self.configfile_path = 'new_squid.conf'
		self.actual_section = None
		self.sections = dict()

	def __get_configfile_content(self):
		configfile_pointer = open(self.configfile_path, 'r')
		configfile_content = configfile_pointer.readlines()
		configfile_pointer.close()

		return configfile_content

	def __get_sections(self, config_raw):
		for line in config_raw:
			if line.startswith('#'):
				if line.split(' ')[1] == 'init':
					self.actual_section = line.split(' ')[2].strip('\n')
					self.sections[self.actual_section] = list()

			if not line.startswith('#') and self.actual_section is not None:
				self.sections[self.actual_section].append(line.strip('\n'))

			if line.startswith('#') and self.actual_section is not None:
				if line.split(' ')[1] == 'end':
					self.actual_section = None

	def __get_config(self):
		new_sections = {'httpaccess': list(),
		                'safeports': list(),
		                'networks': list()}
		for section in self.sections:
			if section == "httpaccess":
				for entry in self.sections[section]:
					ee = entry.split(' ')
					new_sections['httpaccess'].append(HttpAccess(ee[1], ee[2]))
			if section == "safeports":
				for entry in self.sections[section]:
					ee = entry.split(' ')
					new_sections['safeports'].append(SafePort(ee[1], ee[3].split('\t')[0]))
			if section == "networks":
				for entry in self.sections[section]:
					ee = entry.split(' ')
					new_sections['networks'].append(Network(ee[1], ee[3]))

		return new_sections

	def __generate_json(self, config):
		output = dict()
		output['safeports'] = list()
		output['httpaccess'] = list()
		output['networks'] = list()

		for entry in config['safeports']:
			output['safeports'].append({'acl': entry.get_acl(),
				                          'port': entry.get_port()})

		for entry in config['httpaccess']:
			output['httpaccess'].append({'permission': entry.get_permission(),
				                          'acl': entry.get_acl()})

		for entry in config['networks']:
			output['networks'].append({'name': entry.get_name(),
				                         'net': entry.get_new()})

		return output

	def run(self):
		config_raw = self.__get_configfile_content()
		config = self.__get_sections(config_raw)
		config = self.__get_config()
		config = self.__generate_json(config)


if __name__ == '__main__':
	scp = SquidConfigParser()
	scp.run()