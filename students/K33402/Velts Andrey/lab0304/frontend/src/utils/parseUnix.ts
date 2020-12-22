import { fromUnixTime } from "date-fns";

const parseUnix = (date: string): Date => {
  return fromUnixTime(parseInt(date));
};

export default parseUnix;
