#!/usr/bin/env ruby
def gravity(location, velocity)
	j = 0
	location.each do |main_planet|
		(0..2).each do |i|
			location.each do |orbiting_planet|
				if main_planet != orbiting_planet
					velocity[j][i] += compare(main_planet[i], orbiting_planet[i])
				end
			end
		end
		j += 1
	end
	return velocity
end

def compare(number1, number2)
	if number1 < number2
		return 1
	elsif number1 > number2
		return -1
	else
		return 0
	end
end

def combine(location, velocity)
	location += velocity
	return location
end

def energy(location, velocity)
	# nrg = pot * kin
	# pot = sum of pos XYZ
	# kin = sum of Vel xyz
	total_nrg = 0
	(0..3).each do |i|
		pot = 0
		kin = 0
		location[i].each do |p|
			pot += p.abs()
		end
		velocity[i].each do |v|
			kin += v.abs()
		end
		total_nrg += pot * kin
	end
	puts "Answer 1: #{total_nrg}"
	return total_nrg
end

puz = File.open("puz12")
locations = []
velocities = []
i = 0
puz.each_line do |line|
	j = 0
	locations[i] = []
	velocities[i] = []
	line = line.delete("<>").split(", ")
	line.each do |cord|
		cord = cord.split("=")
		locations[i][j] = cord[1].to_i
		velocities[i][j] = 0
		j += 1
	end
	i += 1
end

# locations = [[-1,0,2],[2,-10,-7],[4,-8,8],[3,5,-1]]
# locations = [[-8,-10,0],[5,5,10],[2,-7,3],[9,-8,-3]]
velocities = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

history = []
history.push("#{locations}#{velocities}")
i = 0
while true
	velocities = gravity(locations, velocities)
	locations = combine(locations, velocities)
	if history.include? "#{locations}#{velocities}"
		puts "Answer 2: #{i}"
		break
	end
	if i == 999
		energy(locations, velocities)
	end
	history.push("#{locations}#{velocities}")
	if i % 10000 == 0
		puts i if i != 0
	end
	# puts "#{i+1} #{locations}\n#{i+1} #{velocities}"
	i += 1
end

energy(locations, velocities)