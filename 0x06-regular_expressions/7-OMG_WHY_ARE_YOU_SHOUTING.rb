#!/usr/bin/env ruby
# The regular expression must match a 10 digit phone number
# \d === Most engines: one digit from 0 to 9
puts ARGV[0].scan(/[A-Z]/).join
