function numIdenticalPairs(nums: number[]): number {
  let output = 0;
  const countMap: Record<number, number> = {};

  for (const num of nums) {
    if (countMap[num] === undefined) {
      countMap[num] = 1;
    } else {
      countMap[num]++;
    }
  }

  for (const count of Object.values(countMap)) {
    if (count > 1) {
      output += (count * (count - 1)) / 2;
    }
  }

  return output;
}
