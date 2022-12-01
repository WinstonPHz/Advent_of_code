#!/usr/bin/env ruby
min = 193651
max = 649729

possibles = []

doubles = ["00","11","22","33","44","55","66","77","88","99"]
(min..max).each do |try|
	code = try.to_s
	con = true
	j = -1
	doubles.each do |double|
		j += 1
		#puts "Trying #{j}"
		multiple = false
		numbers_in_a_row = 0
		if code.include? double
			consecutive = code.split('').map {|digit| digit.to_i }
			numbers_in_a_row += 1 if consecutive[0] == j
			(1..consecutive.length-1).each do |i|
				if consecutive[i] < consecutive[i-1]
					con = false
					break
				end
				if consecutive[i] == j
					numbers_in_a_row += 1
					if numbers_in_a_row > 2
						#puts "Too many #{j} in a row #{numbers_in_a_row}"
						multiple = true
						
					end
				end
			end
			next if multiple
			if con == true
				possibles.push(code) 
				break
			end
		end
	end
end
puts "pos: #{possibles.length}"