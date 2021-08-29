def max_sub_array(A):
  curr_max_sum = float('-inf')
  global_max = float('-inf')
  for i in A:
    curr_max_sum = max(curr_max_sum + i, i)
    global_max = max(curr_max_sum, global_max)
  return global_max
