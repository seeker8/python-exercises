/*global require*/
'use strict';

require.config({
    shim: {
        modernizr: {
            exports: 'Modernizr'
        }
    },
    paths: {
        jquery: '../bower_components/jquery/dist/jquery',
        backbone: '../bower_components/backbone/backbone',
        underscore: '../bower_components/lodash/dist/lodash',
        modernizr: '../bower_components/modernizr/modernizr'
    }
});

require([
    'backbone',
    'routes/router'
], function (Backbone, Router) {
    new Router();
    Backbone.history.start();

});
