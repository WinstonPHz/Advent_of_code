#!/usr/bin/env ruby

def computer(input_code)
	#test = "3,9,8,9,10,9,4,9,99,-1,8"
	test = File.open("puz5").read
	input = test.split(',').map {|chr| chr.to_i}
	itr = 0
	while input[itr] != 99 do
		opscode = input[itr].to_s
		code = opscode[-1] 
		#puts "Opscode: #{opscode}, Code: #{code}"
		a = input[input[itr+1]]
		a = input[itr+1] if opscode[-3] == "1"
		b = input[input[itr+2]]
		b = input[itr+2] if opscode[-4] == "1"
		if code.to_i == 1
			input[input[itr+3]] = a+b
			itr += 4
		elsif code.to_i == 2
			input[input[itr+3]] = a*b
			itr += 4
		elsif code.to_i == 3
			# takes and input and puts it in input[input[itr+1]]
			input[input[itr+1]] = input_code
			itr += 2
		elsif code.to_i == 4
			# takes and outputs input[input[itr+1]]
			puts "Outputing: #{a}"
			itr += 2
		elsif code.to_i == 5
			# Jump if True
			if a != 0
				itr = b
			else
				itr += 3
			end
		elsif code.to_i == 6
			# Jump if False
			if a == 0
				itr = b
			else
				itr += 3
			end
		elsif code.to_i == 7
			# less than:
			input[input[itr+3]] = 0
			input[input[itr+3]] = 1 if a < b
			itr += 4
		elsif code.to_i == 8
			# Equals
			input[input[itr+3]] = 0
			input[input[itr+3]] = 1 if a == b
			itr += 4
		end
	end
end

computer(5)

puts "End of Program"