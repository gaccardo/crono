#!/usr/bin/env python

squidfile_p = open('squid.conf', 'r')
squidfile = squidfile_p.readlines()
squidfile_p.close()

squidfile_p = open('new_squid.conf', 'w')
lines = list()

for line in squidfile:
  if not line.startswith('#') and line != '\n':
    squidfile_p.write(line)

squidfile_p.close()
