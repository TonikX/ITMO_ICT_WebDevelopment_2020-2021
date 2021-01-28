const axios = require('axios');
require('dotenv').config();

exports.handler = async (event) => {

  // Create query to DB
  const { itemId, newTitle, newStatus, userId } = JSON.parse(event.body);
  const QUERY = `
    mutation updateItem {
      updateItem(
        id: "${itemId}"
        data: {
          title: "${newTitle}"
          status: ${newStatus}
          user: {
            connect: "${userId}"
          }
        }
      ) {
        _id
        title
        status
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