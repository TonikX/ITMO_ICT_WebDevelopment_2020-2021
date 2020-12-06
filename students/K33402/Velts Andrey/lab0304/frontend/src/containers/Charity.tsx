import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Charity as BaseCharity } from "components";
import { RootState } from "store/rootReducer";
import { fetchCharity } from "store/charity";

const Charity = () => {
  const dispatch = useDispatch();
  const { charities, isLoading } = useSelector(
    (state: RootState) => state.charity
  );

  useEffect(() => {
    dispatch(fetchCharity());
  }, [dispatch]);

  return <BaseCharity charities={charities} isLoading={isLoading} />;
};

export default Charity;
