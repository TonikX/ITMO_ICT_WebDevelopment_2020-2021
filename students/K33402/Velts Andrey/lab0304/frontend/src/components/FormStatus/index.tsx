import React, { FunctionComponent, HTMLAttributes, ReactNode } from "react";
import { classNames } from "utils";
import { AiOutlineExclamationCircle } from "react-icons/ai";

export interface FormStatusProps extends HTMLAttributes<HTMLDivElement> {
  mode?: "default" | "error";
  header?: ReactNode;
}

const FormStatus: FunctionComponent<FormStatusProps> = ({
  mode,
  header,
  children,
  className,
  dangerouslySetInnerHTML,
  ...restProps
}: FormStatusProps) => {
  return (
    <div
      {...restProps}
      className={classNames("FormStatus", `FormStatus--${mode}`, className)}
    >
      {header && <div className="FormStatus__header">{header}</div>}
      {dangerouslySetInnerHTML && (
        <div
          className="FormStatus__content"
          dangerouslySetInnerHTML={dangerouslySetInnerHTML}
        />
      )}
      {children && !dangerouslySetInnerHTML && (
        <div className="FormStatus__content">
          <div className="FormStatus__content-before">
            <AiOutlineExclamationCircle />
          </div>
          {children}
        </div>
      )}
    </div>
  );
};

export default FormStatus;
