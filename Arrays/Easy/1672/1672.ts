function maximumWealth(accounts: number[][]): number {
  let max: number = 0;
  for (let _ of accounts) {
    const wealth: number = _.reduce((a, b) => a + b, 0);
    max = Math.max(max, wealth);
  }
  return max;
}
