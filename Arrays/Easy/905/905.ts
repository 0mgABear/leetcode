function sortArrayByParity(nums: number[]): number[] {
  return nums.filter((n) => n % 2 == 0).concat(nums.filter((n) => n % 2 != 0));
}
