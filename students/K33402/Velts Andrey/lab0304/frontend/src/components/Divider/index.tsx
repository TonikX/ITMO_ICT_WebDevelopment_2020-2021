import React, { FunctionComponent } from "react";
import { classNames } from "utils";

export interface DividerProps {
  type?: "horizontal" | "vertical";
  size?: "medium" | "small";
  orientation?: "left" | "right" | "center";
  className?: string;
  children?: React.ReactNode;
  dashed?: boolean;
  style?: React.CSSProperties;
  plain?: boolean;
}

const Divider: FunctionComponent<DividerProps> = (props: DividerProps) => {
  const {
    className,
    children,
    dashed,
    plain,
    type,
    size,
    ...restProps
  } = props;

  return (
    <div
      className={classNames(className, "Divider", `Divider-size-${size}`, {
        "Divider-horizontal": type === "horizontal",
        "Divider-vertical": type === "vertical",
        "Divider-with-text": !!children,
        "Divider-dashed": !!dashed,
        "Divider-plain": !!plain,
      })}
      {...restProps}
      role="separator"
    >
      {children && <span className="Dinner-inner-text">{children}</span>}
    </div>
  );
};

Divider.defaultProps = {
  type: "horizontal",
  orientation: "center",
  size: "medium",
};

export default Divider;
