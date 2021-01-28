import { axios } from "core";

export const getLost = async () => {
  let { data } = await axios.get("/lost/");
  return data;
};

export const createLost = async (lost: FormData) => {
  let { data } = await axios.post("/lost/", lost, {
    headers: {
      "Content-Type": "multipart/form-data",
    },
  });
  return data;
};
