#!/usr/bin/env ruby
def computer(input_code, itr, input)
	# Example comuter([1,255], 0)
	#test = "3,9,8,9,10,9,4,9,99,-1,8"
	relative_base = 0
	while input[itr] != 99 do
		opscode = input[itr].to_s
		code = opscode[-1] 
		
		#puts "Opscode: #{opscode}, Code: #{code}"
		a = input[input[itr+1]]
		a = input[itr+1] if opscode[-3] == "1"
		a = input[relative_base+input[itr+1]] if opscode[-3] == "2"
		b = input[input[itr+2]]
		b = input[itr+2] if opscode[-4] == "1"
		b = input[relative_base+input[itr+2]] if opscode[-4] == "2"
		c = input[itr+3]
		c = input[itr+3] if opscode[-5] == "1"
		c = relative_base+input[itr+3] if opscode[-5] == "2"
		a = 0 if a == nil
		b = 0 if b == nil
		c = 0 if c == nil

		if code.to_i == 1
			input[c] = a+b
			itr += 4
		elsif code.to_i == 2
			input[c] = a*b
			itr += 4
		elsif code.to_i == 3
			# takes and input and puts it in input[input[itr+1]]
			puts "Not Enough Elements in array" if input_code == []
			input[c] = input_code.shift
			itr += 2
		elsif code.to_i == 4
			# takes and outputs input[input[itr+1]]
			puts "#{a}"
			itr += 2
			# return a, itr, input
			
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
			input[c] = 0
			input[c] = 1 if a < b
			itr += 4
		elsif code.to_i == 8
			# Equals
			input[c] = 0
			input[c] = 1 if a == b
			itr += 4
		elsif code.to_i == 9
			relative_base += a
			itr += 2
		end
	end
	#puts "Exiting computer"
	#return input_code.shift, -1, input
end

test = File.open("puz9").read
code = test.split(',').map {|chr| chr.to_i}
step = 0
puts "Answer 1: #{}"
computer([1],step,code.clone)
puts "Answer 2: #{}"
computer([2],step,code.clone)
