/*global require*/
'use strict';

require.config({
    baseUrl: '/scripts',
    shim: {
        modernizr: {
            exports: 'Modernizr'
        },
        handlebars: {
            exports: 'Handlebars'
        }
    },
    paths: {
        jquery: '../bower_components/jquery/dist/jquery',
        backbone: '../bower_components/backbone/backbone',
        underscore: '../bower_components/lodash/dist/lodash',
        modernizr: '../bower_components/modernizr/modernizr'
    }
});

var specFolder = '../../spec'

require([
     specFolder + 'demo'
], function (Backbone, Router) {
    mocha.run();
});

