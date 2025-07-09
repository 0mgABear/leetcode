function countMatches(
  items: string[][],
  ruleKey: string,
  ruleValue: string
): number {
  let output: number = 0;
  const map: { [key: string]: number } = {
    type: 0,
    color: 1,
    name: 2,
  };

  const index = map[ruleKey];

  for (const item of items) {
    if (item[index] === ruleValue) {
      output++;
    }
  }

  return output;
}
