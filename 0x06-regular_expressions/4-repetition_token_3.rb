#!/usr/bin/env ruby
# Matches a string with hb followed by 0 or more occurences of t

puts ARGV[0].scan(/hbt*n/).join
