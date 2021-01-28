import { axios } from "core";

export const getCharities = async () => {
  let { data } = await axios.get("/charity/");
  return data;
};
