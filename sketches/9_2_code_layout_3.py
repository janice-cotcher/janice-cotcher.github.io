# Calculates the variance of a list of numbers


def calculate_variance(number_list):
  """Calculate the variance"""
  # calculate the mean of the list of numbers
  sum_list = 0
  for number in number_list:
    sum_list = sum_list + number
  mean = sum_list / len(number_list)
  # compute the sum of the mean of the square
  sum_squares = 0
  for number in number_list:
    sum_squares = sum_squares + number**2
  mean_squares = sum_squares / len(number_list)
  # return the variance
  return mean_squares - mean**2