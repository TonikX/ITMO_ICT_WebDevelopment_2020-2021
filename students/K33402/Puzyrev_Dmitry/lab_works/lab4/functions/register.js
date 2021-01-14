const axios = require('axios');
require('dotenv').config();

exports.handler = async (event) => {

  // Create query to DB
  const { name, email, pass } = JSON.parse(event.body);
  const QUERY = `
    mutation registerUser {
      createUser(data: {
        name: "${name}"
        email: "${email}"
        password:"${pass}"
      }) {
        _id
        name
        email
      }
    }
  `

  const {data} = await axios({
    url: 'https://graphql.fauna.com/graphql',
    method: 'POST',
    headers: {
      Authorization: `Bearer ${process.env.FAUNA_SECRET_KEY}`
    },
    data: {
      query: QUERY,
      variables: {},
    }
  })

  return {
    statusCode: 200,
    body: JSON.stringify(data),
  };
};