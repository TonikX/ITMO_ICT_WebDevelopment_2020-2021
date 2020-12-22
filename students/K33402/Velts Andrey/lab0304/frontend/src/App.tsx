import React, { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { authCheckState } from "store/user";
import { RootState } from "store/rootReducer";
import { Route, Switch, Redirect } from "react-router-dom";
import { Layout } from "components";
import { About, Pets, Charity, Events, Lost, Signup } from "pages";

const { Sidebar, Content } = Layout;

const App = () => {
  const dispatch = useDispatch();
  const { token } = useSelector((state: RootState) => state.user);

  useEffect(() => {
    dispatch(authCheckState());
  }, [dispatch]);

  return (
    <Layout>
      <Sidebar />
      <Content>
        <Switch>
          <Route exact path="/" component={About} />
          <Route exact path="/pets" component={Pets} />
          <Route path="/charity" component={Charity} />
          <Route exact path="/events" component={Events} />
          <Route exact path="/lost" component={Lost} />
          <Route
            path="/signup"
            render={() => (token ? <Redirect to="/" /> : <Signup />)}
          />
        </Switch>
      </Content>
    </Layout>
  );
};

export default App;
