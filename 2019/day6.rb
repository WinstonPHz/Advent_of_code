#!/usr/bin/env ruby
test = File.open("puz6").read
orbits = {}
planets = []
test.each_line do |line|
	p = line.split(')')
	a = p[0].strip
	b = p[1].strip
	orbits[b] = a
	planets.push(a) unless planets.include? a
	planets.push(b) unless planets.include? b
end
main_planets = []
planets.each do |main|
	main_planets.push(main) unless orbits.include? main
end

def orbit_search(planet, constilation)
	sum = 1
	if constilation.include? planet
		# puts "#{planet} orbits #{constilation[planet]}"
		sum += orbit_search(constilation[planet], constilation)
	else
		sum = 1
	end
	sum
end

def orbit_link(planet, constilation, first = 0)
	if first == 1
		sum = "First"
	else
		sum = planet
	end
	if constilation.include? planet
		#puts "#{planet} orbits #{constilation[planet]}"
		sum += "," + orbit_link(constilation[planet], constilation)
	end
	sum
end

checksum = 0
planets.each do |cur_planet|
	checksum += orbit_search(cur_planet, orbits)-1
end
puts "Answer 1: #{checksum}"
san = orbit_link("SAN", orbits, 1).split(',')
you = orbit_link("YOU", orbits, 1).split(',')
#puts "#{san}"
#puts "#{you}"
orbital_transfers = 0
san.each do |hops|
	orbital_transfers += 1 unless you.include? hops
end

you.each do |hops|
	orbital_transfers += 1 unless san.include? hops
end

puts "Answer 2: #{orbital_transfers}"