import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Pets as BasePets } from "components";
import { RootState } from "store/rootReducer";
import { fetchPets } from "store/pets";

const Pets = () => {
  const dispatch = useDispatch();
  const { pets, isLoading } = useSelector((state: RootState) => state.pets);

  useEffect(() => {
    dispatch(fetchPets());
  }, [dispatch]);

  return <BasePets pets={pets} isLoading={isLoading} />;
};

export default Pets;
