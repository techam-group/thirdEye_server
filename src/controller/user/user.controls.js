const User = require('../../models/user/user.schema');
const utils = require('../../lib/js/utils');

module.exports = {
  addNewUser: async (req, res) => {
    let {email, password, username} = req.body;
    const foundUser = await User.findOne({ email });

    if (foundUser) {
      res.status(400).send('Email already exists');
      throw new Error('Email already exists');
    }

    password = await utils.hashPassword(password);

    const user = await User.create({email, password, username});

    const token = await utils.createToken({
      username: user.username,
      email: user.email,
      created: user.createdAt
    });

    res.status(200).json({
      username: user.username,
      email: user.email,
      token
    })
  },

  login: async (req, res) => {
    const { email, password } = req.body;
    const foundUser = await User.findOne({ email });

    if (!foundUser) {
      res.status(400).send('Email not does not exist');
      throw new Error('Email not does not exist');
    }

    const matchedPassword = await utils.comparePassword(password, foundUser.password);

    if (!matchedPassword) {
      res.status(400).send('Invalid password');
      throw new Error('Invalid password');
    }

    const token = await utils.createToken({
      username: foundUser.username,
      email: foundUser.email
    });

    res.status(200).json({
      username: foundUser.username,
      email: foundUser.email,
      token
    })
  },

  update: async (req, res) => {
    await res.send('login you in')
  }
};
