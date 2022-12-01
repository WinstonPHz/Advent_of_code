#!/usr/bin/env ruby
width = 25
height = 6
test = File.open("puz8").read
input = test.split('').map {|chr| chr.to_i}
card_stack = []
j = 0
i = -1
while input.length >0
	if j % (width*height) == 0
		i+=1
		card_stack[i] = []
	end
	card_stack[i].push(input.shift)
	j+=1
end

def part1(stack)
	zero = []
	stack.each do |layer|
		zero.push(layer.count(0))
	end
	leastLayer = zero.index(zero.min)
	puts " Answer 1: #{stack[leastLayer].count(1)*stack[leastLayer].count(2)}"
end

message = Array.new width*height, "."

def printlayer(card, width)
	(1..card.length).each do |value|
		print card[value-1]
		print "\n" if value % width == 0
	end
end


part1(card_stack)

card_stack.each do |layer|
	i = 0
	layer.each do |value|
		if message[i] == "."
			message[i] = "-" if value == 0
			message[i] = "8" if value == 1
		end
		i += 1
	end
end

printlayer(message, width)
