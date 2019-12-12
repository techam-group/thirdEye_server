const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const {SECRET_KEY} = process.env;

module.exports = {
  hashPassword: async (password) => {
    try {
      return await bcrypt.hash(password, 20);
    } catch (e) {
      console.log(e);
      return e.message
    }
  },

  comparePassword: async (password, oldPassword) => {
    try {
      return await bcrypt.compare(password, oldPassword)
    } catch (e) {
      console.log(`Error: ${e}`);
      return e.message;
    }
  },

  createToken: async (payload) => {
    try {
      return await jwt.sign(payload, SECRET_KEY, { expiresIn: '48hrs' })
    } catch (e) {
      console.log(e);
      return e.message;
    }
  }
};
