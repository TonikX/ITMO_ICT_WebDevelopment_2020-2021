export interface BasicProps {
  error?: string | null;
  isLoading: boolean;
}

export interface UserProps {
  id?: number;
  token?: string;
  username?: string;
  email?: string;
  name?: string;
  first_name?: string;
  last_name?: string;
  city?: string;
  country?: string;
  location?: string;
  phone_number?: number | null;
  [name: string]: any;
}

export interface SignupUserProps {
  email: string;
  first_name: string;
  last_name: string;
  password1: string;
  password2: string;
  country: string;
  country_code: string;
  city: string;
  [name: string]: any;
}

export interface PasswordChangeProps {
  old_password: string;
  new_password1: string;
  new_password2: string;
}

export type UserState = UserProps & BasicProps;

export interface UserSuccessProps {
  token: string;
  user: UserProps;
}

// Pets

export interface PetProp {
  id: number;
  name: string;
  age: string;
  gender: string;
  image: string;
}

export interface PetsProps {
  pets: PetProp[];
}

export type PetsState = PetsProps & BasicProps;

// Charity

export interface CharityProp {
  id: number;
  title: string;
  description: string;
  goal_money: number;
  current_money: number;
  donation_times: number;
  image: string;
}

export interface CharitiesProps {
  charities: CharityProp[];
}

export type CharitiesState = CharitiesProps & BasicProps;

// Lost

export interface LostPetProps {
  id: number;
  name: string;
  age: string;
  city: string;
  gender: string;
  description: string;
  location: string;
  contacts: string;
  image: string;
}

export interface PostPetProps {
  name: string;
  age: string;
  city: string;
  gender: string;
  description: string;
  location: string;
  contacts: string;
  image: string | File;
  [name: string]: any;
}

export interface LostPetsProps {
  lost: LostPetProps[];
}

export type LostPetsState = LostPetsProps & BasicProps;

// Events

export interface EventProps {
  id: number;
  title: string;
  description: string;
  start_date: string;
  end_date: string;
  category: string;
}

export interface EventsSuccessProps {
  [date: number]: EventProps[] | [];
}

export interface EventsProps {
  events: EventsSuccessProps;
}

export type EventsState = EventsProps & BasicProps;
