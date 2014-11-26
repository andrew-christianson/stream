
"""Stream is three things

(1) A stream wrapper around data including CSV, SQL queries, Arbitrary
text files, and other comon large on disk file formats.  It offers
(will offer) a performant approach for interating through those data
sources using a common interface.  It aims to utilize the full
bandwidth of the underlying storage (e.g., if your disk will read at
50MB/s, stream should proccess files at 50MB/s)

(2) A library of common statistical functions starting streams.

(3) Primarily a learning exercise for me in writing statistical code
from the ground up.  After all, you never really understand someting
until you've written code that does it.

For now, stream targets the data analyst who might use R and Python,
but complain that they lack out-of-core data support and rever to SAS
for larger data.  It does not attempt to tackle the problems facing
true 'Big Data' problems. Instead, it attempts to provide some useful
abstractions and utilities for the desktop analyst working with data
that is, for whatever reason, larger than main memory.  """
from . import stream
from .test import *
