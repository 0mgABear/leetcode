function kidsWithCandies(candies: number[], extraCandies: number): boolean[] {
  const maxCandies = Math.max(...candies);
  const result: boolean[] = [];

  for (const candy of candies) {
    result.push(candy + extraCandies >= maxCandies);
  }

  return result;
}
