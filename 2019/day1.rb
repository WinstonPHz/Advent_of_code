#!/usr/bin/env ruby
line_num=0
text=File.open('puz1').read
fuel = 0
text.each_line do |line|
  modfuel = 0
  ffuel = (line.to_i/3)-2
  while ffuel > 0 do
	modfuel += ffuel
	ffuel = (ffuel/3) - 2
  end
  fuel += modfuel
end
puts fuel