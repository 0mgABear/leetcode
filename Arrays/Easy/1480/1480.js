var runningSum = function (nums) {
  let sum = 0;
  let output = [];
  for (let _ of nums) {
    sum += _;
    output.push(sum);
  }
  return output;
};
