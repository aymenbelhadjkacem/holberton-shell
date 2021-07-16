#!/usr/bin/env ruby
#This script is to find the repetitiones token about a string
#Matches any single character (except newlines, normally)
#Here is used a quantifiers {}
puts ARGV[0].scan(/^h.{1}n$/).join
