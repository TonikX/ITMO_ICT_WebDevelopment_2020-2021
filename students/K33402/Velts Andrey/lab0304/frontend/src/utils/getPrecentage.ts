export default function getPrecentage(
  partialValue: number,
  totalValue: number
): string {
  let calucation = Math.round((100 * partialValue) / totalValue);
  return `${calucation}%`;
}
