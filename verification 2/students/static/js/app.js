var module = angular.module("sampleApp", ['ngRoute']);
module.config(function ($httpProvider, $interpolateProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
})

module.run(function ($http, $cookies) {
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
});

module.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/route1', {
                templateUrl: static_url + 'everify/html/test1.html',
                controller: 'RouteController1'
            }).
            when('/route2', {
                templateUrl: static_url + 'everify/html/test2.html',
                controller: 'RouteController2'
            }).
            otherwise({
                redirectTo: '/'
            });
    }]);

module.controller("RouteController1", function($scope) {
    $scope.test="Thisorking test1"
});
module.controller("RouteController2", function($scope) {
    $scope.test="Thisorking test"
});