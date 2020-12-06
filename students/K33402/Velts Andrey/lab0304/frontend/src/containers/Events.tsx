import { useEffect } from "react";
import { useSelector, useDispatch } from "react-redux";
import { Events as BaseEvents } from "components";
import { RootState } from "store/rootReducer";
import { fetchEvents } from "store/events";

const Events = () => {
  const dispatch = useDispatch();
  const { events, isLoading } = useSelector((state: RootState) => state.events);

  useEffect(() => {
    dispatch(fetchEvents());
  }, [dispatch]);

  return <BaseEvents events={events} isLoading={isLoading} />;
};

export default Events;
