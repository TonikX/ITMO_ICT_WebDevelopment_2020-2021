import React, {
  useState,
  useEffect,
  useCallback,
  FunctionComponent,
  ChangeEvent,
  Dispatch,
  SetStateAction,
} from "react";
import { useSelector, useDispatch } from "react-redux";
import Dialog from "rc-dialog";
import { AiOutlineCamera, AiOutlineEdit } from "react-icons/ai";
import { IoMdClose } from "react-icons/io";
import { Input, Button, File, FormStatus } from "components";
import { PostPetProps } from "types/store";
import { postLost } from "store/lost";
import { RootState } from "store/rootReducer";

export interface PostProps {
  visible: boolean;
  setVisible: Dispatch<SetStateAction<boolean>>;
}

const Post: FunctionComponent<PostProps> = (props: PostProps) => {
  const { visible, setVisible } = props;
  const dispatch = useDispatch();
  const { error, isLoading } = useSelector((state: RootState) => state.lost);
  const [image, setImage] = useState("");
  const [postValue, setPostValue] = useState<PostPetProps>({
    name: "",
    age: "",
    city: "",
    gender: "",
    description: "",
    location: "",
    contacts: "",
    image: "",
  });
  const [errorsValue, setErrorsValue] = useState<PostPetProps>({
    name: "",
    age: "",
    city: "",
    gender: "",
    description: "",
    location: "",
    contacts: "",
    image: "",
  });
  const [isSent, setIsSent] = useState(false);

  const onClose = useCallback(() => {
    setIsSent(false);
    setPostValue({
      name: "",
      age: "",
      city: "",
      gender: "",
      description: "",
      location: "",
      contacts: "",
      image: "",
    });
    setErrorsValue({
      name: "",
      age: "",
      city: "",
      gender: "",
      description: "",
      location: "",
      contacts: "",
      image: "",
    });
    setVisible(false);
  }, [setVisible]);

  const onChange = (e: ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    let value: string = e.target.value;
    const name = e.target.name;
    setPostValue({ ...postValue, [name]: value });
  };

  const submitPost = () => {
    const valid = !Object.values(postValue).some((x) => x === null);
    console.log(valid);
    console.log(555);
    if (valid) {
      const data = new FormData();
      Object.keys(postValue).forEach((key) => data.append(key, postValue[key]));
      console.log(data);
      data.forEach((value, key) => {
        console.log(key + " " + value);
      });
      dispatch(postLost(data));
      setIsSent(true);
    }
  };

  const uploadImage = (e: React.ChangeEvent<HTMLInputElement>) => {
    e.preventDefault();
    if (e.target.files) {
      const file = e.target.files[0];
      setPostValue({ ...postValue, image: file });
      setImage(URL.createObjectURL(file));
    }
  };

  useEffect(() => {
    if (!isLoading && !error && isSent) {
      onClose();
    }
  }, [isLoading, error, isSent, onClose]);

  return (
    <Dialog
      visible={visible}
      animation="zoom"
      maskAnimation="fade"
      onClose={onClose}
      style={{ width: 684 }}
      title={<h1>Настройки</h1>}
      prefixCls="Post"
      closeIcon={<IoMdClose />}
      destroyOnClose
    >
      <div className="Post__field-upload">
        <File
          before={!image ? <AiOutlineCamera /> : <AiOutlineEdit />}
          onChange={uploadImage}
        >
          {!image ? "Добавить фото" : "Изменить фото"}
        </File>
      </div>
      <div className="Post__form">
        {error && <FormStatus mode="error">{error}</FormStatus>}
        <div className="Post__field">
          <span className="Post__field-name">Кличка</span>
          <div className="Post__field-input Post__field-single">
            <Input
              name="name"
              value={postValue["name"] ? postValue["name"] : ""}
              bottom={errorsValue["name"]}
              handleChange={onChange}
            />
          </div>
        </div>
        <div className="Post__field">
          <span className="Post__field-name">Возраст</span>
          <div className="Post__field-input Post__field-single">
            <Input
              name="age"
              value={postValue["age"] ? postValue["age"] : ""}
              bottom={errorsValue["age"]}
              handleChange={onChange}
            />
          </div>
        </div>
        <div className="Post__field">
          <span className="Post__field-name">Город</span>
          <div className="Post__field-input Post__field-single">
            <Input
              name="city"
              value={postValue["city"] ? postValue["city"] : ""}
              bottom={errorsValue["city"]}
              handleChange={onChange}
            />
          </div>
        </div>
        <div className="Post__field">
          <span className="Post__field-name">Место</span>
          <div className="Post__field-input Post__field-single">
            <Input
              name="location"
              value={postValue["location"] ? postValue["location"] : ""}
              bottom={errorsValue["location"]}
              handleChange={onChange}
            />
          </div>
        </div>
        <div className="Post__field">
          <span className="Post__field-name">Приметы</span>
          <div className="Post__field-input Post__field-single">
            <Input
              name="description"
              value={postValue["description"] ? postValue["description"] : ""}
              bottom={errorsValue["description"]}
              handleChange={onChange}
            />
          </div>
        </div>
        <div className="Post__field">
          <span className="Post__field-name">Пол</span>
          <div className="Post__field-input Post__field-single">
            <Input
              name="gender"
              value={postValue["gender"] ? postValue["gender"] : ""}
              bottom={errorsValue["gender"]}
              handleChange={onChange}
            />
          </div>
        </div>
        <div className="Post__field Post__field--large">
          <span className="Post__field-name">Контакты</span>
          <div className="Post__field-input Post__field-single">
            <Input
              name="contacts"
              value={postValue["contacts"] ? postValue["contacts"] : ""}
              bottom={errorsValue["contacts"]}
              handleChange={onChange}
            />
          </div>
        </div>
      </div>
      <div className="Post__field-input Post__field-field">
        <Button mode="primary" onClick={submitPost} disabled={isLoading}>
          Опубликовать
        </Button>
      </div>
    </Dialog>
  );
};

export default Post;
