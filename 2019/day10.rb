#!/usr/bin/env ruby
## Functions
def unit_vector(p1,p2)
	# Where p = [x,y]
	# End goal here is to get a single unit vector, 
	# Point A is main point, Point B is reference point.
	dist_x = p2[0].to_f-p1[0].to_f
	dist_y = p2[1].to_f-p1[1].to_f
	dist_sum = dist_x.abs+dist_y.abs
	unit = [dist_x/dist_sum, dist_y/dist_sum]
	return unit
end

def polar_vector(p1,p2)
	# Where p = [x,y]
	# End goal here is to get a single unit vector, 
	# Point 1 is main point, Point 2 is reference point.
	dist_x = p2[0].to_f-p1[0].to_f
	dist_y = p2[1].to_f-p1[1].to_f
	dist_sum = dist_x.abs+dist_y.abs
	
	r = Math.sqrt(dist_x.abs**2 + dist_y.abs**2)
	unit = [dist_x/r, dist_y/r]
	theta = Math.acos(unit[1].abs)*180/(Math::PI)

	
	if dist_y == 0 && dist_x < 0
		theta = 270
	elsif dist_y == 0 && dist_x > 0
		theta = 90
	elsif dist_x == 0 && dist_y > 0
		theta = 180
	elsif dist_x == 0 && dist_y < 0
		theta = 0

	elsif dist_x > 0 && dist_y < 0
		theta += 0
	elsif dist_x > 0 && dist_y > 0
		theta = 180 - theta
	elsif dist_x < 0 && dist_y > 0
		theta += 180
	elsif dist_x < 0 && dist_y < 0
		theta = 360-theta
	end 
	r = r.round(6)
	theta = theta.round(6)
	return r, theta, unit
end

input = File.open("puz10").read
astroids = []
i = 0
puts "r\t012345678901234567890"
input.each_line do |line|
	j = 0
	puts "#{i}\t#{line}"
	line.split('').each do |point|
		if point == "#"
			astroids.push([j,i])
		end
		j+=1
	end
	i+=1
end

spotted = {}
astroids.each do |spaceport|
	num_spotted = []
	astroids.each do |astroid|
		vector = []
		vector = unit_vector(spaceport,astroid) unless spaceport == astroid
		if vector != []
			num_spotted.push(vector) unless num_spotted.include? vector
		end

	end
	spotted[spaceport] = num_spotted.length
end

maximum = [[0,0],0]
spotted.each do |key, value|
	maximum = [key,value] if value > maximum[1]
end

puts "#{maximum}"
laser = maximum[0]
num_hit = {}
astroids.each do |astroid|
	r = nil
	theta = nil
	r, theta, unit = polar_vector(laser,astroid) unless laser == astroid
	if unit!= nil
		if num_hit.include? unit
			num_hit[unit] = [r, astroid, theta, unit] if r < num_hit[unit][0]
		else
			num_hit[unit] = [r, astroid, theta, unit]
		end
	end
end

num_hit_order = {}
sorted_list = []
Hash[num_hit.sort].each do |key,value|
	sorted_list.push(value[2])
	num_hit_order[value[2]] = value

end
i = 1
Hash[num_hit_order.sort].each do |key, value|
	puts "#{value}" if i == 200
	i+=1
end
