/*global define*/

define([
    'jquery',
    'backbone'
], function ($, Backbone, Modernizr, InternalDependency) {
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
            $('#content').empty().html('<h1>Hello '+name+'</h1>');
        }

    });

    return RouterRouter;
});
