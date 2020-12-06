import { ReactNode } from "react";

export type FormStatusType = "default" | "error" | "valid";

export interface HasAlign {
  align?: "left" | "center" | "right";
}

export type OldRef<T> = (el: T) => void;

export interface RefWithCurrent<T> {
  current: T | null;
}

export interface HasRootRef<T> {
  getRootRef?: OldRef<T> | RefWithCurrent<T>;
}

export interface HasRef<T> {
  getRef?: OldRef<T> | RefWithCurrent<T>;
}

export interface HasChildren {
  children?: ReactNode;
}

export interface HasFormStatus {
  status?: FormStatusType;
}

export interface HasFormLabels {
  top?: ReactNode;
  bottom?: ReactNode;
}

export interface PaginationProps {
  pageSize?: number;
  count?: number;
  total?: number;
  current?: number;
}
