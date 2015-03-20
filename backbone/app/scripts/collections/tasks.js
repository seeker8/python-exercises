/*global define*/

define([
    'underscore',
    'backbone',
    'models/task',
    'localstorage'
], function (_, Backbone, TasksModel) {
    'use strict';

    return Backbone.Collection.extend({
        model: TasksModel,
        localStorage: new Backbone.LocalStorage('TaskCollection')
    });
});
