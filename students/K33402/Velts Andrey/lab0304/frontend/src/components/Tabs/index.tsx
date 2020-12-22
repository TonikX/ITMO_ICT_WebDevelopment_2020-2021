import * as React from "react";
import RcTabs, {
  TabPane,
  TabsProps as RcTabsProps,
  TabPaneProps as RcTabPaneProps,
} from "rc-tabs";
import { EditableConfig } from "rc-tabs/lib/interface";
import { classNames } from "utils";
import {
  AiOutlineEllipsis,
  AiOutlinePlus,
  AiOutlineClose,
} from "react-icons/ai";

export type TabsType = "line" | "card" | "editable-card";
export type TabsPosition = "top" | "right" | "bottom" | "left";

export type TabPaneProps = RcTabPaneProps;

export interface TabsProps extends Omit<RcTabsProps, "editable"> {
  type?: TabsType;
  hideAdd?: boolean;
  centered?: boolean;
  addIcon?: React.ReactNode;
  onEdit?: (
    e: React.MouseEvent | React.KeyboardEvent | string,
    action: "add" | "remove"
  ) => void;
}

function Tabs({
  type,
  className,
  onEdit,
  hideAdd,
  centered,
  addIcon,
  ...props
}: TabsProps) {
  let editable: EditableConfig | undefined;
  if (type === "editable-card") {
    editable = {
      onEdit: (editType, { key, event }) => {
        onEdit?.(editType === "add" ? event : key!, editType);
      },
      removeIcon: <AiOutlineClose />,
      addIcon: addIcon || <AiOutlinePlus />,
      showAdd: hideAdd !== true,
    };
  }
  return (
    <RcTabs
      {...props}
      className={classNames(className, {
        [`Tabs-card`]: ["card", "editable-card"].includes(type as string),
        [`Tabs-editable-card`]: type === "editable-card",
        [`Tabs-centered`]: !!centered,
      })}
      editable={editable}
      moreIcon={<AiOutlineEllipsis />}
      prefixCls="Tabs"
    />
  );
}

Tabs.TabPane = TabPane;

export default Tabs;
