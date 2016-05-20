
require_relative '../small_fibonacci.rb'

describe "Small Fibonacci Sample 1:" do
  n = 3
  it "#{n}" do
    expect(small_fibonacci(n)).to eql(2)
  end
end

describe "Small Fibonacci Sample 2:" do
  n = 10
  it "#{n}" do
    expect(small_fibonacci(n)).to eql(55)
  end
end

describe "Large Fibonacci Last Digit Sample 1:" do
  n = 3
  it "#{n}" do
    expect(large_fibonacci_last_digit(n)).to eql(2)
  end
end

describe "Large Fibonacci Last Digit Sample 2:" do
  n = 327305
  it "#{n}" do
    expect(large_fibonacci_last_digit(n)).to eql(5)
  end
end
