function validMountainArray(arr: number[]): boolean {
  let left: number = 0;
  let right: number = arr.length - 1;
  if (arr.length < 3) {
    return false;
  }
  while (left < right && arr[left] < arr[left + 1]) {
    left += 1;
  }
  while (right > 0 && arr[right - 1] > arr[right]) {
    right -= 1;
  }

  return left === right && left !== 0 && right !== arr.length - 1;
}
