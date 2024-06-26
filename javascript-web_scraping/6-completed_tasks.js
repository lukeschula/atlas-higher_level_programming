#!/usr/bin/node

const request = require('request');
const Url = process.argv[2];

request(Url, (error, response) => {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(response.body);
  const newTask = {};
  for (const task of data) {
    if (task.completed) {
      if (newTask[task.userId]) {
        newTask[task.userId]++;
      } else {
        newTask[task.userId] = 1;
      }
    }
  }
  console.log(newTask);
});
