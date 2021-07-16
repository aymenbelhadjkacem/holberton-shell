#!/usr/bin/env ruby
puts ARGV[0].scan(/(?<=from:)\+*\w+\]{0}/).join + "," + ARGV[0].scan(/(?<=to:)\+*\w+\]{0}/).join + "," + ARGV[0].scan(/(?<=flags:)(-1|0)(:)(-1|0|2)(:)(-1|0)(:)(-1|0)(:)(-1|0)/).join
