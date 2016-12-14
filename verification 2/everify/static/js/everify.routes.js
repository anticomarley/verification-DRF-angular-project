(function () {
  'use strict';

  angular
    .module('everify.routes')
    .config(config);

  config.$inject = ['$routeProvider'];

  /**
  * @name config
  * @desc Define valid application routes
  */
  function config($routeProvider) {
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
  }
})();