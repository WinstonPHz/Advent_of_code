#!/usr/bin/env ruby
test = "1,1,1,4,99,5,6,0,99"
test = File.open("puz2").read
jump = 4
input = test.split(',').map {|chr| chr.to_i}
itr = 0
input[1] = 12
input[2] = 2
masterInput = input.clone
(0..99).each do |i|
	(0..99).each do |j|
		input = masterInput.clone
		input[1] = i
		input[2] = j
		itr = 0
		while input[itr] != 99 do
			if input[itr] == 1
				a = input[input[itr+1]]
				b = input[input[itr+2]]
				input[input[itr+3]] = a+b
			elsif input[itr] == 2
				a = input[input[itr+1]]
				b = input[input[itr+2]]
				input[input[itr+3]] = input[input[itr+1]]*input[input[itr+2]]
			end
			itr+=jump
		end
		#puts "i: #{i} j: #{j}, Ans: #{input[0]}"
		if input[0] == 19690720
			puts "Answer 2: #{100*i + j}"
		end
	end
end
puts "End of Program"
