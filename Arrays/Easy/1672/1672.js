var maximumWealth = function (accounts) {
  let max = 0;
  for (let _ of accounts) {
    const wealth = _.reduce((a, b) => a + b, 0);
    max = Math.max(max, wealth);
  }

  return max;
};
