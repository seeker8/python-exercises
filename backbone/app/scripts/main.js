/*global require*/
'use strict';

require.config({
    shim: {
        modernizr: {
            exports: 'Modernizr'
        },
        handlebars: {
            exports: 'Handlebars'
        }
    },
    paths: {
        jquery: 'vendor/jquery/jquery',
        backbone: 'vendor/backbone/dist/backbone',
        underscore: '../bower_components/lodash/dist/lodash',
        modernizr: 'vendor/modernizr/modernizr',
        localstorage: 'vendor/backbone/localStorage/backbone.localStorage',
        handlebars: 'vendor/handlebars/handlebars'
    }
});

require([
    'backbone',
    'routes/router',
    'handlebars'
], function (Backbone, Router) {
    new Router();
    Backbone.history.start({
        root: '/',
        pushState: true
    });

    $(document).delegate('a', 'click', function (evt) {
        var href = $(this).attr('href');
        evt.preventDefault();
        Backbone.history.navigate(href, true);
    });

});
