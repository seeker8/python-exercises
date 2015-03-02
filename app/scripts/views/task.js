/*global define*/

define([
    'jquery',
    'underscore',
    'backbone',
    'templates'
], function ($, _, Backbone, JST) {
    'use strict';

    var TaskView = Backbone.View.extend({
        template: JST['app/scripts/templates/task.hbs'],

        tagName: 'ul',

        id: 'tasks',

        className: 'list-group',

        events: {
            'click .task':'showDesc'
        },

        showDesc:function(e){
          $(e.currentTarget).next().toggleClass('hide');
        },

        initialize: function () {
           // this.listenTo(this.model, 'change', this.render);
        },

        render: function () {
            var summary = this.model.countBy(function(item){
                return item.attributes.done?'done':'pending';
            });
            console.log(summary);
            this.$el.html(this.template({
                tasks: this.model.toJSON(),
                summary: summary
            }));
        }
    });

    return TaskView;
});
