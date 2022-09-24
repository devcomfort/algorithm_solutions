function squareSum(numbers) {
  return numbers.reduce((acc, cur) => acc + cur ** 2, 0);
}
