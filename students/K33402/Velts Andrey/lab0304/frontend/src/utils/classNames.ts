export interface ObjectClassNames {
  [index: string]: boolean;
}

export type ClassName =
  | number
  | string
  | ObjectClassNames
  | false
  | null
  | undefined;

/**
 * Returns names of classes with given parameters
 *
 * @param classnames - object of className
 * @returns The string of collected classNames
 *
 */
export default function classNames(...classnames: ClassName[]) {
  let result: string[] = [];

  classnames.forEach((item: ClassName): void => {
    if (!item) {
      return;
    }
    switch (typeof item) {
      case "string":
        result.push(item);
        break;
      case "object":
        Object.keys(item).forEach((key: string) => {
          if (item[key]) {
            result.push(key);
          }
        });
        break;
      default:
        result.push(`${item}`);
    }
  });

  return result.join(" ");
}
