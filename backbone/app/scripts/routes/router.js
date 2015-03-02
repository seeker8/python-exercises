/*global define*/

define([
    'jquery',
    'backbone'
], function ($, Backbone) {
    'use strict';

    return Backbone.Router.extend({
        routes: {
            'about/:name': 'about',
            'tasks': 'task',
            '': 'default'
        },
        default: function () {

            require([
                'modernizr',
                'internal-dependency'
            ], function (Modernizr, InternalDependency) {
                console.log('Default');
                if (Modernizr.history) {
                    console.log('This browser supports push-state routing');
                } else {
                    console.log('This browser does not support Modernizr');
                }

                InternalDependency.doSomething();
                $('#content').empty().html('<h1>HOME</h1>');
            });
        },
        about: function (name) {
            console.log('route ' + name);
            $('#content').empty().html('<h1>Hello ' + name + '</h1>');
        },
        task: function () {
            require([
                'collections/tasks',
                'views/task'
            ], function (TaskCollection, TaskView) {
                localStorage.clear();
                var collection = new TaskCollection();
                collection.create({
                    title: 'Band practice',
                    due: '2015-03-12',
                    done: true,
                    desc:'This is a short description'
                });
                collection.create({
                    title: 'Essay sketch',
                    due: '2015-12-12',
                    done: false,
                    desc:'This is a short description'
                });
                collection.create({
                    title: 'Programming exercises',
                    due: '2015-12-12',
                    done: true,
                    desc:'This is a short description'
                });
                var view = new TaskView({
                    model: collection,
                    el: '#content'
                });
                view.render();
            });
        }

    });
});
