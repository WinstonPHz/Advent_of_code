#!/usr/bin/env ruby
def computer(input_code, itr, input, relative_base)
	# Example comuter([1,255], 0)
	#test = "3,9,8,9,10,9,4,9,99,-1,8"
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
			return a, itr, input, relative_base
			
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
	return input_code.shift, -1, input
end

def move(rotate, cur_location, cur_orien)
	# Rotate the orientation
	if rotate == 1
		cur_orien += 1
		cur_orien -= 4 if cur_orien > 3
	elsif rotate == 0
		cur_orien -= 1
		cur_orien += 4 if cur_orien < 0
	end
	# Then move
	if cur_orien == 0
		cur_location = [cur_location[0],cur_location[1]-1]
	elsif cur_orien == 1
		cur_location = [cur_location[0]+1,cur_location[1]]
	elsif cur_orien == 2
		cur_location = [cur_location[0],cur_location[1]+1]
	elsif cur_orien == 3
		cur_location = [cur_location[0]-1,cur_location[1]]
	end
	# Now return location and orientation
	return cur_location, cur_orien
end

def print_pritty(x,y,cordinates,local,dir)
	system "clear"
	print "\n"
	(y[0]..y[1]).each do |y1|
		(x[0]..x[1]).each do |x1|
			if [x1,y1] == local
				if dir == 0
					print "^"
				elsif dir == 1
					print ">"
				elsif dir == 2
					print "v"
				elsif dir == 3
					print "<"
				end
			else
				if cordinates.include? [x1,y1]
					print cordinates[[x1,y1]]
				else
					print " "
				end
			end
		end
		print "\n"
	end
	sleep(1/5)
end

rb = 0
orientation = 0
location = [0,0]
hull = {}
hull[location] = " "
test = File.open("puz11").read
com_code = test.split(',').map {|chr| chr.to_i}
step = 0
x_cord = [0,0]
y_cord = [0,0]

while step >= 0
	color = 0
	if hull.include? location
		color = 1 if hull[location] == "#" || step == 0
	end
	val1,step,com_code,rb = computer([color],step,com_code.clone,rb)
	val2,step,com_code,rb = computer([],step,com_code.clone,rb) if step >= 0
	#puts "Painting: #{val1}, #{location}"
	hull[location] = "#" if val1 == 1 && step >= 0
	hull[location] = " " if val1 == 0 && step >= 0
	location, orientation = move(val2,location,orientation) if step >= 0
	x_cord[0] = location[0] if location[0] < x_cord[0]
	x_cord[1] = location[0] if location[0] > x_cord[1]
	y_cord[0] = location[1] if location[1] < y_cord[0]
	y_cord[1] = location[1] if location[1] > y_cord[1]
	# puts "Moved to: #{val2}, #{location}, #{orientation}, on step: #{step}"
	print_pritty(x_cord,y_cord,hull,location,orientation)
end

tile_count = 0
hull.each do |key, value|
	tile_count += 1 if value == "#"
end
puts hull.length
