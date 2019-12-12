require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const {PORT, MDB_URL} = process.env;

const userRoutes = require('./src/routes/user/user.routes');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

const options = {
  useNewUrlParser: true,
  useCreateIndex: true,
  useUnifiedTopology: true,
  useFindAndModify: false
};

mongoose.connect(MDB_URL, options)
  .then(() => console.log('Connected to DB...'))
  .catch(err => {
    console.log(`Error Connecting to DB`);
    console.log('----------------------');
    console.log(err);
  });

app.use('/user', userRoutes);

app.listen(PORT, () => console.log(`server running on http://localhost:${PORT}`));
