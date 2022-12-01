#!/usr/bin/env ruby
def computer(input_code, itr, input)
	# Example comuter([1,255], 0)
	#test = "3,9,8,9,10,9,4,9,99,-1,8"
	out = 0
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
			puts "Not Enough Elements in array" if input_code == []
			input[input[itr+1]] = input_code.shift
			itr += 2
		elsif code.to_i == 4
			# takes and outputs input[input[itr+1]]
			# puts "Outputing: #{a}"
			itr += 2
			return a, itr, input
			
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
	return input_code.shift, -1, input
end

possibles = []
phase_seq = [5,6,7,8,9]
phase_sequences = phase_seq.permutation(5).to_a
test = File.open("puz7").read
input = test.split(',').map {|chr| chr.to_i}

phase_sequences.each do |seq|
	amp = 0
	computer_code = []
	phase_seq.each do |esq|	
		computer_code.push(input.clone)
	end
	command_number = [0,0,0,0,0]
	(0..4).each do |i|
		amp, command_number[i], computer_code[i] = computer([seq[i], amp], command_number[i], computer_code[i])
	end
	while command_number[4]>-1
		(0..4).each do |i|
			amp, command_number[i], computer_code[i] = computer([amp], command_number[i], computer_code[i])
		end
	end
	possibles.push(amp)
	#puts "Checked #{seq}"
end

puts "End of Program #{possibles.max}"