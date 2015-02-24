/*global define*/

define([
    'jquery',
    'backbone'
], function ($, Backbone) {
    'use strict';

    var RouterRouter = Backbone.Router.extend({
        routes: {
            'about/:name': 'about',
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
            console.log('route '+name);
            $('#content').empty().html('<h1>Hello '+name+'</h1>');
        }

    });

    return RouterRouter;
});
