import { fromUnixTime } from "date-fns";

/**
 * Parsing a unix timestamp to date.
 *
 * @param date - Date in unix timestamp
 * @returns The Date object
 *
 */
const parseUnix = (date: string): Date => {
  return fromUnixTime(parseInt(date));
};

export default parseUnix;
