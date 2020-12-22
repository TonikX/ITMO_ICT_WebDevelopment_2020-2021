import { FunctionComponent } from "react";
import { Spinner } from "components";
import { PetProp } from "types/store";
import { BACKEND_URL } from "settings";

export interface PetsProps {
  pets: PetProp[];
  isLoading: boolean;
}

const Pets: FunctionComponent<PetsProps> = (props: PetsProps) => {
  const { pets, isLoading } = props;

  if (isLoading) {
    return (
      <div className="Pets">
        <Spinner size="large" />
      </div>
    );
  }

  return (
    <div className="Pets">
      <h3>Дом любимым</h3>
      <h1>
        Они нуждаются в Вашей <br />
        любви прямо сейчас
      </h1>
      <div className="Pets__content">
        {pets &&
          pets.length > 0 &&
          pets.map((pet) => (
            <div className="Pets__card">
              <img
                className="Pets__card-image"
                alt="Pet"
                src={`${BACKEND_URL}${pet.image}`}
              />
              <div className="Pets__card-name">{pet.name}</div>
              <div className="Pets__card-description">{`${pet.gender} / ${pet.age}`}</div>
            </div>
          ))}
      </div>
    </div>
  );
};

export default Pets;
