export function formatPixelRow(values) {
  return values.map((value) => value.toFixed(2)).join(", ");
}
