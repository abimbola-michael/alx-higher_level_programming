#!/usr/bin/node
// a script that computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

request.get(url, (error, res, data) => {
  if (error) {
    console.log(error);
  } else {
    const todos = JSON.parse(data);
    const completedTasks = {};
    todos.forEach((todo) => {
      if (todo.completed) {
        if (completedTasks[todo.userId]) {
          completedTasks[todo.userId] += 1;
        } else {
          completedTasks[todo.userId] = 1;
        }
      }
    });
    console.log(completedTasks);
  }
});
