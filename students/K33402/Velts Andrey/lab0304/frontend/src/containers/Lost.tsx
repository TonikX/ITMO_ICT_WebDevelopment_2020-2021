import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Lost as BaseLost } from "components";
import { RootState } from "store/rootReducer";
import { fetchLost } from "store/lost";

const Charity = () => {
  const dispatch = useDispatch();
  const { lost, isLoading } = useSelector((state: RootState) => state.lost);

  useEffect(() => {
    dispatch(fetchLost());
  }, [dispatch]);

  return <BaseLost lost={lost} isLoading={isLoading} />;
};

export default Charity;
