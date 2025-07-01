function runningSum(nums: number[]): number[] {
  let sum: number = 0;
  let output: number[] = [];
  for (let _ of nums) {
    sum += _;
    output.push(sum);
  }
  return output;
}
