const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const userSchema = new Schema({
  username: {
    type: String,
    minLength: 3,
    unique: true,
    required: true
  },
  email: {
    type: String,
    minLength: 8,
    unique: true,
    required: true
  },
  password: {
    type: String,
    required: true
  }
}, { timestamp: true });

const User = mongoose.model('User', userSchema);

module.exports = User;
