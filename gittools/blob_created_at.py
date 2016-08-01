#!/usr/bin/env python

import click
import logging
import pathlib2 as pathlib
import os
import sh
import time

GIT = sh.git
LOG = logging.getLogger()
DEFAULT_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def find_loose_object(topdir, hash):
    objpath = topdir / '.git' / 'objects' / hash[:2] / hash[2:]
    if objpath.is_file():
        return objpath


def find_packfile(topdir, want):
    packdir = topdir / '.git' / 'objects' / 'pack'
    for idx in packdir.glob('*.idx'):
        LOG.info('inspecting packfile: %s', idx)
        with idx.open('rb') as fd:
            objects  = GIT('show-index', _in=fd)
            for line in objects.splitlines():
                offset, hash = line.split()[:2]
                if hash == want:
                    return idx


@click.command()
@click.option('-v', '--verbose', 'loglevel', flag_value='INFO')
@click.option('-d', '--debug', 'loglevel', flag_value='DEBUG')
@click.option('-f', '--format', default='%Y-%m-%d %H:%M:%S',
              help='format string for strftime '
              '(default is "%s")' % DEFAULT_TIME_FORMAT)
@click.argument('hash')
def cli(hash, loglevel='WARNING', format=None):
    logging.basicConfig(level=loglevel)
    if loglevel != 'DEBUG':
        logging.getLogger('sh').setLevel('WARNING')

    try:
        res = GIT('rev-parse', '--show-toplevel')
        topdir = pathlib.Path(res.splitlines()[0])
        LOG.info('found repository toplvel at: %s', topdir)

        res = GIT('rev-parse', '--verify', hash)
        valid_hash = res.splitlines()[0]
        LOG.info('looking for content hash: %s', valid_hash)
    except sh.ErrorReturnCode as err:
        raise click.ClickException(err.stderr)

    for func in find_loose_object, find_packfile:
        target = func(topdir, valid_hash)
        if target is not None:
            break
    else:
        raise click.ClickException('unable to find object id %s' % valid_hash)

    s = os.stat(str(target))
    print time.strftime(format, time.localtime(s.st_mtime))

if __name__ == '__main__':
    cli()
