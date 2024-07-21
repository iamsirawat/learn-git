def is_prime(num):
  """Checks if a number is prime."""
  if num <= 1:
    return False
  if num <= 3:
    return True
  if num % 2 == 0 or num % 3 == 0:
    return False
  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6
  return True

def find_primes(limit):
  """Finds prime numbers up to a given limit."""
  primes = []
  for num in range(2, limit + 1):
    if is_prime(num):
      primes.append(num)
  return primes

# Find prime numbers from 1 to 100
primes = find_primes(100)
print(primes)