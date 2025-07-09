function numJewelsInStones(jewels: string, stones: string): number {
  let hash: Record<string, number> = {};
  let output: number = 0;
  for (const char of jewels) {
    hash[char] = 1;
  }
  for (const char of stones) {
    if (hash[char]) {
      output += 1;
    }
  }
  return output;
}
