/**
 * Created by lyhapple on 15/11/6.
 */

_.mixin(s.exports());

Vue.config.delimiters = ['#[', ']'];
Vue.config.unsafeDelimiters = ['{!!', '!!}'];
Vue.filter('length', function (items) {
    return items.length;
});
Vue.filter('replace', function (str, find, replace) {
    return str.replaceAll(find, replace);
});

(function($){
    $.AdminLTE.Config = {
        domain: 'http://127.0.0.1:8000'
    };
})(jQuery);