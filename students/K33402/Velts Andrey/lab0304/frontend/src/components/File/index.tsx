import { ReactNode, FunctionComponent, InputHTMLAttributes } from "react";
import { Button } from "components";
import { classNames } from "utils";
import { HasRef, HasRootRef } from "types/props";

export interface FileProps
  extends InputHTMLAttributes<HTMLInputElement>,
    HasRef<HTMLInputElement>,
    HasRootRef<HTMLElement> {
  before?: ReactNode;
}

const File: FunctionComponent<FileProps> = (props: FileProps) => {
  const {
    children,
    className,
    style,
    getRef,
    getRootRef,
    before,
    ...restProps
  } = props;

  return (
    <Button
      className={classNames("File", className)}
      component="label"
      mode="tertiary"
      style={style}
      before={before}
      getRootRef={getRootRef}
      disabled={restProps.disabled}
    >
      <input {...restProps} className="File__input" type="file" ref={getRef} />
      {children}
    </Button>
  );
};

File.defaultProps = {
  children: "Выберите файл",
};

export default File;
