import { axios } from "core";

export const getPets = async () => {
  let { data } = await axios.get("/pets/");
  return data;
};
