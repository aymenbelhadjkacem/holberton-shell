#!/usr/bin/env ruby
#This script is to find the repetitiones token about a strin
#Any number of the preceding character is allowed (e.g. .* will match any 
#single-line string, including an empty string, and gets used a lot)
puts ARGV[0].scan(/^hbt*n$/).join
