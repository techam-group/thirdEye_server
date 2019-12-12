const express = require('express');
const router = express.Router();

const userController = require('../../controller/user/user.controls');

router.post('/new', userController.addNewUser);
router.post('/login', userController.login);
router.put('/update', userController.update);

module.exports = router;
