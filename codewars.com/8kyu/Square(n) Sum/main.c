#include <stddef.h>

int square_sum(const int *values, size_t count)
{
  int result = 0;
  for (int i = 0; i < count; result += values[i] * values[i], i++)
    ;
  return result;
}
