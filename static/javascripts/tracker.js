'user strict';

var dependencies = [
    'ngRoute',
    'ui.router',
    'ui.bootstrap'
];

var app = angular
  .module('tracker', dependencies);

app.config([
        '$stateProvider', '$urlRouterProvider', '$locationProvider', '$interpolateProvider'
    , function ($stateProvider, $urlRouterProvider, $locationProvider, $interpolateProvider) {
/*
    $urlRouterProvider.otherwise('/');
    $locationProvider.hashPrefix('!');
    $stateProvider
        .state('tracker', {
            url: '/',
            views: {
                'routerView': {
                    template: '/static/views/home.html',
                    controller: 'trackerCtrl'
                }
            }
        });
*/
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
}]);
