import React, { FunctionComponent } from "react";
import { classNames } from "utils";
import { AiOutlineLoading } from "react-icons/ai";

export interface SpinnerProps extends React.HTMLAttributes<HTMLDivElement> {
  size?: "small" | "regular" | "large" | "medium";
}

const Spinner: FunctionComponent<SpinnerProps> = ({
  className,
  size,
  ...restProps
}: SpinnerProps) => {
  return (
    <div
      {...restProps}
      className={classNames(className, "Spinner", `Spinner-${size}`)}
    >
      <AiOutlineLoading className="Spinner__self" />
    </div>
  );
};

Spinner.defaultProps = {
  size: "regular",
};

export default React.memo(Spinner);
