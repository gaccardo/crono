import re

PARAMETERS = ['Number of clients accessing cache', 'Number of HTTP requests received',
              'Request failure ratio', 'Average HTTP requests per minute since start',
              'Hits as % of all requests', 'Memory hits as % of hit requests',
              'Disk hits as % of hit requests', 'Mean Object Size', 'Cache Misses',
              'Cache Hits']


class NonConvertibleValue(Exception):

    def __str__(self):
        return "This value is not recognized as squid status parameter"

    def __repr__(self):
        return "This value is not recognized as squid status parameter"


class SquidHealthHelper( object ):

    def get_squid_status(self):
        # Here must go the call to squid client
        # os.open('squidclient mgr:info')

        # Temporal
        status_file_pointer = open('mgr_status_sample.txt', 'r')
        status_buffer = status_file_pointer.readlines()
        status_file_pointer.close()

        return status_buffer

    def __process_non_numeric(self, key, value):
        if re.search('Hits as % of all requests', value[0]) or \
           re.search('Memory hits as % of hit requests', value[0]) or \
           re.search('Disk hits as % of hit requests', value[0]):

            min5 = float(value[2].split('%')[0].split(' ')[1])
            min60 = float(value[3].strip('%\n').split(' ')[1])

            return {'5min': min5, 'min60': min60}

        elif re.search('Mean Object Size', value[0]):
            return float(value[1].strip('KB\n '))

    def process_parameters(self, status):
        proccesed = list()

        for line in status:
            for param in PARAMETERS:
                if re.search(param, line):
                    key = ' '.join([line2 for line2 in line.split(':')[0].split(' ') if line2 != '' ])
                    try:
                        value = float(line.split(':')[1].split('\n')[0].split(' ')[-1])
                    except ValueError, e:
                        value = self.__process_non_numeric(key, line.split(':'))
                    proccesed.append( {key: value} )

        return proccesed

    def run(self):
        status = self.process_parameters(self.get_squid_status())
        print status
        

if __name__ == '__main__':
    shh = SquidHealthHelper()
    shh.run()
