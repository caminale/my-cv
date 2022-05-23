#!/usr/bin/env python

import os
import sys

SCRIPT_DIR = os.path.realpath(os.path.join(__file__, '..'))
ROOT_DIR = os.path.realpath(os.path.join(SCRIPT_DIR, '..'))


def main(arguments):
  os.chdir(ROOT_DIR)
  _system('pip install awscli')
  _system('aws s3 sync public/ s3://loic-cam-cv')

# BOILERPLATE TO REPRODUCE -ex behavior of bash

def _system(cmd, logged = True):
  if logged:
    print('$ {0}'.format(cmd))

  output = os.system(cmd)

  # see : https://stackoverflow.com/a/6466753
  error_code = output >> 8
  if error_code > 0:
    raise OSError(error_code)

if __name__ == '__main__':
  try:
    main(sys.argv[1:])
  except (OSError) as e:
    sys.exit(e.args[0])
