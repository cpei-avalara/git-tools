from setuptools import setup, find_packages

with open('requirements.txt') as fd:
    requires = fd.readlines()

setup(name='gittools',
      author='Lars Kellogg-Stedman',
      author_email='lars@oddbit.com',
      url='https://github.com/larsks/git-tools',
      version='0.2',
      packages=find_packages(),
      install_requires=requires,
      entry_points={'console_scripts': [
          'git-blob-created-at = gittools.blob_created_at:cli'
      ]})
