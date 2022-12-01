#!/usr/bin/env ruby
text=File.open('puz3').read
#text = "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83"
#text = "R8,U5,L5,D3\nU7,R6,D4,L4"
i = 0
wire = [[],[]]
text.each_line do |line|
	wire[i] = line.split(',')	
	i+= 1
end

def intersect (horizontal, vertical)
	# Format [[x1, y1][x2 y2] length]
	
	if horizontal[0][0] > horizontal[1][0]
		small_hor = horizontal[1][0]
		large_hor = horizontal[0][0]
		hor_dir = false
	else
		large_hor = horizontal[1][0]
		small_hor = horizontal[0][0]
		hor_dir = true
	end
	if vertical[0][0].between?(small_hor, large_hor)
		puts "X within Segment #{horizontal[0][0]}, #{horizontal[1][0]}, #{vertical[0][0]}"
		if vertical[0][1] > vertical[1][1]
			large_vrt = vertical[0][1]
			small_vrt = vertical[1][1]
			vrt_dir = false
		else
			small_vrt = vertical[0][1]
			large_vrt = vertical[1][1]
			vrt_dir = true
		end
		if horizontal[0][1].between?(small_vrt, large_vrt)
			puts "Intersection at #{vertical[0][0]}, #{horizontal[0][1]}"
			puts "Lengths so far: #{horizontal[2]}, #{vertical[2]}"
			if hor_dir
				hor_nub = large_hor - vertical[0][0] 
			else
				hor_nub = vertical[0][0] - small_hor
			end
			if vrt_dir
				vrt_nub = large_vrt - horizontal[0][1]
			else
				vrt_nub = horizontal[0][1] - small_vrt
			end
			horizontal[2] - hor_nub + vertical[2] - vrt_nub
		else
			 0
		end
	else
		0
	end
end

horiz = []
vert = []
length = 0
cur_x = 0
cur_y = 0
wire[0].each do |direction|
	a = Array[cur_x,cur_y]
	length += direction[1..-1].to_i
	if direction[0] == "R"
		cur_x += direction[1..-1].to_i
		b = Array[cur_x, cur_y]
		c = Array[a, b, length]
		horiz.push(c)
	elsif direction[0] == "L"
		cur_x -= direction[1..-1].to_i
		b = Array[cur_x, cur_y]
		c = Array[a, b, length]
		horiz.push(c)
	elsif direction[0] == "U"
		cur_y += direction[1..-1].to_i
		b = Array[cur_x, cur_y]
		c = Array[a, b, length]
		vert.push(c)
	elsif direction[0] == "D"
		cur_y -= direction[1..-1].to_i
		b = Array[cur_x, cur_y]
		c = Array[a, b, length]
		vert.push(c)
	end
end

puts "Horiz: #{horiz}"
puts "Vert: #{vert}"
length = 0
cur_x = 0
cur_y = 0
man_dist = []
wire[1].each do |direction|
	a = Array[cur_x,cur_y]
	length += direction[1..-1].to_i
	if direction[0] == "R"
		cur_x += direction[1..-1].to_i
		b = Array[cur_x, cur_y]
		c = [a, b, length]
		vert.each do |segment|
			man_dis = intersect(c, segment)
			puts "Returned: #{man_dis}" if man_dis > 0
			man_dist.push(man_dis) if man_dis > 0
		end
	elsif direction[0] == "L"
		cur_x -= direction[1..-1].to_i
		b = Array[cur_x, cur_y]
		c = [a, b, length]
		vert.each do |segment|
			man_dis = intersect(c, segment)
			puts "Returned: #{man_dis}" if man_dis > 0
			man_dist.push(man_dis) if man_dis > 0
		end
	elsif direction[0] == "U"
		cur_y += direction[1..-1].to_i
		b = Array[cur_x, cur_y]
		c = [a, b, length]
		horiz.each do |segment|
			man_dis = intersect(segment, c)
			puts "Returned: #{man_dis}" if man_dis > 0
			man_dist.push(man_dis) if man_dis > 0
		end
	elsif direction[0] == "D"
		cur_y -= direction[1..-1].to_i
		b = Array[cur_x, cur_y]
		c = [a, b, length]
		horiz.each do |segment|
			man_dis = intersect(segment, c)
			puts "Returned: #{man_dis}" if man_dis > 0
			man_dist.push(man_dis) if man_dis > 0
		end
	end
end
puts "All: #{man_dist}"
puts "Distances: #{man_dist.min()}"