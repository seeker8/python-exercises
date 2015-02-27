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
        jquery: '../bower_components/jquery/dist/jquery',
        backbone: '../bower_components/backbone/backbone',
        underscore: '../bower_components/lodash/dist/lodash',
        modernizr: '../bower_components/modernizr/modernizr',
        localstorage: '../bower_components/backbone.localstorage/backbone.localStorage',
        handlebars: '../bower_components/handlebars/handlebars'
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
