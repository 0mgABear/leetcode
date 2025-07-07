function maxArea(height: number[]): number {
  let left: number = 0;
  let right: number = height.length - 1;
  let maxArea: number = 0;

  while (left < right) {
    const h: number = Math.min(height[left], height[right]);
    const w: number = right - left;
    const area: number = h * w;
    maxArea = Math.max(maxArea, area);

    if (height[left] < height[right]) {
      left++;
    } else {
      right--;
    }
  }

  return maxArea;
}
