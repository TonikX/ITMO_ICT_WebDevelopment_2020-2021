import React, {
  FunctionComponent,
  SelectHTMLAttributes,
  RefCallback,
  ChangeEvent,
} from "react";
import { classNames } from "utils";
import { FormField } from "components";
import { HasFormStatus, HasFormLabels } from "types/props";
import { AiOutlineDown } from "react-icons/ai";

export interface SelectProps
  extends SelectHTMLAttributes<HTMLSelectElement>,
    HasFormStatus,
    HasFormLabels {
  align?: "left" | "center" | "right";
  error?: string;
  getRef?: RefCallback<HTMLSelectElement> | null;
  value?: string | number;
  onSubmit?: () => void;
  handleChange: (e: ChangeEvent<HTMLSelectElement>) => void;
  isSignup?: boolean;
}

const Select: FunctionComponent<SelectProps> = ({
  placeholder,
  children,
  align,
  getRef,
  error,
  value,
  title,
  status,
  handleChange,
  className,
  style,
  bottom,
  isSignup,
  ...restProps
}: SelectProps) => {
  return (
    <FormField
      Component="label"
      className={classNames(
        "Select",
        {
          "Select--signup": !!isSignup,
          [`Select--align-${align}`]: !!align,
        },
        className
      )}
      style={style}
      status={status}
      error={error}
      bottom={bottom}
    >
      <select {...restProps} onChange={handleChange} className="Select__el">
        {placeholder && <option value="">{placeholder}</option>}
        {children}
      </select>
      <div className="Select__container">
        <div className="Select__title">{title}</div>
        <div className="Select__icon">
          <AiOutlineDown />
        </div>
      </div>
    </FormField>
  );
};

export default Select;
