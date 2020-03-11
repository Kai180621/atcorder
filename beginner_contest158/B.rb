line = gets.split(' ').map(&:to_i)

quotient = line[0] / (line[1]+line[2])
surplus = line[0] % (line[1]+line[2])

ans = quotient * line[1]

if surplus <= line[1]
  ans += surplus
else
  ans += line[1]
end

p ans