/**
 * Returns the precentage of two numbers.
 *
 * @param partialValue- The part of the overall value
 * @param totalValue - The overall value
 * @returns The percentage of partialValue from totalValue
 *
 */
export default function getPrecentage(
  partialValue: number,
  totalValue: number
): string {
  let calucation = Math.round((100 * partialValue) / totalValue);
  return `${calucation}%`;
}
