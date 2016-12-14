var module = angular.module('everify', ['ngRoute']);
module.config(function ($httpProvider, $interpolateProvider) {
    $interpolateProvider.startSymbol('{$').endSymbol('$}');
    $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
})

module.run(function ($http, $cookies) {
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
});

module.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.when('/student_alumni_registration', {
          controller: 'RegisterController', 
          controllerAs: 'vm',
          templateUrl: 'partials/student_register.html'
        }).when('/institution_registration', {
          controller: 'RegisterController',
          controllerAs: 'vm',
          templateUrl: 'partials/institution_register.html'
        }).when('/corporate_registration', {
          controller: 'RegisterController', 
          controllerAs: 'vm',
          templateUrl: 'partials/corporate_register.html'
        }).otherwise({redirectTo:'/'});
  
    }]);

module.controller('RegisterControllerw', function($scope) {
    $scope.test="Thisorking test1"
});
module.controller('RouteController2', function($scope) {
    $scope.test="Thisorking test"
});
module.controller('RouteController2', function($scope) {
    $scope.test="Thisorking test"
});