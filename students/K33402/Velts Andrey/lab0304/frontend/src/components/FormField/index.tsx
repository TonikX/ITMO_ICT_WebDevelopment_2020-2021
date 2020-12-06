import React, { ElementType, HTMLAttributes } from "react";
import { classNames } from "utils";
import { HasFormLabels, HasFormStatus } from "types/props";

export interface FormFieldProps
  extends HTMLAttributes<HTMLElement>,
    HasFormLabels,
    HasFormStatus {
  Component?: ElementType;
  error?: string;
}

const FormField: React.FunctionComponent<FormFieldProps> = ({
  Component,
  className,
  children,
  error,
  bottom,
  ...restProps
}: FormFieldProps) => {
  if (!Component) {
    return null;
  }
  return (
    <Component
      {...restProps}
      className={classNames(
        "FormField",
        {
          [`FormField--s-error`]: !!error || !!bottom,
        },
        className
      )}
    >
      {error && <div className="FormField__error">{error}</div>}
      {children}
      {bottom && <div className="FormField__error--bottom">{bottom}</div>}
    </Component>
  );
};

FormField.defaultProps = {
  Component: "div",
};

export default FormField;
