import React, {
  FunctionComponent,
  ReactNode,
  ElementType,
  ButtonHTMLAttributes,
} from "react";
import { Link } from "react-router-dom";
import { classNames } from "utils";
import { HasRootRef } from "types/props";

export interface ButtonProps
  extends HasRootRef<HTMLElement>,
    ButtonHTMLAttributes<HTMLElement> {
  mode?:
    | "primary"
    | "secondary"
    | "tertiary"
    | "icon"
    | "commerce"
    | "email"
    | "signup"
    | "oauth"
    | "mode"
    | "link";
  stretched?: boolean;
  before?: ReactNode;
  after?: ReactNode;
  component?: ElementType;
  href?: string;
  target?: string;
  to?: string;
}

const Button: FunctionComponent<ButtonProps> = (props: ButtonProps) => {
  const {
    className,
    mode,
    stretched,
    children,
    before,
    after,
    component,
    ...restProps
  } = props;
  let ComponentProp: ElementType = component!;

  if (ComponentProp === "button" && restProps.href) {
    ComponentProp = "a";
  }
  if (ComponentProp === "button" && restProps.to) {
    ComponentProp = Link;
  }

  return (
    <ComponentProp
      className={classNames(className, `Button`, `Button--lvl-${mode}`, {
        "Button--link": !!restProps.href || !!restProps.to,
      })}
      {...restProps}
    >
      <div className="Button__in">
        {before && <div className="Button__before">{before}</div>}
        {children && <div className="Button__content">{children}</div>}
        {after && <div className="Button__after">{after}</div>}
      </div>
    </ComponentProp>
  );
};

Button.defaultProps = {
  mode: "primary",
  component: "button",
  stretched: false,
};

export default Button;
