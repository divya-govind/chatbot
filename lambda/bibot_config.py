#
# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this
# software and associated documentation files (the "Software"), to deal in the Software
# without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

ORIGINAL_VALUE = 0
TOP_RESOLUTION = 1

SLOT_CONFIG = {
    'match_stage':       {'type': TOP_RESOLUTION, 'remember': True,  'error': 'I couldn\'t find an event called "{}".'}
}

DIMENSIONS = {
    'year':     {'slot': 'time_year',  'column': 'matches.year',  'singular': 'matches'},
    'month':     {'slot': 'time_month', 'column': 'matches.month',       'singular': 'matches'},
    'weekday':     {'slot': 'time_weekday',  'column': 'matches.weekday',  'singular': 'matches'},
    'city':     {'slot': 'venue_city',  'column': 'matches.city',  'singular': 'matches'},
    'country':     {'slot': 'venue_country', 'column': 'matches.country', 'singular': 'matches'},
    'stage': {'slot': 'match_stage',    'column': 'matches.stage',    'singular': 'matches'}
}



class SlotError(Exception):
    pass

