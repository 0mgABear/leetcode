function rob(nums: number[]): number {
  let prev: number = 0;
  let curr: number = 0;
  for (const num of nums) {
    const temp = curr;
    curr = Math.max(curr, prev + num);
    prev = temp;
  }
  return curr;
}
