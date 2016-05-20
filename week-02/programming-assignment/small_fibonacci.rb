
def small_fibonacci(n)
  fib_list(n)
end

def large_fibonacci_last_digit(n)
  fib_list(n) % 10
end

def fib_list(n)
  table = Array.new(n+1)
  table.each_with_index do |x,i|
    if i == 0 or i == 1
      table[i] = i
    else
      table[i] = table[i-1] + table[i-2]
    end
  end
  table[n]
end
