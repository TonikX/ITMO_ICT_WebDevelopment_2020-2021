import React, {
  FunctionComponent,
  InputHTMLAttributes,
  RefCallback,
  ChangeEvent,
} from "react";
import { classNames } from "utils";
import { FormField } from "components";
import { HasFormLabels } from "types/props";

export interface InputProps
  extends HasFormLabels,
    InputHTMLAttributes<HTMLInputElement> {
  align?: "left" | "center" | "right";
  error?: string;
  getRef?: RefCallback<HTMLInputElement> | null;
  value: string | number;
  onSubmit?: () => void;
  handleChange: (e: ChangeEvent<HTMLInputElement>) => void;
}

const Input: FunctionComponent<InputProps> = ({
  align,
  getRef,
  error,
  value,
  handleChange,
  className,
  top,
  bottom,
  ...restProps
}: InputProps) => {
  return (
    <FormField
      className={classNames("Input", className, {
        [`Input--${align}`]: !!align,
      })}
      error={error}
      bottom={bottom}
    >
      <input
        {...restProps}
        value={value}
        onChange={handleChange}
        className="Input__el"
        ref={getRef}
      />
    </FormField>
  );
};

Input.defaultProps = {
  type: "text",
};

export default Input;
