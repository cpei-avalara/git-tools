A collection of misc. git utilities.

## Installation

To install the current development version:

    pip install git+https://github.com/larsks/git-tools.git

## Utilities

### git-blob-created-at

This will tell you the date a blob was instantiated on your system, as
described in [this question][].

[this question]: http://stackoverflow.com/questions/38705793/how-can-i-determine-when-a-git-ref-was-created/38706590

Example:

    $ git blob-created-at 95902415ddfddcb7a48e7ed3d8391f60c6f4e53f
    2016-08-01 12:19:51

